import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage.morphology import distance_transform_bf
plt.style.use('seaborn-white')

import librosa
import librosa.display

WAVE_INPUT_FILENAME = 'result_2.wav'

# 파일에서 진폭과 샘플링 레이트를 불러온다
# wav = 진폭 / sr = 샘플링 레이트
wav, sr = librosa.load(WAVE_INPUT_FILENAME)
print('진폭 :', wav)
print('샘플링 레이트 :', sr)

# 파형 그리기
fig = plt.figure(figsize=(14,5))
librosa.display.waveplot(wav, sr=sr)
plt.ylabel('Amplitude')
plt.show()

# FFT(Fast Fourier Transform, 고속 푸리에 변환)
fft = np.fft.fft(wav)

magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_magnitude = magnitude[:int(len(magnitude)/2)]
left_frequency = frequency[:int(len(frequency)/2)]

print(fft.shape)
print(frequency.shape)
print(left_frequency.shape)

fig = plt.figure(figsize=(14,5))
plt.plot(left_frequency, left_magnitude)
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.show()

# STFT(Short Time Fourier Transform, 단시간 푸리에 변환)
n_fft = 2048
hop_length = 512

stft = librosa.stft(wav, n_fft=n_fft, hop_length=hop_length)
spectogram = np.abs(stft)
print('스펙트럼 :', spectogram)

# Spectogram
fig = plt.figure(figsize=(14,5))
librosa.display.specshow(spectogram, sr=sr, hop_length=hop_length)
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.plasma()
plt.show()

# Log-spectogram
log_spectogram = librosa.amplitude_to_db(spectogram)

fig = plt.figure(figsize=(14,5))
librosa.display.specshow(log_spectogram, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar(format='%+2.0f dB')
plt.show()

# MFCC
MFCCs = librosa.feature.mfcc(
    wav, sr=22050,
    n_fft=n_fft, hop_length=hop_length,
    n_mfcc=13
)
print('MFCCs 모양 :', MFCCs.shape)
print('MFCCs\n', MFCCs)

fig = plt.figure(figsize=(14,5))
librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length, x_axis='time')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.colorbar(format='%+2.0f dB')
plt.show()