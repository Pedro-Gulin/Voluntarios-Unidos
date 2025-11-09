from models.db import db
from models.voluntarios.voluntarios import Voluntarios
from datetime import datetime

class Ponto(db.Model):
    __tablename__ = 'ponto'

    id = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('voluntarios.id'), nullable=False)
    nome_voluntario = db.Column(db.String(250), nullable=True)
    cpf_voluntario = db.Column(db.String(14), nullable=False)
    numero_carteirinha = db.Column(db.String(50), nullable=True)
    horario = db.Column(db.DateTime, nullable=False, default=datetime.now)

    voluntario = db.relationship('Voluntarios', backref='pontos', lazy=True)

    from datetime import datetime

    @staticmethod
    def bater_ponto(cpf_voluntario, numero_carteirinha, horario=None):
        voluntario = Voluntarios.query.filter_by(cpf=cpf_voluntario).first()

        if not voluntario:
            raise ValueError("Voluntário com esse CPF não encontrado.")

        # se vier string do processar_tag, converte para datetime
        if isinstance(horario, str):
            try:
                horario = datetime.strptime(horario, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                horario = datetime.now()

        # se não vier nada, usa o horário atual
        if horario is None:
            horario = datetime.now()

        ponto = Ponto(
            id_voluntario=voluntario.id,
            nome_voluntario=voluntario.nome,
            cpf_voluntario=voluntario.cpf,
            numero_carteirinha=numero_carteirinha,
            horario=horario  # agora sim é um datetime real
        )

        db.session.add(ponto)
        db.session.commit()


    @staticmethod
    def buscar_ponto(cpf_voluntario):
        return Ponto.query.filter_by(cpf_voluntario=cpf_voluntario).all()

    @staticmethod
    def buscar_ponto_id(id):
        return Ponto.query.filter_by(id=id).first()

    @staticmethod
    def buscar_pontos():
        return Ponto.query.all()
