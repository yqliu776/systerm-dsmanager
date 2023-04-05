from flask import Blueprint, render_template, session, redirect, url_for

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def index():
    if 'user_id' in session:
        is_logged_in = True
    else:
        is_logged_in = False
    return render_template('user/index_user.html', is_logged_in=is_logged_in)


@bp.route('/login')
def login():
    return render_template('user/login_user.html')


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('permission', None)
    session.pop('name', None)
    return redirect(url_for('user.index'))


@bp.route('/register')
def register():
    return render_template('user/register.html')
