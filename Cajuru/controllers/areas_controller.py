from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db
from models.voluntarios.areas import Areas

areas_ = Blueprint("areas", __name__, template_folder="views")

@areas_.route('/cadastrar_area')
def cadastrar_area():
    return render_template("cadastrar_area.html")

@areas_.route('/add_area', methods=['POST'])
def add_area():
    global areas 
    if request.method == 'POST':
        nome = request.form["nome"]
        quantidade_horas = request.form["quantidade_horas"]
        descricao = request.form["descricao"]
        
        area_ja_existe = Areas.buscar_area_especifica(nome)
        if area_ja_existe:
            flash("Area ja existe!")
            return redirect(url_for('area.cadastrar_area'))
        
        Areas.salvar_area(nome, quantidade_horas, descricao)
        flash("Area cadastrada com sucesso!")
        return redirect("areas")
        
@areas_.route('/edit_area')
def edit_area():
    nome = request.args.get('nome')
    area = Areas.buscar_area_especifica(nome)

    return render_template("update_area.html", area=area, nome=nome)

@areas_.route('/updt_area', methods=['POST'])
def updt_area():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade_horas = request.form['quantidade_horas']
        descricao = request.form['descricao']
        
        area = Areas.buscar_area_especifica(nome)
        
        if quantidade_horas:
            area.quantidade_horas = quantidade_horas
        
        if descricao:
            area.descricao = descricao
        
        db.session.commit()
        flash("Area atualizada com sucesso!")
        return redirect("areas")
    
@areas_.route('/del_area', methods=['GET'])
def del_area():
    nome = request.args.get("nome")

    area = Areas.buscar_area_especifica(nome)

    db.session.delete(area)
    db.session.commit()
    
    flash("Area deletada com sucesso!")

    return redirect("/areas")