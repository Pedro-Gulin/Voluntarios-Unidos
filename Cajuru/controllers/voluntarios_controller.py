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

@voluntarios.route('/edit_voluntario')
def edit_voluntario():
    cpf = request.args.get("cpf")
    voluntario = Voluntarios.buscar_por_cpf(cpf)
    return render_template("update_voluntario.html", cpf = cpf, voluntario = voluntario)

@voluntarios.route('/updt_voluntario', methods=['POST'])
def updt_voluntario():
    if request.method == 'POST':
        cpf = request.form['cpf']
        voluntario = Voluntarios.buscar_por_cpf(cpf)

        if not voluntario:
            flash("Voluntário não encontrado!", "danger")
            return redirect("listar_voluntarios")

        data_nasc = request.form['data_nasc']
        local_nasc = request.form['local_nasc']
        rg = request.form['rg']
        cpf = request.form['cpf']
        estado_civil = request.form['estado_civil']
        nome_conjuge = request.form['nome_conjuge']
        nome_pai = request.form['nome_pai']
        nome_mae = request.form['nome_mae']
        endereco = request.form['endereco']
        cep = request.form['cep']
        telefone = request.form['telefone']
        religiao = request.form['religiao']
        email = request.form['email']
        escolaridade = request.form['escolaridade']
        local_trabalho = request.form['local_trabalho']
        ocupacao = request.form['ocupacao']
        tratamento = request.form['tratamento']
        transporte = request.form['transporte']
        sab_volun = request.form['sab_volun']
        trab_vol = request.form['trab_vol']
        grupo_vol = request.form['grupo_vol']
        como_contri = request.form['como_contri']
        musical = request.form['musical']
        alimentacao = request.form['alimentacao']
        data_vinculo = request.form['data_vinculo']
        codigo_carteirinha = request.form['codigo_carteirinha']
        
        if data_nasc:
            voluntario.data_nasc = data_nasc

        if local_nasc:
            voluntario.local_nasc = local_nasc

        if rg:
            voluntario.rg = rg

        if cpf:
            voluntario.cpf = cpf

        if estado_civil:
            voluntario.estado_civil = estado_civil

        if nome_conjuge:
            voluntario.nome_conjuge = nome_conjuge

        if nome_pai:
            voluntario.nome_pai = nome_pai

        if nome_mae:
            voluntario.nome_mae = nome_mae

        if endereco:
            voluntario.endereco = endereco

        if cep:
            voluntario.cep = cep

        if telefone:
            voluntario.telefone = telefone

        if religiao:
            voluntario.religiao = religiao

        if email:
            voluntario.email = email

        if escolaridade:
            voluntario.escolaridade = escolaridade

        if local_trabalho:
            voluntario.local_trabalho = local_trabalho

        if ocupacao:
            voluntario.ocupacao = ocupacao

        if tratamento:
            voluntario.tratamento = tratamento

        if transporte:
            voluntario.transporte = transporte

        if sab_volun:
            voluntario.sab_volun = sab_volun

        if trab_vol:
            voluntario.trab_vol = trab_vol

        if grupo_vol:
            voluntario.grupo_vol = grupo_vol

        if como_contri:
            voluntario.como_contri = como_contri

        if musical:
            voluntario.musical = musical

        if alimentacao:
            voluntario.alimentacao = alimentacao

        if data_vinculo:
            voluntario.data_vinculo = data_vinculo

        if codigo_carteirinha:
            voluntario.codigo_carteirinha = codigo_carteirinha


        db.session.commit()
        flash("Voluntário(a) atualizado(a) com sucesso!", "success")
        return redirect("listar_voluntarios")
    
@voluntarios.route('/del_voluntario', methods=['GET'])
def del_voluntario():
    cpf = request.args.get("cpf")
    voluntario = Voluntarios.buscar_por_cpf(cpf)
    
    if voluntario:
        db.session.delete(voluntario)
        db.session.commit()
        flash("Voluntário(a) deletado(a) com sucesso!", "success")
        return redirect("listar_voluntarios")
    else:
        flash("Não foi possível deletar o voluntário(a)!", "success")
        return redirect("listar_voluntarios")