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

## Alternativa: Usar Conda (Recomendado si tienes Anaconda/Miniconda)

Si tienes problemas con SSL usando `venv` (especialmente con Anaconda), puedes usar conda:

### Crear el ambiente con conda

```powershell
conda create -n tecnologico_monterrey python=3.8 -y
```

### Activar el ambiente conda

```powershell
conda activate tecnologico_monterrey
```

### Instalar dependencias

```powershell
pip install pytest
# O si tienes requirements.txt
pip install -r requirements.txt
```

### Desactivar el ambiente conda

```powershell
conda deactivate
```

### Comandos completos con conda (ejemplo)

```powershell
# Crear el ambiente conda
conda create -n tecnologico_monterrey python=3.8 -y

# Activar el ambiente conda
conda activate tecnologico_monterrey

# Instalar dependencias
pip install -r requirements.txt

# Verificar que estás en el ambiente conda
conda info --envs
```

## Solución de problemas SSL

Si encuentras errores de SSL al instalar paquetes con pip:

1. **Usa conda en lugar de venv** (recomendado con Anaconda)
2. **O reinstala/actualiza Anaconda** para corregir el módulo SSL
3. **O usa un Python de python.org** en lugar de Anaconda para crear el venv

## Ejecutar Tests (WSL/Linux)

### Activar el ambiente virtual en WSL

```bash
source env/bin/activate
```

### Ejecutar todas las pruebas

```bash
pytest
```

### Ejecutar solo las pruebas unitarias

```bash
pytest tests/unit/
```

### Ejecutar solo las pruebas de integración

```bash
pytest tests/integration/
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