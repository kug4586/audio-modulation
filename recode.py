# 사용한 모듈
import pyaudio
import wave

CHUNK = 1024 # 양자화로 표현된 값
FORMAT = pyaudio.paInt16 # 비트 수
CHANNELS = 2 # 통신 채널
RATE = 44100 # 샘플링 속도
RECORD_SECONDS = 5  # 녹음 시간
WAVE_OUTPUT_FILENAME = "result_1.wav" # 파일 이름

# 객체 생성
p = pyaudio.PyAudio()

# 녹음 셋팅
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True, # 입력(녹음) 상태
                frames_per_buffer=CHUNK)

print("* recording")

# 녹음 시작
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

# 녹음 종료
stream.stop_stream()
stream.close()
p.terminate()

# 파일 저장하기
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()