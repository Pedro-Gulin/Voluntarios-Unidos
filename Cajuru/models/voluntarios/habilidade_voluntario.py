from models.db import db
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.habilidades import Habilidades

class Habilidade_voluntario(db.Model):
    __tablename__ = 'habilidade_voluntario'
    
    id = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('voluntarios.id'), nullable=False)
    nome_voluntario = db.Column(db.String(250), nullable=True)
    id_habilidade = db.Column(db.Integer, db.ForeignKey('habilidades.id', ondelete='CASCADE'), nullable=False)
    nome_habilidade = db.Column(db.String(250), nullable=True)
    
    voluntario = db.relationship('Voluntarios', backref='habilidade_voluntario', lazy=True)
    habilidade = db.relationship('Habilidades', backref='habilidade_voluntario', lazy=True)
    
    @staticmethod
    def save_habilidade_voluntario(id_voluntario, id_habilidade, nome_voluntario, nome_habilidade):
        habilidade_voluntario = Habilidade_voluntario(id_voluntario = id_voluntario, nome_voluntario = nome_voluntario, id_habilidade = id_habilidade, nome_habilidade = nome_habilidade)
        
        db.session.add(habilidade_voluntario)
        db.session.commit()
        
    @staticmethod
    def buscar_habilidade_voluntario():
        return Habilidade_voluntario.query.all()
    
    @staticmethod
    def buscar_habilidade_voluntario_especifico(id_voluntario):
        return Habilidade_voluntario.query.filter_by(id_voluntario = id_voluntario).first()
    
    @staticmethod
    def buscar_habilidade_por_idhabilidade(id_habilidade):
        return Habilidade_voluntario.query.filter_by(id_habilidade = id_habilidade).first()