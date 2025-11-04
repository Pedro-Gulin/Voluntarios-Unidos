from models.db import db
from flask_login import UserMixin
from models.user.roles import Role

class Users(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    role = db.relationship('Role', backref='users', lazy=True)

    @property
    def role_name(self):
        return self.role.name if self.role else "Sem função"

    def save_user(email, password, role_name):
        role = Role.get_single_role(role_name)
        user = Users(email=email, password=password, role_id=role.id)
        db.session.add(user)
        db.session.commit()
        
    def get_single_user(email):
        return Users.query.filter_by(email=email).first()
    
    def get_users():
        return Users.query.all()     