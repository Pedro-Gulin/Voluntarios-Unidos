from sqlalchemy import select
from models.db import db
from datetime import datetime

class Voluntarios(db.Model):
    __tablename__ = 'voluntarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=True)
    data_nasc = db.Column(db.Date, nullable=True)
    local_nasc = db.Column(db.String(100), nullable=True)
    rg = db.Column(db.String(14), unique=True, nullable=True)
    cpf = db.Column(db.String(11), unique=True, nullable=True)
    estado_civil = db.Column(db.String(20), nullable=True)
    nome_conjuge = db.Column(db.String(120), nullable=True)
    nome_pai = db.Column(db.String(120), nullable=True)
    nome_mae = db.Column(db.String(120), nullable=True)
    endereco = db.Column(db.String(120), nullable=True)
    cep = db.Column(db.String(20), nullable=True)
    telefone = db.Column(db.String(15), nullable=True)
    religiao = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    escolaridade = db.Column(db.String(50), nullable=True)
    local_trabalho = db.Column(db.String(100), nullable=True)
    ocupacao = db.Column(db.String(100), nullable=True)
    tratamento = db.Column(db.String(120), nullable=True)
    transporte = db.Column(db.String(50), nullable=True)
    sab_volun = db.Column(db.String(120), nullable=True)
    trab_vol = db.Column(db.String(120), nullable=True)
    grupo_vol = db.Column(db.String(250), nullable=True)
    como_contri = db.Column(db.String(250), nullable=True)
    musical = db.Column(db.String(120), nullable=True)
    alimentacao = db.Column(db.String(50), nullable=True)
    data_vinculo = db.Column(db.Date, nullable=True)
    codigo_carteirinha = db.Column(db.String(50), nullable=True)
    
    def salvar_voluntario(nome, data_nasc, local_nasc, rg, cpf, estado_civil, nome_conjuge,
                                 nome_pai, nome_mae, endereco, cep, telefone, religiao, email, escolaridade, local_trabalho, ocupacao, tratamento, transporte, sab_volun, trab_vol , grupo_vol, como_contri, musical, alimentacao):
    
        
        voluntario = Voluntarios(nome = nome, data_nasc = data_nasc, local_nasc = local_nasc, rg = rg, cpf = cpf, estado_civil = estado_civil, nome_conjuge = nome_conjuge,
                                 nome_pai = nome_pai, nome_mae = nome_mae, endereco = endereco, cep = cep, telefone = telefone, religiao = religiao, email = email, escolaridade = escolaridade, local_trabalho = local_trabalho, ocupacao = ocupacao, tratamento = tratamento, transporte = transporte, sab_volun = sab_volun, trab_vol  = trab_vol, grupo_vol = grupo_vol, como_contri = como_contri, musical = musical, alimentacao = alimentacao)
        
        db.session.add(voluntario)
        db.session.commit()
        
    @staticmethod
    def buscar_voluntario(nome):
        return Voluntarios.query.filter_by(nome=nome).first()

    @staticmethod
    def buscar_vol_id(id_voluntario):
        volu = select(Voluntarios.nome).where(Voluntarios.id == id_voluntario)
        return db.session.execute(volu).scalar_one_or_none()

    @staticmethod
    def buscar_por_tag(tag):
        return Voluntarios.query.filter_by(codigo_carteirinha=tag).first()

    @staticmethod
    def buscar_por_cpf(cpf):
        return Voluntarios.query.filter_by(cpf=cpf).first()
    
    @staticmethod
    def buscar_id_por_cpf(cpf):
        voluntario = Voluntarios.query.filter_by(cpf = cpf).first()
        return voluntario.id
    
    @staticmethod
    def buscar_nome_por_id(id):
        voluntario = Voluntarios.query.filter_by(id = id).first()
        return voluntario.nome

    @staticmethod
    def associar_tag_ao_voluntario(tag):
        voluntario_sem_tag = Voluntarios.query.filter(
            (Voluntarios.codigo_carteirinha == None) | (Voluntarios.codigo_carteirinha == "")
        ).first()
        if voluntario_sem_tag:
            voluntario_sem_tag.codigo_carteirinha = tag
            db.session.commit()
            return voluntario_sem_tag
        else:
            return None

    @staticmethod
    def associar_tag_por_cpf(cpf, tag):
        voluntario = Voluntarios.buscar_por_cpf(cpf)
        if voluntario:
            voluntario.codigo_carteirinha = tag
            db.session.commit()
            return voluntario
        return None
    
    @staticmethod
    def associar_tag(cpf, codigo_carteirinha):
        voluntario = Voluntarios.query.filter_by(cpf = cpf).first()
        if voluntario:
            voluntario.codigo_carteirinha = codigo_carteirinha
            
    @staticmethod
    def buscar_voluntarios():
        return Voluntarios.query.all()