# ┌────────────────────────────────────────┐
# │ Script PowerShell para entorno virtual │
# └────────────────────────────────────────┘

# Verificar si el entorno virtual ya existe
if (Test-Path ".\venv") {
    Write-Host "El entorno virtual 'venv' ya existe." -ForegroundColor Yellow
}
else {
    Write-Host "Creando entorno virtual 'venv'..." -ForegroundColor Blue
    py -m venv venv
    Write-Host "Entorno virtual creado." -ForegroundColor Green
}

# Activar el entorno virtual
Write-Host "Activando entorno virtual..." -ForegroundColor Blue
& .\venv\Scripts\Activate.ps1

# Verificar si requirements.txt existe
if (Test-Path ".\requirements.txt") {
    Write-Host "Instalando dependencias desde requirements.txt..." -ForegroundColor Blue
    pip install -r requirements.txt
    Write-Host "Dependencias instaladas correctamente." -ForegroundColor Green
}
else {
    Write-Host "No se encontró 'requirements.txt'. Por favor crea uno antes de continuar." -ForegroundColor Red
}

# Confirmar paquetes instalados
Write-Host "`nPaquetes instalados:" -ForegroundColor Blue
pip list

Write-Host "`nEntorno listo para trabajar. Puedes comenzar tus ejercicios." -ForegroundColor Green
