from app.database.models import Pedido


class TrackingService:

    @staticmethod
    def buscar_pedido(codigo):
        return Pedido.query.filter_by(codigo_rastreio=codigo).first()
