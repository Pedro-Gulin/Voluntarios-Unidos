from models.db import db
from models.voluntarios.voluntarios import Voluntarios

class nucleo_voluntariado(db.Model):
    __tablename__ = 'nucleo_voluntariado'
    
    id = db.Column(db.Integer, primary_key=True)
    id_voluntario = db.Column(db.Integer, db.ForeignKey('voluntarios.id'), nullable=False)
    nome_voluntario = db.Column(db.String(120), nullable=True)
    domingo = db.Column(db.String(50), nullable=True)
    segunda_feira = db.Column(db.String(50), nullable=True)
    terca_feira = db.Column(db.String(50), nullable=True)
    quarta_feira = db.Column(db.String(50), nullable=True)
    quinta_feira = db.Column(db.String(50), nullable=True)
    sexta_feira = db.Column(db.String(50), nullable=True)
    sabado = db.Column(db.String(50), nullable=True)
    
    voluntario = db.relationship('Voluntarios', backref='nucleo_voluntariado', lazy=True)
    
    def save_nucleo_voluntario(id_voluntario, nome_voluntario, domingo, segunda_feira, terca_feira, quarta_feira, quinta_feira, sexta_feira, sabado):
        
        nucleo_voluntariados = nucleo_voluntariado(id_voluntario = id_voluntario, nome_voluntario = nome_voluntario, domingo = domingo, segunda_feira = segunda_feira, terca_feira = terca_feira, quarta_feira = quarta_feira, quinta_feira = quinta_feira, sexta_feira = sexta_feira, sabado = sabado)
        
        db.session.add(nucleo_voluntariados)
        db.session.commit()
        
    def buscar_nucleo_voluntariado_especifico(id_voluntario):
        return nucleo_voluntariado.query.filter_by(id_voluntario = id_voluntario).first()
    
    def buscar_nucleo_voluntarios():
        return nucleo_voluntariado.query.all()