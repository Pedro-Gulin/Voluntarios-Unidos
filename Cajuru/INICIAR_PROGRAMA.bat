@echo off
echo Iniciando o sistema do hospital...
echo (Isso pode demorar um pouco na primeira vez)
echo.

docker-compose up -d

echo.
echo PRONTO!
echo.
echo O sistema esta rodando. 
echo Abra seu navegador e acesse:
echo http://localhost:8449
echo.
pause