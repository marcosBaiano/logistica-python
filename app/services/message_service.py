from app.database.models import Mensagem


class MessageService:

    @staticmethod
    def listar_por_usuario(usuario_id):
        return Mensagem.query.filter_by(usuario_id=usuario_id).order_by(Mensagem.criado_em.asc()).all()
