from ProcesarEntrada import ProcesarEntrada
from ObtenerEntrada import ObtenerEntrada

#TODO verificar el main
if __name__ == "__main__":
     entrada = ObtenerEntrada()
     procesar = ProcesarEntrada()
     procesar.procesarEntrada(entrada.getEntrada()) 
