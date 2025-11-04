from flask import Flask, session, request, render_template, redirect, url_for, Blueprint
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from models.voluntarios.voluntarios import Voluntarios

cadastro_voluntario = Blueprint("cadastro_voluntario",__name__, template_folder="templates")

@cadastro_voluntario.route('/cadastro_voluntario', methods=['GET', 'POST'])
def cadastrar_voluntario():
    if request.method == 'POST':
        db = SessionLocal()
        try:
            data_nasc = datetime.strptime(request.form.get('dataNascimento'), "%Y-%m-%d").date()
            voluntario = Voluntario(
                nome=request.form.get('nome'),
                data_nasc=data_nasc,
                local_nasc=request.form.get('localNascimento'),
                rg=request.form.get('rg'),
                cpf=request.form.get('cpf'),
                estado_civil=request.form.get('estadoCivil'),
                nome_conjuge=request.form.get('nomeConjugue'),
                nome_pai=request.form.get('nomePai'),
                nome_mae=request.form.get('nomeMae'),
                endereco=request.form.get('enderecoResidencial'),
                cep=request.form.get('cep'),
                telefone=request.form.get('celular'),
                religiao=request.form.get('religiao'),
                email=request.form.get('email'),
                escolaridade=request.form.get('escolaridade'),
                local_trabalho=request.form.get('localTrabalho'),
                ocupacao=request.form.get('ocupacao'),
                tratamento=request.form.get('tratamento'),
                transporte=request.form.get('tipoTransporte'),
                sab_volun=request.form.get('comoFicouSabendo')
            )
            db.add(voluntario)
            db.commit()
            db.refresh(voluntario)

            return render_template("home.html", nome=voluntario.nome)

        except IntegrityError as e:
            db.rollback()
            print("Erro: ", e)
            return "Erro: CPF ou e-mail já cadastrado."
        finally:
            db.close()

    return render_template("cadastro_voluntario.html")

@cadastro_voluntario.route('/cadastro_voluntario_2', methods = ['GET', 'POST'])
def cadastro_voluntario_2():
    return render_template("cadastro_voluntario_2.html")

@cadastro_voluntario.route('/cadastro_voluntario_3', methods = ['GET', 'POST'])
def cadastro_voluntario_3():
    return render_template("cadastro_voluntario_3.html")

@cadastro_voluntario.route('/cadastro_voluntario_4', methods = ['GET', 'POST'])
def cadastro_voluntario_4():
    return render_template("cadastro_voluntario_4.html")

