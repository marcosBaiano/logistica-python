from app.chatbot.intent_detector import IntentDetector
from app.chatbot.fallback import Fallback
from app.chatbot.context_manager import ContextManager
from app.database.models import Mensagem
from app.database.db import db


class ChatEngine:

    @staticmethod
    def processar(usuario_id, texto):
        intencao = IntentDetector.detectar(texto)

        if intencao:
            resposta = intencao.resposta
            nome_intencao = intencao.nome
            contexto = intencao.contexto
        else:
            resposta = Fallback.resposta()
            nome_intencao = 'fallback'
            contexto = None

        if contexto:
            ContextManager.salvar(usuario_id, contexto, nome_intencao)

        mensagem = Mensagem(
            usuario_id=usuario_id,
            mensagem=texto,
            resposta=resposta,
            intencao_detectada=nome_intencao
        )

        db.session.add(mensagem)
        db.session.commit()

        return {
            'resposta': resposta,
            'intencao': nome_intencao
        }
