def procesar_nombre(nombre):
    if isinstance(nombre, str):
        return nombre.capitalize()
    return "Error nombre"


def procesar_apellido_paterno(apellido_p):
    if isinstance(apellido_p, str):
        return apellido_p.capitalize()
    return "Error Apellido Paterno"


def procesar_apellido_materno(apellido_m):
    if isinstance(apellido_m, str):
        return apellido_m.capitalize()
    return "Error Apellido Materno"


def generar_usuario(nombre, apellido_paterno, apellido_materno):
    nombre_procesado = procesar_nombre(nombre).lower()
    ap_paterno_procesado = procesar_apellido_paterno(apellido_paterno).lower()
    ap_materno_procesado = procesar_apellido_materno(apellido_materno).lower()
    return f"{nombre_procesado}.{ap_paterno_procesado}.{ap_materno_procesado}"