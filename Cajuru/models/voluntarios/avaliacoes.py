from models.db import db
from models.voluntarios.voluntarios import Voluntarios

class Avaliacoes(db.Model):
    __tablename__ = 'avaliacoes'
    
    id = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('voluntarios.id'), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    nota = db.Column(db.Float, nullable=False)
    comentario = db.Column(db.String(250), nullable=True)
    
    voluntario = db.relationship('Voluntarios', backref='avaliacoes', lazy=True)