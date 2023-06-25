import time
import os
from youtube_search import YoutubeSearch
import splitingMusic

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

    while True:
        song = input('부르고 싶은 곡을 입력해주세요(나가기 = exit) >>> ') 

        if (song == "exit"): break
        elif (song == ""):
            print("다시입력해주세요")
            continue

    
        songList = SearchSong('TJ노래방 '+song)

        if len(songList) < 1:
            print("존재하지 않는 곡입니다. 다시 입력해주세요.")
            continue

        videoNames = GetName(songList)
        for index, videoName in enumerate(videoNames):
            print(f"{index}: {videoName}")
    
        selectedVideo = input('원하시는 영상을 선택해주세요 >>> ')
        value = GetNameAndAdd(songList)

        splitingMusic(value[videoNames[selectedVideo]])

        break
        



# -----

def checkInputs(rightCases,value):
    return value in rightCases

# 메인 함수
def execute():
    currentMode = ''
    while True:
        os.system('clear')
        print('1. 노래방 부르기')
        print('2. 노래 추가')
        print('3. 노래 녹음하기')
        print('4. 종료')

        category = input('>>> ')

        # 없다면
        if (not checkInputs(['1','2','3','4'],category)):
            continue
        os.system('clear')
        
        if (category == '1'):
            print(1)
        elif (category == '2'):
            selectSong()
        elif (category == '3'):
            print(3)
        else:
            exit()

        # selectSong()
