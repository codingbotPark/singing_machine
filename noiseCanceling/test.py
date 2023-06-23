import numpy as np
import sounddevice as sd

# 노이즈 프로파일 초기화
noise_profile = None

# 노이즈 캔슬링 콜백 함수
def audio_callback(indata, frames, time, status):
    if status:
        print("Audio status:", status)

    # 노이즈 캔슬링 수행
    if noise_profile is not None:
        processed_audio = indata - noise_profile * np.mean(indata)
    else:
        processed_audio = indata

    # 출력
    sd.play(processed_audio)

# 노이즈 프로파일 업데이트 함수
def update_noise_profile(indata):
    global noise_profile
    if noise_profile is None:
        noise_profile = np.zeros_like(indata)
    else:
        noise_profile = noise_profile * 0.9 + np.abs(indata) * 0.1

# 오디오 스트림 열기
stream = sd.InputStream(callback=audio_callback)
stream.start()

# 노이즈 프로파일 업데이트를 위한 루프
while True:
    input()
    update_noise_profile(stream.read(stream.frames)[0])
