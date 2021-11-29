# 사용한 모듈
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import librosa as lr

# 불러올 파일명
audio_file = './result_1.wav'

# 파일에서 진폭과 샘플링 레이트를 불러온다
# y = 진폭 / sr = 샘플링 레이트
y, sr = lr.load(audio_file)

# t = 시간
t = np.arange(0, len(y)) / sr

# 그래프로 표현
fig, ax = plt.subplots()
ax.plot(t, y)
ax.set(xlabel='time(s)', ylabel='amplitude')
plt.show()