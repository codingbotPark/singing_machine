from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

# 음악 파일 경로
audio_file = "/home/codingbotpark/singing_supporter/splitingMusic/musics/들리나요..._UC_pwIXKXNm5KGhdEVzmY60A/vocals.wav"

# 음악 파일을 AudioSegment 객체로 로드
audio = AudioSegment.from_file(audio_file)

chunks = split_on_silence(audio, min_silence_len=1000, silence_thresh=-30)

# 음성 인식을 위한 Recognizer 객체 생성
recognizer = sr.Recognizer()

# 추출한 가사를 저장할 변수
lyrics = ""

# 각 청크에서 가사 추출
for i,chunk in enumerate(chunks):
    # 청크를 WAV 파일로 저장
    chunk.export(f"temp{i}.wav", format="wav")

    # WAV 파일을 읽어서 음성 인식 수행
    with sr.AudioFile(f"temp{i}.wav") as source:
        audio = recognizer.record(source)
        try:
            # 음성을 텍스트로 변환
            text = recognizer.recognize_google(audio, language="ko-KR")
            # 추출한 텍스트를 가사에 추가
            lyrics += text + " "
        except sr.UnknownValueError:
            pass

# 가사 출력
print(lyrics)