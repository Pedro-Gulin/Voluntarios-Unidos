from models.db import db 

class Ficha(db.Model):
    
    __tablename__ = 'ficha'
    
    id = db.Column(db.Integer, primary_key=True)
    numero_ficha = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date)
    voluntario = db.Column(db.String(250))
    solicitante = db.Column(db.String(250))
    paciente = db.Column(db.String(250))