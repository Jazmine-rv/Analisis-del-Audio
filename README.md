# Modelos Y Clasificacion - Técnicas para el Análisis del Audio 

## Descripción

Este trabajo práctico consiste en analizar y procesar un archivo de audio (`AnalisisTextos.mp3`) usando herramientas como MediaInfo, ffmpeg y Python. Se realizan las siguientes tareas:

- Análisis del archivo original con MediaInfo.
- Muestreo (resampling) con ffmpeg para cambiar la frecuencia de muestreo y formato.
- Análisis del archivo modificado con MediaInfo.
- Procesamiento en Python para:
  - Mostrar vector de la señal y características (cantidad de muestras, frecuencia de muestreo, duración).
  - Graficar la forma de onda del audio.
  - Reproducir el audio original y modificado.
  - Modificar la frecuencia de muestreo para acelerar o ralentizar el audio.
  - Reducir la calidad del audio cambiando la profundidad de bits y analizar su efecto.

## Librerias usadas

   - Librerías Python: `soundfile`, `matplotlib`, `numpy`, `IPython`

---
## Archivos incluidos

- `AnalisisTextos.mp3`: archivo de audio original.
- `AnalisisTextos.txt`: Mediainfo del archivo de audio original
- `AnalisisTextos_rsampled.wav`: archivo de audio resampleado.
- `AnalisisTextos_rsampled.txt`: Mediainfo del archivo de audio resampleado.
- `AnalisisAudio.py`: Script para el análisis y procesamiento.
- `README.md`: Archivo con la descripción y guía.
