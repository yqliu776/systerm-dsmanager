from flask import Blueprint, render_template, session, redirect, url_for, request
from werkzeug.security import check_password_hash

from forms import UserLoginForm
from models import UserModel

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def index():
    if 'user_id' in session:
        is_logged_in = True
    else:
        is_logged_in = False
    return render_template('user/index_user.html', is_logged_in=is_logged_in)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login。
    :return:
    """
    if request.method == 'GET':
        return render_template('user/login_user.html')
    else:
        form = UserLoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if user is None:
                error = '用户不存在！'
                return render_template('user/login_user.html', error=error)
            else:
                # print(generate_password_hash(password))
                if user and check_password_hash(user.password, password):
                    session['admin_id'] = user.id
                    session['name'] = user.username
                    return redirect(url_for('user.index'))
                else:
                    error = '账户密码错误！'
                    return render_template('user/login_user.html', error=error)
        else:
            error = '帐号或密码格式不正确，请重新输入。'
            return render_template('user/login_user.html', error=error)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('name', None)
    return redirect(url_for('user.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('user/register_user.html')
