from gtts import gTTS
from playsound import playsound

audio = "speech.mp3"

language = "es"

texto = input("Introduce el texto a convertir en audio: ")

sp = gTTS(text = texto, lang = language, slow = False)

sp.save(audio)

playsound(audio)
