import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# 1. ADIM: Test için temiz bir sinyal ve üzerine gürültü üretiyoruz
fs = 360  # Örnekleme frekansı
t = np.linspace(0, 2, 2 * fs, endpoint=False)  # 2 saniyelik bir alan

# Yapay bir EKG dalgası benzetimi (Temiz sinyal)
clean_signal = np.sin(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 3 * t)

# Sinyale yüksek frekanslı gürültü (kas titremesi gibi) ekliyoruz
noise = 0.3 * np.sin(2 * np.pi * 60 * t) + 0.1 * np.random.normal(size=len(t))
raw_signal = clean_signal + noise

# 2. ADIM: Alçak Geçiren (Low-pass) Filtre Fonksiyonu
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# 3. ADIM: Filtreyi Uygulama (40 Hz üzerini tıraşla)
cutoff = 40.0
filtered_signal = butter_lowpass_filter(raw_signal, cutoff, fs, order=4)

# 4. ADIM: Grafik Çizdirme
plt.figure(figsize=(12, 6))

# Üst Grafik: Gürültülü Ham Sinyal
plt.subplot(2, 1, 1)
plt.plot(raw_signal, color='red', label='Ham Gürültülü Sinyal')
plt.title('EKG Filtreleme Öncesi ve Sonrası (Yapay Test Sinyali)')
plt.ylabel('Genlik')
plt.legend()
plt.grid(True)

# Alt Grafik: Filtrelenmiş Temiz Sinyal
plt.subplot(2, 1, 2)
plt.plot(filtered_signal, color='green', label='Filtrelenmiş Temiz Sinyal')
plt.xlabel('Örnek Sayısı')
plt.ylabel('Genlik')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()