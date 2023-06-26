import pyaudio, wave
from pydub import AudioSegment
    
def main():
    mp3_path = "mr.mp3"  # 분석할 mp3 파일의 경로를 지정합니다.
    duration = 180


    # 마이크 설정
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = int(duration)
    WAVE_OUTPUT_FILENAME = "output.mp3"

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

    # 음원 파일 경로
    audio_file1 = "mr.mp3"
    audio_file2 = "output.mp3"

    # 음원 파일 로드
    sound1 = AudioSegment.from_file(audio_file1)
    sound2 = AudioSegment.from_file(audio_file2)

    # 음원 합치기
    mixed_sound = sound1.overlay(sound2)

    # 합쳐진 음원을 새 파일로 저장
    mixed_sound.export("sum_output.mp3", format="mp3")
