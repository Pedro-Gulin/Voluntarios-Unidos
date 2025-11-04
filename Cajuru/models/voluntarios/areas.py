from sqlalchemy import select
from models import db

class Areas(db.Model):
    __tablename__ = 'areas'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=True)
    quantidade_horas = db.Column(db.Integer)
    descricao = db.Column(db.String(250))
    
    def salvar_area(nome,quantidade_horas, descricao):
        
        area = Areas(nome = nome, quantidade_horas = quantidade_horas, descricao = descricao)
        
        db.session.add(area)
        db.session.commit()
        
    def buscar_areas():
        return Areas.query.all()
        
    def buscar_area_especifica(nome):
        return Areas.query.filter_by(nome = nome).first()
    
    def buscar_area_id_por_nome(nome):
        area = Areas.query.filter_by(nome = nome).first()
        return area.id
    
    def buscar_area_por_id(id_area):
        area = select(Areas.nome).where(Areas.id == id_area)
        return db.session.execute(area).scalar_one_or_none()