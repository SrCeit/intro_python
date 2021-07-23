from datetime import date, datetime
from playsound import playsound

alarma = input("Introduce la hora a la que sonará la alarma (HH:MM:SS):\n ")

hora = alarma[0:2]
minutos = alarma[2:5]
segundos = alarma[6:8]
periodo = alarma[9:11]
print("Preparando alarma... ")
while True:
    ahora = datetime.now()
    actual_hora = ahora.strftime("%I")
    actual_minutos = ahora.strftime("%M")
    actual_segundos = ahora.strftime("%S")
    actual_periodo = ahora.strftime("%p")
    if(periodo == actual_periodo):
        if(hora == actual_hora):
            if(minutos == actual_minutos):
                if(segundos == actual_segundos):
                    print("Son las despiertate o'clock!")
                    playsound("audio.mp3")
                    break