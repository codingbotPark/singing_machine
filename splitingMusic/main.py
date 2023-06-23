import __downloadMusic__
import os
from spleeter.separator import Separator

# outputPath = config.outputPath
outputPath = "musics"


def execute(link):
    # videoInfo = __downloadMusic__.downloadVideo(link)
    videoInfo = __downloadMusic__.downloadMusic(link)
    savedPath = splitFile(videoInfo)
    spreadSplitedFiles()

def splitFile(videoInfo):
    videoTitle = videoInfo.title
    videoChannel = videoInfo.channel_id

    separator = Separator('spleeter:2stems')

    dirPath = os.path.join(os.getcwd(),outputPath ,videoTitle+'_'+videoChannel)
    path = os.path.join(dirPath,videoTitle+'.mp3')
    separator.separate_to_file(path,dirPath)

    return os.path.join(dirPath,videoTitle)

# split된 파일들이 저장된 폴더를 music 하위 폴더에 그대로 저장
def spreadSplitedFiles(splitedPath)
    print(5)