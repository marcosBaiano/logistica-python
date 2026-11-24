from app.database.db import db
from datetime import datetime


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    telefone = db.Column(db.String(30))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)


class Intencao(db.Model):
    __tablename__ = 'intencoes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    palavras_chave = db.Column(db.Text)
    resposta = db.Column(db.Text)
    contexto = db.Column(db.String(100))
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)


class Mensagem(db.Model):
    __tablename__ = 'mensagens'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    mensagem = db.Column(db.Text)
    resposta = db.Column(db.Text)
    intencao_detectada = db.Column(db.String(100))
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)


class Pedido(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)
    codigo_rastreio = db.Column(db.String(100))
    cliente_id = db.Column(db.Integer)
    status_entrega = db.Column(db.String(100))
    localizacao_atual = db.Column(db.String(255))


class HistoricoRastreio(db.Model):
    __tablename__ = 'historico_rastreio'

    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer)
    status = db.Column(db.String(255))
    localizacao = db.Column(db.String(255))
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow)


class Chamado(db.Model):
    __tablename__ = 'chamados'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    assunto = db.Column(db.String(255))
    descricao = db.Column(db.Text)
    status = db.Column(db.String(50), default='aberto')


class Sessao(db.Model):
    __tablename__ = 'sessoes'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    contexto = db.Column(db.String(255))
    etapa = db.Column(db.String(100))
