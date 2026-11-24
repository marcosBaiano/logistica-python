from app.database.models import Chamado
from app.database.db import db


class TicketService:

    @staticmethod
    def criar(usuario_id, assunto, descricao):
        chamado = Chamado(usuario_id=usuario_id, assunto=assunto, descricao=descricao)
        db.session.add(chamado)
        db.session.commit()
        return chamado

    @staticmethod
    def listar():
        return Chamado.query.order_by(Chamado.id.desc()).all()
