from pytube import YouTube
import os

# outputPath = config.outputPath

outputPath = "musics"


def downloadMusic(link):

    yt = YouTube(link)
    videoTitle = yt.title
    videoChannel = yt.channel_id
    print(videoTitle,videoChannel)

    makeMusicsDir()

    path = os.path.join(outputPath,videoTitle+'_'+videoChannel)

    yt.streams.filter(only_audio=True).first().download(output_path=path,filename=f'{videoTitle}.mp3')
    return yt

def downloadVideo(link):


    yt = YouTube(link)
    videoTitle = yt.title
    videoChannel = yt.channel_id

    makeMusicsDir()
    path = os.path.join(outputPath,videoTitle+'_'+videoChannel)

    yt.streams.get_highest_resolution().download(output_path=path,filename=f'{videoTitle}.mp4')
    return yt

def makeMusicsDir():
    os.makedirs(outputPath,exist_ok=True)
