from models.db import db
from models.voluntarios.voluntarios import Voluntarios
from models.voluntarios.areas import Areas

class Escala(db.Model):
    __tablename__ = 'escala'
     
    id = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('voluntarios.id'), nullable=False)
    nome_voluntario = db.Column(db.String(250), nullable=True)
    id_area = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    nome_area = db.Column(db.String(250), nullable=True)
    data = db.Column(db.String(20), nullable=False)
    turno = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20))
    
    voluntario = db.relationship('Voluntarios', backref='escala', lazy=True)
    area = db.relationship('Areas', backref='escala', lazy=True)
    
    def salvar_escala(id_voluntario, nome_voluntario, id_area, nome_area, data, turno, status):
        escala = Escala(id_voluntario = id_voluntario, nome_voluntario = nome_voluntario, id_area = id_area, nome_area = nome_area, data = data, turno = turno, status = status)
        
        db.session.add(escala)
        db.session.commit()
    
    def buscar_escala_especifica(id_voluntario):
        return Escala.query.filter_by(id_voluntario = id_voluntario).first()
    
    def buscar_escalas():
        return Escala.query.all()
    
    def buscar_escala_id_por_nome(nome_voluntario):
        escala = Escala.query.filter_by(nome_voluntario = nome_voluntario).first()
        return escala.id
    
    def buscar_escala_area_por_nome(nome_area):
        escala = Escala.query.filter_by(nome_area = nome_area).first()
        return escala.id