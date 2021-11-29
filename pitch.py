import librosa
from librosa.util.utils import normalize
import numpy as np
import wave
import pyaudio
import scipy.signal as signal

CHUNK = 1024
WAVE_INPUT_FILENAME = 'result_1.wav'
CHANNELS = 2
FORMAT = pyaudio.paInt16

# 오디오 파일 저장
def audio_save(name, data, rate):
    p = pyaudio.PyAudio()
    WAVE_OUTPUT_FILENAME = name + '.wav'
    RATE = rate
    frames = data

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# 오디오 파일 불러오기
a, sr = librosa.load("result_1.wav")

# #normalize_function (구현 안됨)
# min_level_db = -100
# def _normalize(S):
#     return np.clip((S-min_level_db)/(-min_level_db), 0, 1)

# amplitude = np.abs(librosa.stft(a, n_fft=1024, hop_length=512, win_length = 1024, window=signal.hann))
# mag_db = librosa.amplitude_to_db(amplitude)
# mag_n = _normalize(mag_db)

# 높낮이 변조
s3_a = librosa.effects.pitch_shift(a, sr, n_steps=3)

# 오디오 파일 저장
audio_save('result_2', s3_a, 22050)