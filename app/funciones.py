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
