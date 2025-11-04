from models.db import db
from models.voluntarios.voluntarios import Voluntarios

class Habilidades(db.Model):
    __tablename__ = 'habilidades'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(250), nullable=True)
    
    def salvar_habilidade(nome, descricao):
        
        habilidade = Habilidades(nome = nome, descricao = descricao)
        
        db.session.add(habilidade)
        db.session.commit()
        
    def buscar_habilidades():
        return Habilidades.query.all()
    
    def buscar_habilidade_especifica(nome):
        return Habilidades.query.filter_by(nome = nome).first()
    
    def buscar_habilidade_nome_id(nome):
        habilidade = Habilidades.query.filter_by(nome = nome).first()
        return habilidade.id if habilidade else None