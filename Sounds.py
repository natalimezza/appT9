#TODO verificar el sonido
from playsound import playsound
#playsound('short.mp3','long.mp3')
class Sound:
    def short(self):
        playsound('short.mp3')
        
    def long(self):
        playsound('long.mp3')