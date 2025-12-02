import pytest

from app.funciones import procesar_nombre


@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_calcular_curp():
    pass


@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_calcular_rfc():
    pass


#   xfail
@pytest.mark.xfail
def test_nombre_falla():
    assert procesar_nombre(12) == "Doce"


#   Escribir una marca personal
@pytest.mark.mi_marca
def test_mi_marca():
    assert procesar_nombre("jorgE") == "Jorge"
