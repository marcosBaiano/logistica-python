from app.database.models import Intencao
from app.database.db import db


class IntentService:

    @staticmethod
    def listar_ativas():
        return Intencao.query.filter_by(ativo=True).all()

    @staticmethod
    def criar(nome, palavras_chave, resposta, contexto=None):
        intencao = Intencao(
            nome=nome,
            palavras_chave=palavras_chave,
            resposta=resposta,
            contexto=contexto,
            ativo=True
        )
        db.session.add(intencao)
        db.session.commit()
        return intencao
