from flask import Blueprint, request, render_template, redirect, url_for, flash, session, jsonify
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.areas import Areas
from models.voluntarios.atuacao import Atuacao
from models.voluntarios.escala import Escala
from models.voluntarios.habilidade_voluntario import Habilidade_voluntario
from models.voluntarios.habilidades import Habilidades
from models.voluntarios.nucleo_voluntariado import nucleo_voluntariado
from models.voluntarios.ponto import Ponto
from datetime import datetime, date
from calendar import monthrange
from sqlalchemy import func, extract
from models import db 

#video de referencia: https://www.youtube.com/watch?v=E2hytuQvLlE

relatorios_ = Blueprint("relatorios", __name__, template_folder="views")

#1 - Quantidade de voluntarios por area por mes

@relatorios_.route('/voluntarios_mes')
def voluntarios_mes():
    return render_template("voluntarios_por_mes.html")

@relatorios_.route('/api/voluntarios_por_mes')
def api_voluntarios_por_mes():
    mes_str = request.args.get('mes')
    
    try:
        if mes_str:
            data_ref = datetime.strptime(mes_str, "%Y-%m")
        else:
            data_ref = date.today()

        _, ultimo_dia = monthrange(data_ref.year, data_ref.month)
        inicio, fim = date(data_ref.year, data_ref.month, 1), date(data_ref.year, data_ref.month, ultimo_dia)
        
        data = db.session.query(
            Atuacao.nome_area,
            func.count(Atuacao.id_voluntario.distinct())
        ).filter(
            Atuacao.data_inicio <= fim,
            Atuacao.data_fim >= inicio
        ).group_by(
            Atuacao.nome_area
        ).order_by(
            Atuacao.nome_area
        ).all()
        
        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        chart_data = {
            "labels": labels,
            "datasets": [{
                "label": "Voluntários Ativos por Área",
                "data": values,
                "backgroundColor": "rgba(54, 162, 235, 0.6)",
                "borderColor": "rgba(54, 162, 235, 1)",
                "borderWidth": 1
            }]
        }
        
        return jsonify(chart_data)

    except Exception as e:
        print("Erro:", e)

#2 - Quantidade de dinheiro economizado por area por mes

@relatorios_.route('/dinheiro_area_mes')
def dinheiro_area_mes():
    return render_template("dinheiro_area_mes.html")


@relatorios_.route('/api/dinheiro_area_mes')
def api_dinheiro_area_mes():
    mes_str = request.args.get('mes')
    try:
        if mes_str:
            data_ref = datetime.strptime(mes_str, "%Y-%m")
        else:
            data_ref = date.today()

        _, ultimo_dia = monthrange(data_ref.year, data_ref.month)
        inicio, fim = date(data_ref.year, data_ref.month, 1), date(data_ref.year, data_ref.month, ultimo_dia)
        
        data = db.session.query(
            Atuacao.nome_area,
            func.sum(Atuacao.horas * Atuacao.valor_hora)
        ).filter(
            Atuacao.data_inicio <= fim,
            Atuacao.data_fim >= inicio
        ).group_by(
            Atuacao.nome_area
        ).order_by(
            Atuacao.nome_area
        ).all()
        
        labels = [row[0] for row in data]
        values = [float(row[1]) if row[1] is not None else 0 for row in data] 

        chart_data = {
            "labels": labels,
            "datasets": [{
                "label": "Dinheiro Economizado por Área (R$)",
                "data": values,
                "backgroundColor": "rgba(75, 192, 192, 0.6)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }]
        }
        
        return jsonify(chart_data)

    except Exception as e:
        print("Erro:", e)
    
# 3 - Horas trabalhadas por voluntario por mes

@relatorios_.route('/horas_volu_mes')
def horas_volu_mes():
    return render_template("horas_volu_mes.html")

@relatorios_.route('/api/horas_volu_mes')
def api_horas_volu_mes():
    mes_str = request.args.get('mes')
    try:
        if mes_str:
            data_ref = datetime.strptime(mes_str, "%Y-%m")
        else:
            data_ref = date.today()

        _, ultimo_dia = monthrange(data_ref.year, data_ref.month)
        inicio, fim = date(data_ref.year, data_ref.month, 1), date(data_ref.year, data_ref.month, ultimo_dia)
    
        data = db.session.query(
            Atuacao.nome_voluntario,
            func.sum(Atuacao.horas)
        ).filter(
            Atuacao.data_inicio <= fim,
            Atuacao.data_fim >= inicio
        ).group_by(
            Atuacao.nome_voluntario
        ).order_by(
            Atuacao.nome_voluntario
        ).all()
        
        labels = [row[0] for row in data]
        values = [float(row[1]) if row[1] is not None else 0 for row in data] 

        chart_data = {
            "labels": labels,
            "datasets": [{
                "label": "Quantidade de horas trabalhadas por voluntario por mes",
                "data": values,
                "backgroundColor": "rgba(75, 192, 192, 0.6)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }]
        }
        
        return jsonify(chart_data)

    except Exception as e:
        print("Erro:", e)

#4 - Quantidade de horas trabalhadas por area por mes

@relatorios_.route('/horas_area_mes')
def horas_area_mes():
    return render_template("horas_area_mes.html")

@relatorios_.route('/api/horas_area_mes')
def api_horas_area_mes():
    mes_str = request.args.get('mes')
    try:
        if mes_str:
            data_ref = datetime.strptime(mes_str, "%Y-%m")
        else:
            data_ref = date.today()

        _, ultimo_dia = monthrange(data_ref.year, data_ref.month)
        inicio, fim = date(data_ref.year, data_ref.month, 1), date(data_ref.year, data_ref.month, ultimo_dia)
    
        data = db.session.query(
            Atuacao.nome_area,
            func.sum(Atuacao.horas)
        ).filter(
            Atuacao.data_inicio <= fim,
            Atuacao.data_fim >= inicio
        ).group_by(
            Atuacao.nome_area
        ).order_by(
            Atuacao.nome_area
        ).all()
        
        labels = [row[0] for row in data]
        values = [float(row[1]) if row[1] is not None else 0 for row in data] 

        chart_data = {
            "labels": labels,
            "datasets": [{
                "label": "Quantidade de horas trabalhadas por area por mes",
                "data": values,
                "backgroundColor": "rgba(75, 192, 192, 0.6)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }]
        }
        
        return jsonify(chart_data)
    except Exception as e:
        print("Erro:", e)
    
#5 - Quantidade de habilidades associadas a voluntarios

@relatorios_.route('/habilidades_associadas')
def habilidades_associadas():
    return render_template("habilidades_associadas.html")

@relatorios_.route('/api/habilidades_associadas')
def api_habilidades_associadas():
    mes_str = request.args.get('mes')
    try:
        if mes_str:
            data_ref = datetime.strptime(mes_str, "%Y-%m")
        else:
            data_ref = date.today()

        _, ultimo_dia = monthrange(data_ref.year, data_ref.month)
        inicio, fim = date(data_ref.year, data_ref.month, 1), date(data_ref.year, data_ref.month, ultimo_dia)
        
        data = db.session.query(
            Habilidade_voluntario.nome_habilidade,
            func.count(Habilidade_voluntario.id_voluntario)
        ).join(
            Atuacao, Atuacao.id_voluntario == Habilidade_voluntario.id_voluntario
        ).filter(
            Atuacao.data_inicio <= fim,
            Atuacao.data_fim >= inicio
        ).group_by(
            Habilidade_voluntario.nome_habilidade
        ).order_by(
            Habilidade_voluntario.nome_habilidade
        ).all()
        
        chart_data = {
            "labels": [nome for nome, _ in data],
            "datasets": [{
                "label": "Habilidades associadas",
                "data": [int(qtd or 0) for _, qtd in data],
                "backgroundColor": "rgba(75, 192, 192, 0.6)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }]
        }

        return jsonify(chart_data)
    except Exception as e:
        print("Erro:", e)
    
#6 - Quantidade de voluntarios novos por mes

@relatorios_.route('/novos_volu_ano')
def novos_volu_ano():
    return render_template("novos_volu_ano.html")

@relatorios_.route('/api/novos_volu_ano')
def api_novos_volu_ano():
    ano_str = request.args.get('ano')
    try:
        ano = int(ano_str) if ano_str else date.today().year
        inicio, fim = date(ano, 1, 1), date(ano, 12, 31)

        dados = (
            db.session.query(extract('month', Voluntarios.data_vinculo), func.count(Voluntarios.id))
            .filter(Voluntarios.data_vinculo.between(inicio, fim))
            .group_by(extract('month', Voluntarios.data_vinculo))
            .order_by(extract('month', Voluntarios.data_vinculo))
            .all()
        )

        labels = [int(mes) for mes, _ in dados]
        values = [int(qtd) for _, qtd in dados]

        chart_data = {
            "labels": labels,
            "datasets": [{
                "label": f"Novos voluntários em {ano}",
                "data": values,
                "backgroundColor": "rgba(75,192,192,0.6)",
                "borderColor": "rgba(75,192,192,1)",
                "borderWidth": 1
            }]
        }

        return jsonify(chart_data)

    except ValueError:
        return jsonify({"error": "Ano inválido. Use o formato YYYY."}), 400
    except Exception as e:
        print("Erro ao consultar o banco:", e)
        return jsonify({"error": "Erro interno ao processar sua solicitação."}), 500

    
#7 - Quantidade de pontos por funcionario por por mes

@relatorios_.route('/volu_pontos_mes')
def volu_pontos_mes():
    return render_template("volu_pontos_mes.html")

@relatorios_.route('/api/volu_pontos_mes')
def api_volu_pontos_mes():
    mes_str = request.args.get('mes')
    try:
        if mes_str:
            data_ref = datetime.strptime(mes_str, "%Y-%m")
        else:
            data_ref = date.today()

        _, ultimo_dia = monthrange(data_ref.year, data_ref.month)
        inicio, fim = date(data_ref.year, data_ref.month, 1), date(data_ref.year, data_ref.month, ultimo_dia)

        data = (
            db.session.query(Voluntarios.nome, func.count(Ponto.id))
            .filter(Ponto.horario.between(inicio, fim))
            .group_by(Voluntarios.nome)
            .order_by(Voluntarios.nome)
            .all()
        )

        chart_data = {
            "labels": [nome for nome, _ in data],
            "datasets": [{
                "label": "Pontos por voluntário no mês",
                "data": [int(qtd or 0) for _, qtd in data],
                "backgroundColor": "rgba(75, 192, 192, 0.6)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }]
        }

        return jsonify(chart_data)
    except Exception as e:
        print("Erro:", e)