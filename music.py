import requests
from lxml import html
import os
from pydub import AudioSegment

#html_lst = [] #1 - 601 
page = requests.get("https://maplestory.fandom.com/wiki/Music")
tree = html.fromstring(page.content)
track_str = "ogg_player_"
ogg_num = 602
for num in range(1, ogg_num):
	element = tree.get_element_by_id(track_str+str(num))
	semi_lst = html.tostring(element).decode("utf-8").split(";") #url is always the 9th element (8th in index)
	name = semi_lst[-1].split("alt=")[-1][1:-19]
	url = semi_lst[8]
	doc = requests.get(url)
	filename_ogg = name + ".ogg"
	filename_mp3 = name + ".mp3"
	with open(filename_ogg, 'wb') as f:
	    f.write(doc.content)
	ogg_audio = AudioSegment.from_file(filename_ogg, format="ogg")
	ogg_audio.export(filename_mp3, format="mp3")
	os.remove(filename_ogg)