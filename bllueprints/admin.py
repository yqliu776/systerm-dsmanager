from flask import Blueprint, render_template, request, session, redirect, url_for
from models import AdminModel
from forms import AdminLoginForm, AdminAddForm
from werkzeug.security import check_password_hash, generate_password_hash
from exts import db
from sqlalchemy.sql import exists

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def index():
    return render_template('admin/index_admin.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Administrator login。
    :return:
    """
    if request.method == 'GET':
        return render_template('admin/login_admin.html')
    else:
        form = AdminLoginForm(request.form)
        if form.validate():
            adminname = form.adminname.data
            password = form.password.data
            admin = AdminModel.query.filter_by(adminname=adminname).first()
            if admin is None:
                error = 'NameError：There is no such administrator!'
                return render_template('admin/login_admin.html', error=error)
            else:
                # print(generate_password_hash(password))
                if admin and check_password_hash(admin.password, password):
                    session['admin_id'] = admin.id
                    session['permission'] = admin.permission
                    return redirect(url_for('admin.index'))
                else:
                    error = 'PassWorldError: The administrator password is incorrect!'
                    return render_template('admin/login_admin.html', error=error)
        else:
            error = 'FormatError: Please check your account or password format and try again!'
            return render_template('admin/login_admin.html', error=error)


@bp.route('/add_admin', methods=['GET', 'POST'])
def add_admin():
    """
    Add an administrator
    :return:
    """
    if request.method == 'GET':
        return render_template('admin/add_admin.html')
    else:
        if session.get('permission') != 0:
            error = 'PermissionError: The permissions are insufficient, please contact the super administrator'
            return render_template('admin/add_admin.html', error=error)
        else:
            form = AdminAddForm(request.form)
            if form.validate():
                adminname = form.adminname.data
                password = form.password.data
                permission = form.Permission.data
                scalar = db.session.query(exists().where(AdminModel.adminname == adminname))
                if scalar.scalar():
                    error = 'NameError: This administrator already exists！'
                    return render_template('admin/add_admin.html', error=error)
                else:
                    match permission:
                        case "SuperRoot":
                            permission = 0
                        case "NormalAdmin":
                            permission = 1
                        case "Observer":
                            permission = 2
                        case _:
                            error = 'PermissionError: Please select an administrator privilege level！'
                            return render_template('admin/add_admin.html', error=error)

                    hash_pwd = generate_password_hash(password)
                    admin = AdminModel(adminname=adminname, password=hash_pwd, permission=permission)
                    db.session.add(admin)
                    db.session.commit()
                    feedback = 'Added successfully！'
                    return render_template('admin/add_admin.html', feedback=feedback)
            else:
                error = 'FormatError: The account or password format is incorrect！ '
                return render_template('admin/add_admin.html', error=error)


@bp.route('/pop_admin', methods=['GET', 'POST'])
def pop_admin():
    pass
