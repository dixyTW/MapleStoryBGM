# MapleStoryBGM
Short Script that downloads all Maplestory soundtracks on Maplestory Wiki using Beautifulsoup 

Install all required dependencies via requirements.txt  
## IMPORTANT 
Install ffmpeg for pydub for ogg to mp3 file conversions
```bash
brew install ffmpeg
```
## Usage
aggregate.py is used only for obtaining bgm.json file.  
bgm.json consists of metatdata about the songs.  

After installing all dependencies, run the music.py file in your command line
```bash
python music.py
```
There should be mp3 files starting to pop up in the current directory, download will take some time.

## Credits
Songs are retrieved through the [Maplestory Wiki](https://maplestory.fandom.com/wiki/Music)  

Metadata obtained from [maplestory-db](https://github.com/maplestory-music/maplebgm-db)


