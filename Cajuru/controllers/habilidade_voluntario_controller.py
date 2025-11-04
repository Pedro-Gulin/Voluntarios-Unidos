from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models.db import db
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.habilidades import Habilidades
from models.voluntarios.habilidade_voluntario import Habilidade_voluntario

habilidade_voluntario_ = Blueprint("habilidade_voluntario", __name__, template_folder="views")

@habilidade_voluntario_.route('/associar_habilidade')
def associar_habilidade():
    return render_template("associar_habilidade.html")

@habilidade_voluntario_.route('/add_habilidade', methods=['POST'])
def add_habilidade():
    if request.method == 'POST':
        cpf_voluntario = request.form["cpf_voluntario"]
        nome_habilidade = request.form["nome_habilidade"]
        voluntario_id = Voluntarios.buscar_id_por_cpf(cpf_voluntario)
        nome_voluntario = Voluntarios.buscar_nome_por_id(voluntario_id)
        habilidade_id = Habilidades.buscar_habilidade_nome_id(nome_habilidade)
        
        if voluntario_id and habilidade_id:
            Habilidade_voluntario.save_habilidade_voluntario(voluntario_id, habilidade_id, nome_voluntario, nome_habilidade)
            flash("Habilidade associada com sucesso")
            return redirect("habilidades_voluntarios")
        
        else:
            flash("Habilidade ou voluntario nao encontrados!")
            return redirect("habilidades_voluntarios")
        
@habilidade_voluntario_.route('/edit_habilidade_voluntario')
def edit_habilidade_voluntario():
    voluntario_id = request.args.get("voluntario_id")
    habilidade_voluntario = Habilidade_voluntario.buscar_habilidade_voluntario_especifico(voluntario_id)
    
    return render_template("update_habilidade_voluntario.html", habilidade_voluntario = habilidade_voluntario, voluntario_id = voluntario_id)

@habilidade_voluntario_.route('/updt_habilidade_voluntario', methods=['POST'])
def updt_habilidade_voluntario():
    if request.method == 'POST':
        id_voluntario = request.form['id_voluntario']
        nome_voluntario = request.form['nome_voluntario']
        nome_habilidade = request.form['nome_habilidade']
        id_habilidade = Habilidades.buscar_habilidade_nome_id(nome_habilidade)
        
        habilidade_voluntario = Habilidade_voluntario.buscar_habilidade_voluntario_especifico(id_voluntario)
        
        if id_habilidade:
            habilidade_voluntario.id_habilidade = id_habilidade
            habilidade_voluntario.nome_habilidade = nome_habilidade
        
        db.session.commit()
        flash("A habilidade do voluntario foi atualizada com sucesso")
        return redirect("habilidades_voluntarios")
    
@habilidade_voluntario_.route('/del_habilidade_voluntario', methods=['GET'])
def del_habilidade_voluntario():
    id_voluntario = request.args.get("id_voluntario")
    habilidade_voluntario = Habilidade_voluntario.buscar_habilidade_voluntario_especifico(id_voluntario)
    
    if not habilidade_voluntario:
        flash("Registro não encontrado!")
        return redirect("habilidade_voluntario")
    
    db.session.delete(habilidade_voluntario)
    db.session.commit()
    flash("Vínculo da habilidade com o voluntário encerrado!")
    return redirect("habilidade_voluntario")