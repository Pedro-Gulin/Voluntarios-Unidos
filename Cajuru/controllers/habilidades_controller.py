from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db
from models.voluntarios.habilidades import Habilidades
from models.voluntarios.habilidade_voluntario import Habilidade_voluntario

habilidades_ = Blueprint("habilidades", __name__, template_folder="views")

@habilidades_.route('/cadastrar_habilidade')
def cadastrar_habilidade():
    return render_template("cadastrar_habilidade.html")

@habilidades_.route('/add_habilidade', methods=['POST'])
def add_habilidade():
    global habilidades 
    if request.method == 'POST':
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        
        habilidade_ja_existe = Habilidades.buscar_habilidade_especifica(nome)
        if habilidade_ja_existe:
            flash("Habilidade ja existe!")
            return redirect(url_for('habilidade.cadastrar_habilidade'))
        
        Habilidades.salvar_habilidade(nome, descricao)
        flash("Habilidade cadastrada com sucesso!")
        return redirect("habilidades")
        
@habilidades_.route('/edit_habilidade')
def edit_habilidade():
    nome = request.args.get('nome')
    habilidade = Habilidades.buscar_habilidade_especifica(nome)

    return render_template("update_habilidade.html", habilidade=habilidade, nome=nome)

@habilidades_.route('/updt_habilidade', methods=['POST'])
def updt_habilidade():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        
        habilidade = Habilidades.buscar_habilidade_especifica(nome)
        
        if descricao:
            habilidade.descricao = descricao
        
        db.session.commit()
        flash("Habilidade atualizada com sucesso!")
        return redirect("habilidades")
    
@habilidades_.route('/del_habilidade', methods=['GET'])
def del_habilidade():
    nome = request.args.get("nome")

    habilidade = Habilidades.buscar_habilidade_especifica(nome)
    
    habilidade_voluntario = Habilidade_voluntario.buscar_habilidade_por_idhabilidade(habilidade.id)
    
    if habilidade_voluntario:
        flash("Precisa deletar o vinculo da habilidade com o voluntario antes")
        return redirect("/habilidades")
    
    else:
        db.session.delete(habilidade)
        db.session.commit()
        
        flash("Habilidade deletada com sucesso!")

        return redirect("/habilidades")