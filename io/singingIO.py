import time
import os
from youtube_search import YoutubeSearch
import splitingMusic
import re
import singingMusic

outputPath = "musics"

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


def addSong():

    while True:
        song = input('저장하고 싶은 곡을 입력해주세요(나가기 = exit) >>> ') 

        if (song == "exit"): break
        elif (song == ""):
            print("다시입력해주세요")
            continue

    
        # songList = SearchSong('TJ노래방 '+song)
        songList = SearchSong(song)

        if len(songList) < 1:
            print("존재하지 않는 곡입니다. 다시 입력해주세요.")
            continue

        videoNames = GetName(songList)
        for index, videoName in enumerate(videoNames):
            print(f"{index}: {videoName}")
    
        selectedVideo = input('원하시는 영상을 선택해주세요 >>> ')
        songAddrs = GetNameAndAdd(songList)
        print(songAddrs[videoNames[int(selectedVideo)]])
        splitingMusic.execute(songAddrs[videoNames[int(selectedVideo)]])
        break   

def singSong():
    musicsPath = os.path.join(os.getcwd(),outputPath)
    musics = os.listdir(musicsPath)
    
    def findSong(puttedString):
        resultArr = []
        for music in musics:
            if re.search(r'\b' + re.escape(puttedString.lower()) + r'\b',''.join(music.split('_')[:-1]).lower() ):
                resultArr.append(music)
        
        return resultArr

    while True:
        showingIdx = 1
        # 저장된 or 유튜브 노래방 영상인지 기준이 되는 숫자, 노래방 영상의 시작번째 인덱스가 저장된다
        standIndex = 0
        song = input('부르고 싶은 곡을 입력해주세요 >>> ')
        similarWithSavedSongs = findSong(song)

        # 만약 저장된 노래 중 비슷한 노래가 있다면
        if similarWithSavedSongs:
            print("---저장된 비슷한 노래입니다(노래 서포팅이 적용됩니다)---")
            for i in similarWithSavedSongs:
                print(f"{showingIdx}. {''.join(i.split('_')[0])}")
                showingIdx+=1
            standIndex = showingIdx
        else:
            print("저장된 노래 중 해당 노래를 찾을 수 없었습니다")
        
        print('\n---유튜브 tj노래방으로 검색한 결과입니다---')
        tjSongList = SearchSong('TJ노래방' + song)

        if tjSongList:
            videoNames = GetName(tjSongList)
            for videoName in videoNames:
                print(f"{showingIdx}. {videoName}")
                showingIdx+=1
        else:
            print("존재하지 않는 곡입니다. 다시 입력해주세요")
            continue

        while True:
            selectedSong = input("\n원하시는 음원을 선택해주세요 >>> ")

            try:
                selectedNumber = int(selectedSong)
                if selectedNumber > 0 and selectedNumber < showingIdx:
                    # 저장된 파일 선택
                    if selectedNumber < standIndex:
                        audioPath = os.path.join(os.getcwd(),outputPath,similarWithSavedSongs[selectedNumber - 1])
                        # singingMusic.execute(
                        #     os.path.join(audioPath,'accompaniment.wav'),
                        #     os.path.join(audioPath,'vocals.wav')
                        # )

                        playMusicThread = singingMusic.PlayMusic(os.path.join(audioPath,'accompaniment.wav'))
                        micInputThread = singingMusic.MicInput(os.path.join(audioPath,'vocals.wav'))

                        micInputThread.start(); 
                        playMusicThread.start(); 

                        playMusicThread.join()
                        micInputThread.join()

                    else:
                        print("tj 노래방 영상 선택")
                else:
                    print("\n유효한 숫자를 입력해주세요\n")
                    continue
                    
                break
            except ValueError:
                print("\n숫자를 입력해주세요\n")
                continue
        break


# -----

def checkInputs(rightCases,value):
    return value in rightCases

# 메인 함수
def execute():
    currentMode = ''
    while True:
        os.system('clear')
        print('1. 노래  부르기')
        print('2. 노래 추가')
        print('3. 노래 녹음하기')
        print('4. 종료')

        category = input('>>> ')

        # 없다면
        if (not checkInputs(['1','2','3','4'],category)):
            continue
        os.system('clear')
        
        if (category == '1'):
            singSong()
        elif (category == '2'):
            addSong()
        elif (category == '3'):
            print(3)
        else:
            exit()

        # selectSong()
