from flask import Blueprint, render_template, request, redirect, flash
from models import db
from models.voluntarios.ponto import Ponto
from models.voluntarios.voluntarios import Voluntarios
from datetime import datetime
from controllers.shared_state import ultima_tag

ponto_ = Blueprint("ponto_", __name__, template_folder="views")

def processar_tag(tag):
    tag = tag.strip()
    voluntario = Voluntarios.buscar_por_tag(tag)
    if voluntario:
        try:
            horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            Ponto.bater_ponto(voluntario.cpf, voluntario.codigo_carteirinha, horario_atual)
            print(f"Ponto batido por {voluntario.nome} ({voluntario.cpf}) às {horario_atual}")
            return f"Ponto registrado para {voluntario.nome}"
        except Exception as e:
            print(f"Erro ao bater ponto: {str(e)}")
            return "Erro ao registrar ponto"
    else:
        cpf_em_espera = getattr(processar_tag, "cpf_temp", None)

        if cpf_em_espera:
            voluntario = Voluntarios.associar_tag_por_cpf(cpf_em_espera, tag)
            if voluntario:
                print(f"Tag {tag} associada ao CPF {cpf_em_espera} ({voluntario.nome})")
                horario_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Ponto.bater_ponto(voluntario.cpf, voluntario.codigo_carteirinha, horario_atual)
                processar_tag.cpf_temp = None
                return f"Tag associada e ponto registrado para {voluntario.nome}"
        associado = Voluntarios.associar_tag_ao_voluntario(tag)
        if associado:
            print(f"Tag {tag} associada ao voluntário {associado.nome}.")
            return f"Tag associada a {associado.nome}"
        else:
            print(f"Nenhum voluntário disponível para associar a tag {tag}.")
            return "Nenhum voluntário disponível para associar"

@ponto_.route('/cadastrar_ponto')
def cadastrar_ponto():
    voluntario = Voluntarios.buscar_por_tag(ultima_tag)
    cpf_voluntario = voluntario.cpf if voluntario else ""

    return render_template(
        "cadastrar_ponto.html",
        ultima_tag=ultima_tag,
        cpf_voluntario=cpf_voluntario
    )

from models.voluntarios.voluntarios import Voluntarios

@ponto_.route('/add_ponto', methods=['POST'])
def add_ponto():
    cpf_voluntario = request.form.get("cpf_voluntario")
    numero_carteirinha = request.form.get("numero_carteirinha")

    if cpf_voluntario and numero_carteirinha and numero_carteirinha != "Nenhuma tag lida ainda":
        voluntario = Voluntarios.buscar_por_cpf(cpf_voluntario)
        if voluntario and not voluntario.codigo_carteirinha:
            voluntario.codigo_carteirinha = numero_carteirinha
            db.session.commit()
            flash(f"Tag vinculada ao CPF {cpf_voluntario} com sucesso!")

    try:
        Ponto.bater_ponto(cpf_voluntario, numero_carteirinha)
        
        flash("Ponto cadastrado com sucesso!")
    except ValueError as e:
        flash(f"Erro: {str(e)}")
    except Exception as e:
        flash(f"Erro ao registrar ponto: {str(e)}")

    return redirect('/ponto')

@ponto_.route('/edit_ponto')
def edit_ponto():
    id_ponto = request.args.get('id')
    ponto = Ponto.buscar_ponto_id(id_ponto)

    if not ponto:
        flash("Ponto não encontrado.")
        return redirect('/ponto')

    return render_template("update_ponto.html", ponto=ponto)


@ponto_.route('/updt_ponto', methods=['POST'])
def updt_ponto():
    id_ponto = request.form.get('id')
    horario = request.form.get('horario')

    ponto = Ponto.buscar_ponto_id(id_ponto)

    if not ponto:
        flash("Ponto não encontrado.")
        return redirect('/ponto')

    if horario and horario != ponto.horario:
        ponto.horario = horario
        db.session.commit()
        flash("Ponto atualizado com sucesso!")
    else:
        flash("Nenhuma alteração realizada.")

    return redirect('/ponto')


@ponto_.route('/del_ponto', methods=['GET'])
def del_ponto():
    id_ponto = request.args.get("id")
    ponto = Ponto.buscar_ponto_id(id_ponto)

    if ponto:
        db.session.delete(ponto)
        db.session.commit()
        flash("Ponto deletado com sucesso!")
    else:
        flash("Não foi possível deletar o ponto.")

    return redirect('/ponto')