@echo off
rem (Raiz do projeto) / PARAR_PROGRAMA.bat

echo Parando o sistema do hospital...
echo (Isso vai desligar o servidor e o banco de dados)
echo.

docker-compose down

echo.
echo Sistema parado com sucesso.
echo.
pause