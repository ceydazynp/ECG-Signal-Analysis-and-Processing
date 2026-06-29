import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_ecg_data(file_path):
    """Veri setinden EKG sinyalini okur."""
    data = pd.read_csv(file_path)

   
    time = data["Zaman"].values
    signal = data["Sinyal"].values

    return time, signal


def plot_raw_ecg(time, signal):
    """Ham EKG sinyalini ekrana çizer."""
    plt.figure(figsize=(10, 4))
    plt.plot(
        time,
        signal,
        label="Ham EKG Sinyali",
        color="red",
        linewidth=2,
        marker="o",
    )
    plt.title("Ham EKG Sinyali Görselleştirme (1. Gün)")
    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik (mV)")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    
    FILE_PATH = "cu01.csv"

    try:
        time, signal = load_ecg_data(FILE_PATH)
        plot_raw_ecg(time, signal)
        print("1. Gün Başarıyla Tamamlandı: Veri okundu ve çizdirildi!")
    except Exception as e:
        print(f"Hata oluştu: {e}")
