from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db
from models.voluntarios.voluntarios import Voluntarios

voluntarios = Blueprint("voluntarios", __name__, template_folder="views")

@voluntarios.route('/cadastrar_voluntario')
def cadastrar_voluntario():
    return render_template("cadastro_voluntario.html")

@voluntarios.route('/add_voluntario_1', methods=['POST'])
def add_voluntario_1():
    global Voluntarios
    global voluntarios
    
    session['voluntario'] = {
        'nome': request.form['nome'],
        'data_nasc': request.form['dataNascimento'],
        'local_nasc': request.form['localNascimento'],
        'rg': request.form['rg'],
        'cpf': request.form['cpf'],
        'estado_civil': request.form['estadoCivil'],
        'nome_conjuge': request.form['nomeConjugue'],
        'nome_pai': request.form['nomePai'],
        'nome_mae': request.form['nomeMae'],
        'endereco': request.form['enderecoResidencial'],
        'cep': request.form['cep'],
        'telefone': request.form['celular'],
        'religiao': request.form['religiao'],
        'email': request.form['email'],
        'escolaridade': request.form['escolaridade'],
        'local_trabalho': request.form['localTrabalho'],
        'ocupacao': request.form['ocupacao'],
        'tratamento': request.form['tratamento'],
        'transporte': request.form['tipoTransporte'],
        'sab_volun': request.form['comoFicouSabendo']
    }

    return render_template("cadastro_voluntario_2.html")

@voluntarios.route('/add_voluntario_2', methods=['POST'])
def add_voluntario_2():
    global Voluntarios
    global voluntarios
    
    voluntario = session.get('voluntario', {})
    voluntario.update({
        'trab_vol': request.form['experiencias'],
        'grupo_vol': request.form['grupoVoluntario'],
        'como_contri': request.form['porqueVoluntario'],
        'musical': request.form['habilidadeMusical'],
        'alimentacao': request.form['alimentacao'],
        'data_vinculo': request.form['dataVinculo']
    })
    
    Voluntarios.salvar_voluntario(
        voluntario['nome'],
        voluntario['data_nasc'],
        voluntario['local_nasc'],
        voluntario['rg'],
        voluntario['cpf'],
        voluntario['estado_civil'],
        voluntario['nome_conjuge'],
        voluntario['nome_pai'],
        voluntario['nome_mae'],
        voluntario['endereco'],
        voluntario['cep'],
        voluntario['telefone'],
        voluntario['religiao'],
        voluntario['email'],
        voluntario['escolaridade'],
        voluntario['local_trabalho'],
        voluntario['ocupacao'],
        voluntario['tratamento'],
        voluntario['transporte'],
        voluntario['sab_volun'],
        voluntario['trab_vol'],
        voluntario['grupo_vol'],
        voluntario['como_contri'],
        voluntario['musical'],
        voluntario['alimentacao']
    )
    
    session.pop('voluntario', None)
    return redirect(url_for('home'))