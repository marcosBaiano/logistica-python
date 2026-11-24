from app.database.models import Intencao


class IntentDetector:

    @staticmethod
    def detectar(texto):
        texto = texto.lower()
        intencoes = Intencao.query.filter_by(ativo=True).all()

        for intencao in intencoes:
            palavras = intencao.palavras_chave.split(',') if intencao.palavras_chave else []
            for palavra in palavras:
                if palavra.strip().lower() in texto:
                    return intencao

        return None
