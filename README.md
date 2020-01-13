# MStoryBGM
Short Script that downloads all maplestory BGM (Only works for Mac)

Install all required dependencies via requirements.txt
Also install libav for pydub for ogg to mp3 file conversions
```bash
brew install libav
```
Songs are retrieved through the Maplestory Wiki (link: https://maplestory.fandom.com/wiki/Music)
If you check the source code for the page and search for "ogg_player_1"
You will find yourself at the first song of the list
This script only downloads 1-601
If you want songs beyond 601, go into the script and adjust the ogg_num variable for other songs
I've only allowed number
