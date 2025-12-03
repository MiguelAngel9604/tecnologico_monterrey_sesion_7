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

## GitHub Actions - Eventos Comunes

GitHub Actions puede ejecutarse en respuesta a muchos eventos. Aquí están los más comunes con ejemplos:

### 1. Push (Push a una rama)

Se ejecuta cuando haces push de código a una rama específica.

```yaml
on:
  push:
    branches: [ main, develop ]
    # Opcional: solo en archivos específicos
    paths:
      - 'app/**'
      - 'tests/**'
```

**Ejemplo de uso**: Ejecutar tests automáticamente cuando se hace push a `main`.

### 2. Pull Request

Se ejecuta cuando se crea, actualiza o cierra un pull request.

```yaml
on:
  pull_request:
    branches: [ main ]
    types: [ opened, synchronize, reopened, closed ]
```

**Ejemplo de uso**: Validar código antes de hacer merge a `main`.

### 3. Workflow Dispatch (Ejecución Manual)

Permite ejecutar el workflow manualmente desde la pestaña Actions de GitHub.

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production
```

**Ejemplo de uso**: Deploy manual a diferentes ambientes.

### 4. Schedule (Tareas Programadas)

Ejecuta el workflow en horarios específicos usando sintaxis cron.

```yaml
on:
  schedule:
    # Todos los días a las 2 AM UTC
    - cron: '0 2 * * *'
    # Cada lunes a las 9 AM UTC
    - cron: '0 9 * * 1'
    # Cada hora
    - cron: '0 * * * *'
```

**Sintaxis cron**: `minuto hora día-del-mes mes día-de-la-semana`

**Ejemplo de uso**: Ejecutar backups diarios o reportes semanales.

### 5. Release

Se ejecuta cuando se publica, crea o edita un release.

```yaml
on:
  release:
    types: [ published, created, edited ]
```

**Ejemplo de uso**: Deploy automático a producción cuando se publica un release.

### 6. Issues

Se ejecuta cuando se crea, cierra o etiqueta un issue.

```yaml
on:
  issues:
    types: [ opened, closed, labeled, reopened ]
```

**Ejemplo de uso**: Automatizar respuestas a issues o asignar etiquetas.

### 7. Issue Comment

Se ejecuta cuando se comenta en un issue o pull request.

```yaml
on:
  issue_comment:
    types: [ created ]
```

**Ejemplo de uso**: Ejecutar tests cuando alguien comenta `/test` en un PR.

### 8. Pull Request Review

Se ejecuta cuando se envía, edita o descarta una revisión de PR.

```yaml
on:
  pull_request_review:
    types: [ submitted, edited, dismissed ]
```

**Ejemplo de uso**: Notificar cuando un PR es aprobado.

### 9. Create (Crear rama/tag)

Se ejecuta cuando se crea una nueva rama o tag.

```yaml
on:
  create:
    branches: [ main ]
```

**Ejemplo de uso**: Inicializar configuración cuando se crea una nueva rama.

### 10. Delete (Eliminar rama/tag)

Se ejecuta cuando se elimina una rama o tag.

```yaml
on:
  delete:
    branches: [ feature/* ]
```

**Ejemplo de uso**: Limpiar recursos cuando se elimina una rama de feature.

### 11. Workflow Run (Workflow en cascada)

Se ejecuta cuando otro workflow termina.

```yaml
on:
  workflow_run:
    workflows: ["CI"]  # Nombre del workflow
    types: [ completed ]
    branches: [ main ]
```

**Ejemplo de uso**: Ejecutar deploy después de que pase el CI.

### 12. Push con Filtros Avanzados

Filtra por ramas, paths y más.

```yaml
on:
  push:
    branches: [ main, develop ]
    branches-ignore: [ 'main' ]  # Todas excepto main
    paths:                        # Solo archivos específicos
      - 'app/**'
      - 'tests/**'
      - '*.py'
    paths-ignore:                 # Ignorar archivos
      - 'docs/**'
      - '*.md'
    tags:
      - 'v*'                      # Solo tags que empiezan con 'v'
```

**Ejemplo de uso**: Ejecutar tests solo cuando cambian archivos de código, no documentación.

### Ejemplo Completo: Múltiples Eventos

```yaml
name: CI/CD Pipeline Completo

on:
  # Push a ramas principales
  push:
    branches: [ main, develop ]
    paths:
      - 'app/**'
      - 'tests/**'
  
  # Pull requests
  pull_request:
    branches: [ main ]
    types: [ opened, synchronize, reopened ]
  
  # Release
  release:
    types: [ published ]
  
  # Ejecución manual
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy environment'
        required: true
        default: 'staging'
  
  # Tarea programada (backup diario)
  schedule:
    - cron: '0 2 * * *'  # 2 AM UTC diario
  
  # Cuando se crea un issue
  issues:
    types: [ opened, labeled ]
```

### Tabla de Eventos Más Comunes

| Evento | Cuándo se dispara | Uso común |
|--------|-------------------|-----------|
| `push` | Push a rama | CI/CD, tests automáticos |
| `pull_request` | PR abierto/actualizado | Validación antes de merge |
| `workflow_dispatch` | Manual desde UI | Deploy manual, testing |
| `schedule` | Horario programado | Backups, reportes diarios |
| `release` | Release publicado | Deploy a producción |
| `issues` | Issue creado/cerrado | Automatización de issues |
| `workflow_run` | Otro workflow termina | Pipeline en cascada |
| `create` | Rama/tag creado | Inicialización automática |
| `delete` | Rama/tag eliminado | Limpieza de recursos |

### Sintaxis Cron - Referencia Rápida

```
┌───────────── minuto (0 - 59)
│ ┌─────────── hora (0 - 23)
│ │ ┌───────── día del mes (1 - 31)
│ │ │ ┌─────── mes (1 - 12)
│ │ │ │ ┌───── día de la semana (0 - 6) (0 = domingo)
│ │ │ │ │
* * * * *
```

**Ejemplos de cron:**
- `'0 2 * * *'` - Todos los días a las 2 AM
- `'0 9 * * 1'` - Todos los lunes a las 9 AM
- `'*/15 * * * *'` - Cada 15 minutos
- `'0 0 1 * *'` - Primer día de cada mes a medianoche
- `'0 * * * *'` - Cada hora
- `'*/30 * * * *'` - Cada 30 minutos