#!/bin/bash

# ┌────────────────────────────────────────┐
# │ Script Bash para entorno virtual       │
# └────────────────────────────────────────┘

# Colores para mensajes
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
GREEN='\033[1;32m'
RED='\033[1;31m'
NC='\033[0m' # Sin color

# Verificar si el entorno virtual ya existe
if [ -d "./venv" ]; then
    echo -e "${YELLOW}El entorno virtual 'venv' ya existe.${NC}"
else
    echo -e "${BLUE}Creando entorno virtual 'venv'...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}Entorno virtual creado.${NC}"
fi

# Activar el entorno virtual
echo -e "${BLUE}Activando entorno virtual...${NC}"
source ./venv/bin/activate

# Verificar si requirements.txt existe
if [ -f "./requirements.txt" ]; then
    echo -e "${BLUE}Instalando dependencias desde requirements.txt...${NC}"
    pip install -r requirements.txt
    echo -e "${GREEN}Dependencias instaladas correctamente.${NC}"
else
    echo -e "${RED}No se encontró 'requirements.txt'. Por favor crea uno antes de continuar.${NC}"
fi

# Confirmar paquetes instalados
echo -e "\n${BLUE}Paquetes instalados:${NC}"
pip list

echo -e "\n${GREEN}Entorno listo para trabajar. Puedes comenzar tus ejercicios.${NC}"
