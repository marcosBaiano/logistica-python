from app.database.models import Sessao
from app.database.db import db


class ContextManager:

    @staticmethod
    def salvar(usuario_id, contexto, etapa):
        sessao = Sessao.query.filter_by(usuario_id=usuario_id).first()
        if not sessao:
            sessao = Sessao(usuario_id=usuario_id)
        sessao.contexto = contexto
        sessao.etapa = etapa
        db.session.add(sessao)
        db.session.commit()

    @staticmethod
    def obter(usuario_id):
        return Sessao.query.filter_by(usuario_id=usuario_id).first()
