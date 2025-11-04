from flask import Flask 
from models.user.users import Users
from models.db import db
from models.user.roles import Role
from models.voluntarios.areas import Areas
from models.voluntarios.atuacao import Atuacao
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.escala import Escala
from models.voluntarios.habilidades import Habilidades
from models.voluntarios.habilidade_voluntario import Habilidade_voluntario
from models.voluntarios.nucleo_voluntariado import nucleo_voluntariado
from models.voluntarios.ponto import Ponto


def create_db(app: Flask):
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # ---- USERS E ROLES ----
        Role.save_role("Admin", "Usuario full")
        Role.save_role("User", "User com limitacoes")
        Users.save_user("pedro@pedro.com", "1234", "Admin")
        Users.save_user("teste@teste.com", "12345", "User")

        # ---- AREAS ----
        Areas.salvar_area("Maqueiro", 12, "Carregador de maca")
        Areas.salvar_area("Cozinha", 8, "Ajuda no preparo e distribuição de alimentos")
        Areas.salvar_area("Recepção", 6, "Atendimento inicial e orientação ao público")
        Areas.salvar_area("Limpeza", 10, "Higienização de áreas comuns do hospital")

        # ---- VOLUNTARIOS ----
        Voluntarios.salvar_voluntario(
            nome="Pedro da Silva",
            data_nasc="1990-01-01",
            local_nasc="Curitiba",
            rg="1234567",
            cpf="12345678900",
            estado_civil="Solteiro",
            nome_conjuge=None,
            nome_pai="José da Silva",
            nome_mae="Maria da Silva",
            endereco="Rua das Flores, 123",
            cep="80000-000",
            telefone="(41)99999-9999",
            religiao="Católica",
            email="pedro@teste.com",
            escolaridade="Ensino Médio Completo",
            local_trabalho="Hospital Cajuru",
            ocupacao="Auxiliar",
            tratamento="Senhor",
            transporte="Ônibus",
            sab_volun="Sábados de manhã",
            trab_vol="Auxílio na cozinha",
            grupo_vol="Grupo de apoio alimentar",
            como_contri="Preparando refeições",
            musical="Violão",
            alimentacao="Vegetariano",
            data_vinculo = "2025-10-04",
            codigo_carteirinha = "12314245"
        )

        Voluntarios.salvar_voluntario(
            nome="Ana Paula Souza",
            data_nasc="1985-05-14",
            local_nasc="Londrina",
            rg="7654321",
            cpf="98765432100",
            estado_civil="Casada",
            nome_conjuge="Carlos Souza",
            nome_pai="Roberto Souza",
            nome_mae="Helena Souza",
            endereco="Av. Brasil, 890",
            cep="86000-100",
            telefone="(43)98888-8888",
            religiao="Evangélica",
            email="ana@teste.com",
            escolaridade="Ensino Superior Completo",
            local_trabalho="Colégio Estadual",
            ocupacao="Professora",
            tratamento="Senhora",
            transporte="Carro",
            sab_volun="Domingos à tarde",
            trab_vol="Atendimento ao público",
            grupo_vol="Grupo de recepção",
            como_contri="Orientando visitantes",
            musical="Piano",
            alimentacao="Comum",
            data_vinculo = "2025-10-15",
            codigo_carteirinha = "98765432"
        )

        Voluntarios.salvar_voluntario(
            nome="João Pereira",
            data_nasc="1995-07-20",
            local_nasc="Maringá",
            rg="4567890",
            cpf="11122233344",
            estado_civil="Solteiro",
            nome_conjuge=None,
            nome_pai="Antônio Pereira",
            nome_mae="Cláudia Pereira",
            endereco="Rua Santos, 45",
            cep="87000-200",
            telefone="(44)97777-7777",
            religiao="Espírita",
            email="joao@teste.com",
            escolaridade="Ensino Técnico",
            local_trabalho="Oficina Pereira",
            ocupacao="Mecânico",
            tratamento="Senhor",
            transporte="Bicicleta",
            sab_volun="Sábados à tarde",
            trab_vol="Manutenção de equipamentos",
            grupo_vol="Equipe de manutenção",
            como_contri="Fazendo reparos",
            musical="Guitarra",
            alimentacao="Comum",
            data_vinculo = "2025-10-10",
            codigo_carteirinha = "55544433"
        )

        Voluntarios.salvar_voluntario(
            nome="Maria Oliveira",
            data_nasc="1992-03-03",
            local_nasc="Ponta Grossa",
            rg="9988776",
            cpf="44455566677",
            estado_civil="Casada",
            nome_conjuge="Paulo Oliveira",
            nome_pai="Luiz Oliveira",
            nome_mae="Cecília Oliveira",
            endereco="Rua Central, 234",
            cep="84000-300",
            telefone="(42)96666-6666",
            religiao="Católica",
            email="maria@teste.com",
            escolaridade="Ensino Médio Completo",
            local_trabalho="Mercado Central",
            ocupacao="Atendente",
            tratamento="Senhora",
            transporte="Carro",
            sab_volun="Domingos de manhã",
            trab_vol="Limpeza e higienização",
            grupo_vol="Grupo de limpeza",
            como_contri="Auxiliando na higienização",
            musical="Nenhum",
            alimentacao="Comum",
            data_vinculo = "2025-10-25",
            codigo_carteirinha = "99900011"
        )

        # ---- ATUACAO ----
        Atuacao.salvar_atuacao(1, 1, 12, 12.50, "Cozinha", "2025-10-23", "2025-10-25")
        Atuacao.salvar_atuacao(2, 2, 10, 11.00, "Recepção de visitantes", "2025-10-10", "2025-10-15")
        Atuacao.salvar_atuacao(3, 3, 8, 10.00, "Manutenção elétrica", "2025-10-05", "2025-10-09")
        Atuacao.salvar_atuacao(4, 4, 9, 9.50, "Limpeza de corredores", "2025-10-03", "2025-10-15")

        # ---- ESCALA ----
        Escala.salvar_escala(1, "Pedro da Silva", 1, "Maqueiro", "2025-10-04", "Manhã", "ativo")
        Escala.salvar_escala(2, "Ana Paula Souza", 2, "Cozinha", "2025-10-05", "Tarde", "ativo")
        Escala.salvar_escala(3, "João Pereira", 3, "Recepção", "2025-10-06", "Noite", "ativo")
        Escala.salvar_escala(4, "Maria Oliveira", 4, "Limpeza", "2025-10-07", "Manhã", "ativo")

        # ---- HABILIDADES ----
        Habilidades.salvar_habilidade("Cozinhar", "Sabe cozinhar bem")
        Habilidades.salvar_habilidade("Comunicação", "Boa comunicação com público")
        Habilidades.salvar_habilidade("Manutenção", "Capaz de realizar pequenos reparos")
        Habilidades.salvar_habilidade("Organização", "Sabe manter o ambiente limpo e organizado")

        # ---- HABILIDADE_VOLUNTARIO ----
        Habilidade_voluntario.save_habilidade_voluntario(1, 1, "Pedro da Silva", "Cozinhar")
        Habilidade_voluntario.save_habilidade_voluntario(2, 2, "Ana Paula Souza", "Comunicação")
        Habilidade_voluntario.save_habilidade_voluntario(3, 3, "João Pereira", "Manutenção")
        Habilidade_voluntario.save_habilidade_voluntario(4, 4, "Maria Oliveira", "Organização")


        # ---- NUCLEO_VOLUNTARIADO ----
        nucleo_voluntariado.save_nucleo_voluntario(1, "Pedro da Silva", "07:00 - 12:00", "00:00 - 00:00", "07:00 - 14:00", "00:00 - 00:00", "10:00 - 18:00", "00:00 - 00:00", "07:00 - 19:00")
        nucleo_voluntariado.save_nucleo_voluntario(2, "Ana Paula Souza", "00:00 - 00:00", "08:00 - 14:00", "00:00 - 00:00", "10:00 - 16:00", "00:00 - 00:00", "09:00 - 13:00", "00:00 - 00:00")
        nucleo_voluntariado.save_nucleo_voluntario(3, "João Pereira", "00:00 - 00:00", "09:00 - 12:00", "08:00 - 15:00", "00:00 - 00:00", "10:00 - 14:00", "00:00 - 00:00", "00:00 - 00:00")
        nucleo_voluntariado.save_nucleo_voluntario(4, "Maria Oliveira", "08:00 - 12:00", "00:00 - 00:00", "00:00 - 00:00", "09:00 - 15:00", "00:00 - 00:00", "07:00 - 13:00", "00:00 - 00:00")

        # ---- PONTO ----
        Ponto.bater_ponto("12345678900", "12314245", "2025-10-04")
        Ponto.bater_ponto("98765432100", "98765432", "2025-10-15")
        Ponto.bater_ponto("11122233344", "55544433", "2025-10-10")
        Ponto.bater_ponto("44455566677", "99900011", "2025-10-25")
