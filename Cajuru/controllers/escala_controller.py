from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db
from models.voluntarios.escala import Escala
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.areas import Areas

escala_ = Blueprint("escala", __name__, template_folder="views")

@escala_.route('/cadastrar_escala')
def cadastrar_escala():
    return render_template("cadastrar_escala.html")

@escala_.route('/add_escala', methods=['POST'])
def add_escala():
    global escala 
    if request.method == 'POST':
        cpf_voluntario = request.form["cpf_voluntario"]
        nome_area = request.form["nome_area"]
        data = request.form["data"]
        turno = request.form["turno"]
        status = request.form["status"]
        
        id_voluntario = Voluntarios.buscar_id_por_cpf(cpf_voluntario)
        id_area = Areas.buscar_area_especifica(nome_area)
        
        escala_ja_existe = Escala.buscar_escala_especifica(id_voluntario)
        if escala_ja_existe:
            flash("Escala ja cadastrada")
            return redirect(url_for('escala.cadastrar_escala'))
        
        Escala.salvar_escala(id_voluntario, id_area, data, turno, status)
        flash("Escala cadastrada com sucesso!")
        return redirect("escalas")
    
@escala_.route('/edit_escala')
def edit_escala():
    id_voluntario = request.args.get('id_voluntario')
    escala = Escala.buscar_escala_especifica(id_voluntario)
        
    return render_template("update_escala.html", escala = escala, id_voluntario = id_voluntario)
    
@escala_.route('/updt_escala', methods=['POST'])
def updt_escala():
    if request.method == 'POST':
        nome_voluntario = request.form['nome_voluntario']
        nome_area = request.form['nome_area']
        id_voluntario = Escala.buscar_escala_id_por_nome(nome_voluntario)
        id_area = Areas.buscar_area_id_por_nome(nome_area)
        data = request.form['data']
        turno = request.form['turno']
        status = request.form['status']
            
        escala = Escala.buscar_escala_especifica(id_voluntario)
            
        if id_area:
            escala.nome_area = nome_area
                
        if data:
            escala.data = data 
                
        if turno:
            escala.turno = turno 
                
        if status:
            escala.status = status 
                
        db.session.commit()
        flash("Escala editada com sucesso")
        return redirect("escalas")
        
@escala_.route('/del_escala', methods=['GET'])
def del_escala():
    id_voluntario = request.args.get("id_voluntario")
    escala = Escala.buscar_escala_especifica(id_voluntario)
            
    db.session.delete(escala)
    db.session.commit()
    flash("Escala deletada com sucesso!")
    return redirect("/escalas")
        
        
        