import pyaudio
import wave
from moviepy.editor import VideoFileClip
#from mutagen.mp3 import MP3

def get_mp3_duration(mp3_path):
    video_clip = VideoFileClip(mp3_path)
    duration = video_clip.duration
    video_clip.close()
    #audio = MP3(mp3_path)
    #duration = audio.info.length
    return duration
    
mp3_path = "queencard.mp3"  # 분석할 mp3 파일의 경로를 지정합니다.
#duration = get_mp3_duration(mp3_path)
duration = 10


# 마이크 설정
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = int(duration)
WAVE_OUTPUT_FILENAME = "output1.mp3"

audio = pyaudio.PyAudio()

# 마이크에서 오디오 스트림 열기
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("녹음 시작...")

frames = []

# 오디오 스트림 읽기
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("녹음 완료.")

# 오디오 스트림 닫기
stream.stop_stream()
stream.close()
audio.terminate()

# 녹음된 오디오 저장
wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(RATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()
