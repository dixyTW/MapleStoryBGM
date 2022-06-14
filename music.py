import requests
from lxml import html
import os
from pydub import AudioSegment
from bs4 import BeautifulSoup 
import json


AudioSegment.converter = '/usr/local/Cellar/ffmpeg/5.0.1_2/bin/ffmpeg' # path to ffmpeg, can use avconv if installed correctly

#html_lst = [] #1 - 601 
pagenation = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "A-M", "N-Z_and_Miscellaneous"]
base = "https://maplestory.fandom.com/wiki/Music#"
data = []
with open("bgm.json", 'r') as f:
    data = json.load(f)
# convert json data into filename:item format for easy matching
dic = {}
for item in data:
    dic[item['filename']] = item

r = requests.get(base)
soup = BeautifulSoup(r.content, features='lxml')
audio = soup.find_all("audio") # get all audio tag elements

for a in audio:
    url = a['src']
    doc = requests.get(url)
    name = [s for s in url.split("/") if s.endswith(".ogg")][0][:-4] #obtain name from the download link and trim file type
    filename_ogg = name + ".ogg"
    filename_mp3 = name + ".mp3"
    with open(filename_ogg, 'wb') as f:
        f.write(doc.content)
    ogg_audio = AudioSegment.from_ogg(filename_ogg)
    metadata = {'title': dic[name]['description'], 'artist': dic[name]['metadata']['artist'], 'album': 'Maplestory Soundtrack', 'year':dic[name]['metadata']['year']}
    ogg_audio.export(filename_mp3, format="mp3", tags=metadata)
    os.remove(filename_ogg)
    


