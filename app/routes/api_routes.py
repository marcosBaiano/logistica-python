from flask import Blueprint
from flask import jsonify

api_bp = Blueprint('api', __name__)


@api_bp.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'logistica_bot'})
