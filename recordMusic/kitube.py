from pytube import YouTube
import moviepy.editor as mp

# YouTube 동영상 링크 설정
youtube_link = input("Enter a youtube video's URL:\n")

# YouTube 동영상 다운로드
yt = YouTube(youtube_link)
yt.streams.filter(only_audio=True).first().download()

# 다운로드한 동영상 파일명 설정
video_file = yt.streams.filter(only_audio=True).first().default_filename

# 다운로드한 동영상 파일을 MP3로 변환
#mp3_file = video_file.split(".")[0] + ".mp3"
mp3_file = "mr.mp3"
clip = mp.AudioFileClip(video_file)
clip.write_audiofile(mp3_file)

# 변환한 MP3 파일 저장 완료
print("MP3 파일 저장 완료:", mp3_file)
