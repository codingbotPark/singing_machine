import __downloadMusic__
import os
from spleeter.separator import Separator
import time

outputPath = "musics"

# def execute():
def execute(link):
    print(link)
    print("음원 다운로드 중입니다...")
    videoInfo = __downloadMusic__.downloadMusic(link)

    print("음원 보컬과 MR 분리중입니다...")
    savedPath = splitFile(videoInfo)

    print("분리된 파일들의 위치를 변경하는 중입니다...")
    spreadSplitedFiles(savedPath)

# def splitFile():
def splitFile(videoInfo):
    videoTitle = videoInfo['videoTitle']
    videoChannel = videoInfo['videoChannel']

    separator = Separator('spleeter:2stems')

    # dirPath = '/home/codingbotpark/singing_supporter/musics/들리나요..._UC_pwIXKXNm5KGhdEVzmY60A'
    # path = '/home/codingbotpark/singing_supporter/musics/들리나요..._UC_pwIXKXNm5KGhdEVzmY60A/들리나요....mp3'
    dirPath = os.path.join(os.getcwd(),outputPath ,videoTitle+'_'+videoChannel)
    path = os.path.join(dirPath,videoTitle+'.mp3')
    separator.separate_to_file(path,dirPath)

    return os.path.join(dirPath,videoTitle)
    # return os.path.join(dirPath,'들리나요...')

# split된 파일들이 저장된 폴더를 music 하위 폴더에 그대로 저장
def spreadSplitedFiles(savedPath):
    savedFiles = os.listdir(savedPath)
    for filename in savedFiles:
        sourcePath = os.path.join(savedPath,filename)
        targetPath = os.path.join(savedPath,'../',filename)
        os.rename(sourcePath,targetPath)
    # 디렉토리 삭제
    os.rmdir(savedPath)


