from flask import Blueprint
from flask import jsonify

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def dashboard():
    return jsonify({'message': 'Painel administrativo do Bot Logístico'}), 200
