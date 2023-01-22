from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def index():
    return 'user_index'


@bp.route('/login')
def login():
    return 'user_login'
