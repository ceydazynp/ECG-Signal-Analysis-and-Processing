import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks
veri = pd.read_csv('cu01.csv')
print("Veri Setinin İlk Satırları:")
print(veri.head())
ekg_sinyali = veri['Sinyal'].values

def butter_lowpass_filter(data, cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y
fs = 100      
cutoff = 15    
temiz_sinyal = butter_lowpass_filter(ekg_sinyali, cutoff, fs)
# Sinyalimiz çok kısa olduğu için mesafeyi (distance) ve yükseklik (height) sınırını düşürüyoruz:
pikler, _ = find_peaks(temiz_sinyal, distance=5, height=0.2)

plt.figure(figsize=(12, 6))

plt.plot(ekg_sinyali, label='Orijinal Gürültülü Sinyal', color='lightgray', alpha=0.7)

plt.plot(temiz_sinyal, label='Filtrelenmiş Temiz Sinyal', color='blue', linewidth=1.5)

plt.plot(pikler, temiz_sinyal[pikler], "x", label='Tespit Edilen R-Pikleri (Kalp Atışları)', color='red', markersize=10, mew=2)

plt.title('Gerçek EKG Sinyali Üzerinde R-Piki Tespiti (Day 3)', fontsize=14)
plt.xlabel('Örnek Sayısı (Sample Index)', fontsize=12)
plt.ylabel('Genlik (Amplitude)', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()