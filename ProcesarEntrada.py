from Sounds import Sound
from Dictionary import Dictionary
import time
class ProcesarEntrada:
    def procesarEntrada(self, entrada):
        myDictionary = Dictionary()
        sonido = Sound()
        
        for i in entrada.upper():
            if i == " ":
                time.sleep(1)
                continue
            clave = myDictionary.getDic(i)
            print(i," " + clave)
            
        for j in clave:
             if j == ".":
                sonido.short()
             else:
                sonido.long()
                time.sleep(0.5)
            