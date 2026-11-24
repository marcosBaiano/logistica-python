class LogService:

    @staticmethod
    def registrar(evento, detalhe=None):
        print(f"[LOG] {evento}: {detalhe}")
