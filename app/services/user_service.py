from app.database.models import Usuario
from app.database.db import db


class UserService:

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def criar(nome, email, telefone=None):
        usuario = Usuario(nome=nome, email=email, telefone=telefone)
        db.session.add(usuario)
        db.session.commit()
        return usuario
