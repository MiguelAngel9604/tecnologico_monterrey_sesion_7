# tecnologico_monterrey_sesion_7

## Configuración del Ambiente Virtual

### Crear el ambiente virtual

```powershell
python -m venv venv
```

O si tienes Python 3 específicamente:
```powershell
python3 -m venv venv
```

### Activar el ambiente virtual

#### En PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

Si obtienes un error de política de ejecución, ejecuta primero:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Alternativa en PowerShell:
```powershell
venv\Scripts\activate
```

#### En CMD (Símbolo del sistema):
```cmd
venv\Scripts\activate.bat
```

### Desactivar el ambiente virtual

```powershell
deactivate
```

### Comandos completos (ejemplo)

```powershell
# Crear el ambiente virtual
python -m venv venv

# Activar el ambiente virtual
.\venv\Scripts\Activate.ps1

# Instalar dependencias (si tienes requirements.txt)
pip install -r requirements.txt

# Verificar que estás en el ambiente virtual (debería mostrar la ruta del venv)
where python
```


### Ejecutar las pruebas específicas de `generar_usuario`

#### Prueba unitaria de `generar_usuario`:
```bash
pytest tests/unit/test_buenas_practicas.py::test_generar_usuario_parametrize -v
```

#### Prueba de integración de `generar_usuario`:
```bash
pytest tests/integration/test_integracion.py::test_generar_usuario_integracion -v
```

### Ejecutar ambas pruebas de `generar_usuario`:

```bash
pytest tests/unit/test_buenas_practicas.py::test_generar_usuario_parametrize tests/integration/test_integracion.py::test_generar_usuario_integracion -v
```

### Opciones útiles de pytest

```bash
# Ejecutar con salida detallada
pytest -v

# Ejecutar mostrando las salidas de print
pytest -s

# Ejecutar y detenerse en el primer error
pytest -x

# Ejecutar un archivo específico
pytest tests/unit/test_buenas_practicas.py

# Ejecutar una función de prueba específica
pytest tests/unit/test_buenas_practicas.py::test_generar_usuario_parametrize
```

## Flake8 - Linting y Verificación de Código

### ¿Qué es Flake8?

Flake8 es una herramienta que verifica tu código Python contra:
- **PEP 8** (guía de estilo de Python)
- **Errores de programación** (imports no usados, nombres indefinidos)
- **Complejidad ciclomática** (medida de complejidad del código)

### Estructura del Comando Flake8

```bash
flake8 [OPCIONES] [ARCHIVOS_O_DIRECTORIOS]
```

#### Componentes:

1. **`flake8`** - El comando principal
2. **`[OPCIONES]`** - Flags que modifican el comportamiento (ej: `--ignore`, `--max-line-length`)
3. **`[ARCHIVOS_O_DIRECTORIOS]`** - Qué archivos o carpetas analizar

### Opciones Comunes de Flake8

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `--ignore` | Ignora códigos de error específicos | `--ignore=E501,W292` |
| `--select` | Solo verifica códigos específicos | `--select=E9,F63` |
| `--exclude` | Excluye archivos/directorios del análisis | `--exclude=venv,migrations` |
| `--max-line-length` | Longitud máxima de línea permitida | `--max-line-length=100` |
| `--max-complexity` | Complejidad ciclomática máxima | `--max-complexity=10` |
| `--count` | Cuenta errores encontrados | `--count` |
| `--statistics` | Muestra estadísticas de errores | `--statistics` |
| `--show-source` | Muestra el código fuente del error | `--show-source` |
| `--exit-zero` | No falla aunque haya errores (solo reporta) | `--exit-zero` |

### Códigos de Error de Flake8

#### Categorías principales:

- **E**: Errores de estilo (PEP 8)
  - `E302`: Se esperan 2 líneas en blanco, se encontró 1
  - `E501`: Línea demasiado larga
  - `E402`: Módulo importado antes de otros imports

- **W**: Advertencias
  - `W292`: Falta salto de línea al final del archivo
  - `W503`: Línea antes de operador binario

- **F**: Errores de PyFlakes (lógica)
  - `F401`: Import no usado
  - `F403`: Import * usado
  - `F63`: Uso de `print` o `pdb`

- **C**: Complejidad ciclomática (requiere plugin)

### Ejemplos Prácticos

#### Ejemplo 1: Básico
```bash
flake8 app/
```
Analiza todos los archivos Python en `app/`

#### Ejemplo 2: Con límite de línea
```bash
flake8 --max-line-length=100 --ignore=E501 app/
```
- Límite de 100 caracteres por línea
- Ignora E501 (línea demasiado larga) para no duplicar errores

#### Ejemplo 3: Múltiples archivos específicos
```bash
flake8 archivo1.py archivo2.py archivo3.py
```
Analiza archivos específicos

#### Ejemplo 4: Solo errores críticos
```bash
flake8 --select=E9,F63,F7,F82 app/
```
Solo verifica errores de sintaxis y nombres indefinidos (errores críticos)

#### Ejemplo 5: Excluir directorios
```bash
flake8 --exclude=venv,__pycache__,migrations .
```
Analiza todo el proyecto excepto esos directorios

#### Ejemplo 6: Verificación suave (solo reporta, no falla)
```bash
flake8 --ignore=E1,E23,W503,F403,F401,E402,E501,E302 --exit-zero tests/
```
- Ignora muchos errores de estilo
- No falla el build (`--exit-zero`)
- Útil para tests donde el estilo es más flexible

### Uso en GitHub Actions

En el workflow `.github/workflows/ejemplo-flake8-pytest.yml`, flake8 se ejecuta en 3 pasos:

#### 1. Verificación suave de tests
```bash
flake8 --ignore=E1,E23,W503,F403,F401,E402,E501,E302 tests/unit/test_buenas_practicas.py tests/integration/test_integracion.py
```
- Ignora muchos errores de estilo en tests
- Verifica que no haya errores críticos
- Falla si encuentra errores no ignorados

#### 2. Verificación crítica en todo el proyecto
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```
- Solo verifica errores críticos (sintaxis, nombres indefinidos)
- Muestra el código fuente del error
- **Falla el build si encuentra estos errores**

#### 3. Estadísticas generales
```bash
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
- Reporta estadísticas de todos los errores
- No falla el build (`--exit-zero`)
- Útil para ver el estado general del código

### Estructura Visual del Comando

```
┌─────┐  ┌──────────────────────────────────────────────┐  ┌────────────────────────────────────┐
│     │  │                                              │  │                                    │
flake8  --ignore=E1,E23,W503,F403,F401,E402,E501,E302  tests/unit/test_buenas_practicas.py
│     │  │                                              │  │                                    │
│     │  └─ Opciones (flags)                           │  └─ Archivos a analizar             │
│     │                                                                                           │
└─ Comando
```

### Orden de Ejecución

1. Flake8 lee las opciones (`--ignore`, `--max-line-length`, etc.)
2. Flake8 identifica los archivos a analizar
3. Flake8 analiza cada archivo línea por línea
4. Flake8 reporta errores que no están en la lista de `--ignore`
5. Si hay errores no ignorados, flake8 termina con código de salida != 0 (falla)

### Instalación

```bash
pip install flake8
```

### Verificar Versión

```bash
flake8 --version
```

### Configuración con Archivo `.flake8` o `setup.cfg`

Puedes crear un archivo `.flake8` en la raíz del proyecto:

```ini
[flake8]
ignore = E501, W292
exclude = 
    .git,
    __pycache__,
    venv,
    env
max-line-length = 100
max-complexity = 10
```

Luego simplemente ejecuta:
```bash
flake8 .
```

Y usará automáticamente la configuración del archivo.