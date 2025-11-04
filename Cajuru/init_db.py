from controllers.app_controller import create_app
from utils.create_db import create_db
import time
import sys
from sqlalchemy.exc import OperationalError

print("--- Script de Inicializacao do Banco de Dados ---")

max_tentativas = 20
tentativa = 1
while tentativa <= max_tentativas:
    try:
        print(f"Tentativa de conexao com o DB (Tentativa {tentativa}/{max_tentativas})...")

        app = create_app()

        with app.app_context():
            create_db(app)
        
        print(">>> SUCESSO: Banco de dados conectado e tabelas verificadas/criadas.")
        break
    
    except OperationalError as e:
        print(f"AVISO: Nao foi possivel conectar ao banco de dados.")
        print("O servico do MySQL pode estar iniciando. Tentando novamente em 5 segundos...")
        time.sleep(5)
        tentativa += 1
    
    except Exception as e:
        print(f"Erro inesperado ao inicializar o DB: {e}")
        sys.exit(1)

if tentativa > max_tentativas:
    print("ERRO CRITICO: Nao foi possivel conectar ao banco de dados.")
    sys.exit(1)

print("--- Fim do Script de Inicializacao ---")