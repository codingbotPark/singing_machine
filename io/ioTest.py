import time
import os
from youtube_search import YoutubeSearch

# 입력값 체크
def CheckInput(song):
	if song == "":
		return "다시 입력해주세요"
	return ""
	
# 노래 검색
def SearchSong(song):
    result = YoutubeSearch(song, max_results=5).to_dict()
    return result

# 이름:주소 형태로 추출
def GetNameAndAdd(datas):
    result = {}
    for data in datas:
        url = f"https://www.youtube.com/watch?v={data['id']}"
        result[data['title']] =  url

    return result

# 이름만 추출
def GetName(datas):
    result = []
    for data in datas:
        result.append(data['title'])
    return result


def selectSong():
    song = input('부르고 싶은 곡을 입력해주세요\n') 

    if CheckInput(song) != "":
    	print(CheckInput(song))
    	time.sleep(3)
    	os.system('clear')
    	continue
    
    songList = SearchSong('TJ노래방 '+song)

    if len(songList) < 1:
    	print("존재하지 않는 곡입니다. 다시 입력해주세요.")
    	time.sleep(3)
    	os.system('clear')
    	continue

    videoNames = GetName(songList)

    for index, videoName in enumerate(videoNames):
        print(f"{index}: {videoName}")
    
    input('\n원하시는 영상을 선택해주세요: ')

    time.sleep(60)

# 메인 함수
currentMode = ''
while True:
    os.system('clear')
    print('1. 노래방 모드')
    print('2. 노래 녹음 모드')

    selectSong()
