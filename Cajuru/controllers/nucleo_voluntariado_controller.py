from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models.db import db
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.nucleo_voluntariado import nucleo_voluntariado

nucleo_voluntariado_ = Blueprint("nucleo_voluntariado", __name__, template_folder="views")

@nucleo_voluntariado_.route('/cadastrar_nucleo_voluntariado')
def cadastrar_nucleo_voluntariado():
    return render_template("cadastrar_nucleo_voluntariado.html")

@nucleo_voluntariado_.route('/add_nucleo_voluntariado', methods=['POST'])
def add_nucleo_voluntariado():
    global nucleo_voluntariados 
    if request.method == 'POST':
        cpf_voluntario = request.form["cpf_voluntario"]
        id_voluntario = Voluntarios.buscar_id_por_cpf(cpf_voluntario)
        nome_voluntario = Voluntarios.buscar_nome_por_id(id_voluntario)
        domingo = request.form["domingo"]
        segunda_feira = request.form["segunda_feira"]
        terca_feira = request.form["terca_feira"]
        quarta_feira = request.form["quarta_feira"]
        quinta_feira = request.form["quinta_feira"]
        sexta_feira = request.form["sexta_feira"]
        sabado = request.form["sabado"]
        
        nucleo_voluntariado_ja_existe = nucleo_voluntariado.buscar_nucleo_voluntariado_especifico(id_voluntario)
        
        if nucleo_voluntariado_ja_existe:
            flash("Nucleo_voluntariado ja existe!")
            return redirect(url_for('nucleo_voluntariado.cadastrar_nucleo_voluntariado'))
        
        nucleo_voluntariado.save_nucleo_voluntario(id_voluntario, nome_voluntario, domingo, segunda_feira, terca_feira, quarta_feira, quinta_feira, sexta_feira, sabado)
        flash("Nucleo_voluntariado cadastrado com sucesso!")
        return redirect("nucleo_voluntariado")
    
@nucleo_voluntariado_.route('/edit_nucleo_voluntariado')
def edit_nucleo_voluntariado():
    id_voluntario = request.args.get('id_voluntario')
    nucleo_voluntariados = nucleo_voluntariado.buscar_nucleo_voluntariado_especifico(id_voluntario)

    return render_template("update_nucleo_voluntariado.html", nucleo_voluntariados=nucleo_voluntariados, id_voluntario=id_voluntario)

@nucleo_voluntariado_.route('/updt_nucleo_voluntariado', methods=['POST'])
def updt_nucleo_voluntariado():
    if request.method == 'POST':
        id_voluntario = request.form["id_voluntario"]
        domingo = request.form["domingo"]
        segunda_feira = request.form["segunda_feira"]
        terca_feira = request.form["terca_feira"]
        quarta_feira = request.form["quarta_feira"]
        quinta_feira = request.form["quinta_feira"]
        sexta_feira = request.form["sexta_feira"]
        sabado = request.form["sabado"]
        
        nucleo_voluntariados = nucleo_voluntariado.buscar_nucleo_voluntariado_especifico(id_voluntario)
        
        if domingo:
            nucleo_voluntariados.domingo = domingo
        
        if segunda_feira:
            nucleo_voluntariados.segunda_feira = segunda_feira
            
        if terca_feira:
            nucleo_voluntariados.terca_feira = terca_feira
            
        if quarta_feira:
            nucleo_voluntariados.quarta_feira = quarta_feira
            
        if quinta_feira:
            nucleo_voluntariados.quinta_feira = quinta_feira
            
        if sexta_feira:
            nucleo_voluntariados.sexta_feira = sexta_feira
            
        if sabado:
            nucleo_voluntariados.sabado = sabado
        
        db.session.commit()
        flash("Nucleo_voluntariado atualizado com sucesso!")
        return redirect("nucleo_voluntariado")
    
@nucleo_voluntariado_.route('/del_nucleo_voluntariado', methods=['GET'])
def del_nucleo_voluntariado():
    id_voluntario = request.args.get("id_voluntario")
    
    nucleo_voluntariados = nucleo_voluntariado.buscar_nucleo_voluntariado_especifico(id_voluntario)
    
    db.session.delete(nucleo_voluntariados)
    db.session.commit()
    
    flash("Nucleo voluntariado deletado com sucesso!")
    return redirect("/nucleo_voluntariado")