import pytest

from app.funciones import procesar_nombre
from app.funciones import procesar_apellido_paterno
from app.funciones import procesar_apellido_materno
from app.funciones import generar_usuario


def concatenar_nombre_completo(nombre, ap, am):
    return nombre + " " + ap + " " + am


def obtener_datos_test_integracion():
    return [
        ("carlos", "LOPEZ", "meJIa", "Carlos Lopez Mejia"),
        ("ivan", "huERTA", "CoroNA", "Ivan Huerta Corona"),
    ]


@pytest.mark.parametrize(
    "nombre, ap, am, esperado", obtener_datos_test_integracion()
)
def test_divide_parametrize(nombre, ap, am, esperado):
    assert (
        procesar_nombre(nombre)
        + " "
        + procesar_apellido_paterno(ap)
        + " "
        + procesar_apellido_materno(am)
        == esperado
    )


def obtener_datos_test_generar_usuario_integracion():
    return [
        ("carlos", "LOPEZ", "meJIa", "carlos.lopez.mejia"),
        ("ivan", "huERTA", "CoroNA", "ivan.huerta.corona"),
        ("MiGuel", "EspiNOZA", "SILVa", "miguel.espinoza.silva"),
    ]


@pytest.mark.parametrize(
    "nombre, ap, am, esperado",
    obtener_datos_test_generar_usuario_integracion(),
)
def test_generar_usuario_integracion(nombre, ap, am, esperado):
    # Prueba de integración: verifica que generar_usuario
    # integra correctamente todas las funciones de procesamiento
    resultado = generar_usuario(nombre, ap, am)
    assert resultado == esperado
    # Verifica que el formato es correcto (todo en minúsculas con puntos)
    assert resultado.islower()
    assert resultado.count(".") == 2
    # Verifica que los componentes procesados están correctos
    partes = resultado.split(".")
    assert partes[0] == procesar_nombre(nombre).lower()
    assert partes[1] == procesar_apellido_paterno(ap).lower()
    assert partes[2] == procesar_apellido_materno(am).lower()
