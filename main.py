import numpy as np
import wave
import matplotlib.pyplot as plt
f = wave.open(r"lantian.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data = wave_data*1.0/(max(abs(wave_data)))
fft_signal = np.fft.fft(wave_data)     # Голосовой сигнал БПФ-преобразование
fft_signal = abs(fft_signal)# Возьмите модуль преобразованного результата
plt.figure(figsize=(10,4))
time=np.arange(0,nframes)*framerate/nframes
plt.plot(time,fft_signal,c="g")
plt.grid()
plt.show()
