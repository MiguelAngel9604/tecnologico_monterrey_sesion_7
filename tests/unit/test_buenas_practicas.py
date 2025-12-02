# import sys

# sys.path.append("app/")
# sys.path.append("../")

# print(sys.path)

import pytest

from app.funciones import procesar_nombre
from app.funciones import procesar_apellido_paterno
from app.funciones import procesar_apellido_materno
from app.funciones import generar_usuario


# Pruebas para el nombre
def obtener_datos_test_nombre():
    return [("carlos", "Carlos"), ("MiGuel", "Miguel"), ("iVAN", "Ivan")]


@pytest.mark.parametrize("nombre, esperado", obtener_datos_test_nombre())
def test_nombre_parametrize(nombre, esperado):
    assert procesar_nombre(nombre) == esperado


# Pruebas para el apellido paterno
def obtener_datos_test_ap():
    return [("LOPEZ", "Lopez"), ("EspiNOZA", "Espinoza"), ("sancHEz", "Sanchez")]


@pytest.mark.parametrize("ap, esperado", obtener_datos_test_ap())
def test_ap_parametrize(ap, esperado):
    assert procesar_apellido_paterno(ap) == esperado


# Pruebas para el apellido materno
def obtener_datos_test_am():
    return [("ferrer", "Ferrer"), ("SILVa", "Silva"), ("PalafoX", "Palafox")]


@pytest.mark.parametrize("am, esperado", obtener_datos_test_am())
def test_am_parametrize(am, esperado):
    assert procesar_apellido_materno(am) == esperado


# Pruebas para generar_usuario
def obtener_datos_test_generar_usuario():
    return [
        ("carlos", "LOPEZ", "meJIa", "carlos.lopez.mejia"),
        ("MiGuel", "EspiNOZA", "SILVa", "miguel.espinoza.silva"),
        ("iVAN", "sancHEz", "PalafoX", "ivan.sanchez.palafox"),
    ]


@pytest.mark.parametrize(
    "nombre, ap, am, esperado", obtener_datos_test_generar_usuario()
)
def test_generar_usuario_parametrize(nombre, ap, am, esperado):
    assert generar_usuario(nombre, ap, am) == esperado
