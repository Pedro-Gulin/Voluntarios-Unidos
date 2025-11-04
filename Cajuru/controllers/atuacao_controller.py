from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db
from models.voluntarios.areas import Areas
from models.voluntarios.atuacao import Atuacao
from models.voluntarios.voluntarios import Voluntarios

atuacao = Blueprint("atuacao", __name__, template_folder="views")

@atuacao.route('/listar_atuacoes')
def listar_atuacoes():
    atuacoes = Atuacao.buscar_atuacoes()
    return render_template("listar_atuacoes.html", atuacoes = atuacoes)

@atuacao.route('/cadastrar_atuacao')
def cadastrar_atuacao():
    render_template("cadastrar_atuacao.html")

@atuacao.route('/add_atuacao', methods=['POST'])
def add_atuacao():
    global Atuacao 
    if request.method == 'POST':
        nome_voluntario = request.form["nome_voluntario"]
        nome_area = request.form["nome_area"]
        horas = request.form["horas"]
        valor_hora = request.form["valor_hora"]
        descricao = request.form["descricao"]
        data_inicio = request.form["data_inicio"]
        data_fim = request.form["data_fim"]
        
        Atuacao.salvar_atuacao(nome_voluntario, nome_area, horas, descricao, data_inicio, data_fim)
     
     
@atuacao.route('/edit_atuacao')
def edit_atuacao():
    nome_voluntario = request.args.get("nome_voluntario")
    atuacao_obj = Atuacao.buscar_atuacao_voluntario(nome_voluntario)
    return render_template("update_atuacao.html", atuacao = atuacao_obj)
        
@atuacao.route('/update_atuacao', methods=['POST'])
def update_atuacao():
    nome_voluntario = request.form["nome_voluntario"]

    atuacao_obj = Atuacao.buscar_atuacao_voluntario(nome_voluntario)
        
    if atuacao_obj:
        nome_area = request.form["nome_area"]
        horas = request.form["horas"]
        valor_hora = request.form["valor_hora"]
        descricao = request.form["descricao"]
        data_inicio = request.form["data_inicio"]
        data_fim = request.form["data_fim"]

        if nome_area:
            atuacao_obj.nome_area = nome_area
        if horas:
            atuacao_obj.horas = horas
        if valor_hora:
            atuacao_obj.valor_hora = valor_hora
        if descricao:
            atuacao_obj.descricao = descricao
        if data_inicio:
            atuacao_obj.data_inicio = data_inicio
        if data_fim:
            atuacao_obj.data_fim = data_fim
            
        db.session.commit()
        flash("Atuação atualizada com sucesso!")
        return redirect(url_for('atuacao.listar_atuacoes'))
    else:
        flash("Atuacao nao encontrada!")
        db.session.rollback()
        return redirect(url_for('atuacao.listar_atuacoes'))
    
@atuacao.route('/del_atuacao', methods=['GET'])
def del_atuacao():
    nome_voluntario = request.args.get("nome_voluntario")
    atuacao = Atuacao.buscar_atuacao_voluntario(nome_voluntario)
            
    db.session.delete(atuacao)
    db.session.commit()
    flash("Atuação deletada com sucesso!")
    return redirect(url_for('atuacao.listar_atuacoes'))