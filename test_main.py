from ProcesarEntrada import ProcesarEntrada
from ObtenerEntrada import ObtenerEntrada
import pytest
import ProcesarEntrada
import ObtenerEntrada

@pytest.mark.parametrize("input_a,expected",
   [ 
   ("a",2)
   ]
   ) 
def test_in(input_a, expected):
   assert ObtenerEntrada(input_a) == expected
       
          
def test_entrada():
   assert ProcesarEntrada("a") == 2

