from models import db
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.areas import Areas
from datetime import datetime

class Atuacao(db.Model):
    __tablename__ = 'atuacao'
    
    id = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('voluntarios.id'), nullable=False)
    nome_voluntario = db.Column(db.String(120), nullable=False)
    id_area = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    nome_area = db.Column(db.String(120), nullable=False)
    horas = db.Column(db.Integer)
    valor_hora = db.Column(db.Float)
    descricao = db.Column(db.String(250))
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    
    area = db.relationship('Areas', backref='atuacoes', lazy=True)
    voluntario = db.relationship('Voluntarios', backref='atuacoes', lazy=True)
    
    @staticmethod
    def salvar_atuacao(id_area, id_voluntario, horas, valor_hora, descricao, data_inicio, data_fim):
        voluntario = Voluntarios.query.get(id_voluntario)
        area = Areas.query.get(id_area)
        
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
        data_fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

        if not voluntario or not area:
            raise ValueError("Voluntário ou área não encontrados.")

        atuacao = Atuacao(
            id_voluntario=id_voluntario,
            nome_voluntario=voluntario.nome,
            id_area=id_area,
            nome_area=area.nome,
            horas=horas,
            valor_hora = valor_hora,
            descricao=descricao,
            data_inicio=data_inicio,
            data_fim=data_fim
        )
        
        db.session.add(atuacao)
        db.session.commit()
    
    @staticmethod
    def buscar_atuacoes():
        return Atuacao.query.all()
        
    @staticmethod
    def buscar_atuacao_voluntario(nome_voluntario):
        return Atuacao.query.filter_by(nome_voluntario=nome_voluntario).first()