class ConversationFlow:

    @staticmethod
    def seguir_fluxo(contexto, mensagem):
        if contexto == 'rastreio':
            return 'Por favor, informe o código de rastreio para que eu possa localizar seu pedido.'
        return None
