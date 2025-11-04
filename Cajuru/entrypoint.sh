#!/bin/sh
set -e

echo "Iniciando o script de inicializacao do banco de dados (init_db.py)..."
python init_db.py

echo "Iniciando o servidor web (Gunicorn) na porta 8449..."
exec gunicorn --bind 0.0.0.0:8449 "main:app"