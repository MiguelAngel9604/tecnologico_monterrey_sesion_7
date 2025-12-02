from app.funciones import procesar_nombre


# Pruebas para el nombre
def test_procesar_nombre():
    assert procesar_nombre("carlos") == "Carlos"


def test_procesar_nombre_2():
    assert procesar_nombre("MiGuel") == "Miguel"


def test_procesar_nombre_3():
    assert procesar_nombre("iVAN") == "Ivan"
