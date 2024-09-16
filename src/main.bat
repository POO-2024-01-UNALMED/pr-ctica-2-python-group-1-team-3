@echo off

REM Verificar e instalar las dependencias
pip install -r requirements.txt

REM Compilar el script para verificar errores
python -m Principal.py
if %ERRORLEVEL% neq 0 (
    echo Error de compilación. Revisa el script.
    pause
    exit /b %ERRORLEVEL%
)

REM Ejecutar el script Python
python Principal.py

pause
