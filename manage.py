from bllueprints import main_bp, admin_bp, user_bp, debug_bp


def bp_register(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(debug_bp)
