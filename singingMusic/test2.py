from multiprocessing import Process
import pyaudio
import wave
import numpy as np

# 음악 파일 경로
music_file = "/home/codingbotpark/singing_supporter/musics/들리나요..._UC_pwIXKXNm5KGhdEVzmY60A/accompaniment.wav"

# 오디오 설정
chunk = 1024  # 버퍼 크기
format = pyaudio.paInt16  # 샘플 형식
channels = 2  # 채널 수
rate = 44100  # 샘플링 레이트

# 음악 재생 함수
def play_music():
    wf = wave.open(music_file, 'rb')

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    output=True)

    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()

# 마이크로 입력 함수
def mic_input():

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    output_stream = p.open(format=format,
                           channels=channels,
                           rate=rate,
                           output=True)

    while True:
        data = stream.read(chunk)
        audio = np.frombuffer(data, dtype=np.int16)
        amplitude = np.max(np.abs(audio))
        print("마이크 진폭:", amplitude)
        output_stream.write(data)
        # 마이크로 입력 데이터 처리 (원하는 동작 수행)

playProcess =Process(target=play_music)
mic_inputProccess= Process(target=mic_input)

mic_inputProccess.start(); 
playProcess.start(); 

playProcess.join()
mic_inputProccess.join()