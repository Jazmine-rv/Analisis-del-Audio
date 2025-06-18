# %%
import soundfile as sf
import matplotlib.pyplot as plt
from IPython.display import Audio
import numpy as np


# Leer el archivo de audio, fuerzo la ruta
audio, sr = sf.read(r"C:\ffmpeg\AnalisisTextos_rsampled.wav")

# Informacion básica
print('Vector de la señal segmentada:', audio)  
print('Cantidad de elementos:', len(audio))     
print('Frecuencia de muestreo:', sr)            
print('Duración:', len(audio) / sr, "segundos") 

# Grafico de la onda
plt.plot(audio)
plt.title("Forma de onda del audio")
plt.xlabel("Muestras")
plt.ylabel("Amplitud")
plt.show()

Audio(audio, rate=sr)

# si lo quiero reproducir mas rapido
# Audio(audio, rate=sr*2)

# si lo quiero reproducir mas lento
# Audio(audio, rate=sr*0.3)

# Escalar la amplitud al rango [-128, 127] y convertir a enteros de 8 bits
# audio_8bit = (audio * 2**7).astype(np.int8)

# Reproducir el audio con menor resolución
# print("Audio con profundidad de 8 bits:")
# Audio(audio_8bit, rate=sr)


