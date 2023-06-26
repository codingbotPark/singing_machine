from multiprocessing import Process
import pyaudio
import wave
import numpy as np

# 음악 파일 경로
music_file = "/home/codingbotpark/singing_supporter/musics/들리나요..._UC_pwIXKXNm5KGhdEVzmY60A/accompaniment.wav"
vocal_file = "/home/codingbotpark/singing_supporter/musics/들리나요..._UC_pwIXKXNm5KGhdEVzmY60A/vocals.wav"

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
    wf = wave.open(vocal_file, 'rb')

    p = pyaudio.PyAudio()
    vocal_stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    output=True,
                    frames_per_buffer=chunk)

    mic_stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True)

    vocalData = wf.readframes(chunk)
    while vocalData:
        micData = mic_stream.read(chunk)
        audio = np.frombuffer(micData,dtype=np.int16)
        amplitude = np.max(np.max(np.abs(audio)))
        print("마이크 진폭:", amplitude)

        # 3000 이상일 땐 말하는것
        if (amplitude > 3000):
            vocal_stream.write(micData)
        else:
            vocal_stream.write(vocalData)

        vocalData = wf.readframes(chunk)

    vocal_stream.stop_stream()
    vocal_stream.close()
    mic_stream.stop_stream()
    mic_stream.close()
    p.terminate()


playProcess =Process(target=play_music)
mic_inputProccess= Process(target=mic_input)

mic_inputProccess.start(); 
playProcess.start(); 

playProcess.join()
mic_inputProccess.join()