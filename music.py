import requests
from lxml import html
import os
from pydub import AudioSegment
from bs4 import BeautifulSoup 
import json

dir = os.path.dirname(__file__) # current directory path
AudioSegment.converter = '/usr/local/Cellar/ffmpeg/5.0.1_2/bin/ffmpeg' # path to ffmpeg, can use avconv if installed correctly

#html_lst = [] #1 - 601 
base = "https://maplestory.fandom.com/wiki/Music#"
data = []
with open("bgm.json", 'r') as f:
    data = json.load(f)


# There are some consistencies between the Maplestory Wiki naming and the maplestory-db repository
# Replacing all "_" with " " in all filenames across both data to achieve consistency

# convert json data into filename:item format for easy matching
dic = {}
for item in data:
    filename = item['filename'].replace('_', ' ') 
    dic[filename] = item

# retrieve the Maplestory Wiki page using BeautifulSoup
r = requests.get(base)
soup = BeautifulSoup(r.content, features='lxml')
audio = soup.find_all("audio") # get all audio tag elements

mypath = dir + '/BGM'
if not os.path.isdir(mypath):
   os.makedirs(mypath)

for a in audio:
    url = a['src']
    doc = requests.get(url)
    name = ([s for s in url.split("/") if s.endswith(".ogg")][0][:-4]).replace('_', ' ') #obtain name from the download link and trim file type

    filename_ogg = mypath + '/' + name + ".ogg"
    filename_mp3 = mypath + '/' + name + ".mp3"
    with open(filename_ogg, 'wb') as f:
        f.write(doc.content)
    ogg_audio = AudioSegment.from_ogg(filename_ogg)
    metadata = {}
    if name not in dic:
        # inconsistent with maplestorr-db
         metadata = {'title': name, 'artist': "", 'album': "", 'year': ""}
    else:
        metadata = {'title': dic[name]['metadata']['title'], 'artist': dic[name]['metadata']['title'], 'album': dic[name]['description'], 'year':dic[name]['metadata']['year']}
    ogg_audio.export(filename_mp3, format="mp3", tags=metadata)
    os.remove(filename_ogg)
    


