from flask import Blueprint
from flask import render_template
from flask import request
from flask import jsonify

from app.chatbot.engine import ChatEngine

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/')
def home():
    return render_template('index.html')


@chat_bp.route('/chat', methods=['POST'])
def chat():
    dados = request.get_json() or {}
    mensagem = dados.get('mensagem')
    usuario_id = dados.get('usuario_id', 1)

    if not mensagem:
        return jsonify({'resposta': 'Por favor, envie uma mensagem.'}), 400

    resposta = ChatEngine.processar(usuario_id, mensagem)

    return jsonify(resposta)
