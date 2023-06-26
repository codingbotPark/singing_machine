import pyaudio


chunk = 1024
format = pyaudio.paInt16
channels = 2
rate = 44100

# 음악 실행
def play_music():

    p = pyaudio.PyAudio()
    stream = p.open(
        format=format,
        channels=channels,
        rate=rate,
        output=True
    )
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

    stream.start_stream()

    while True:
        data = stream.read(chunk)
        # 마이크로 입력 데이터 처리 (원하는 동작 수행)

    stream.stop_stream()
    stream.close()
    p.terminate()

# 음악 재생 시작
play_music()