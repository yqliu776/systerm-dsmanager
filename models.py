from exts import db


class AdminModel(db.Model):
    """
    管理员 数据表 模型
    属性：id， adminname， password······
    """
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adminname = db.Column(db.String(200))
    password = db.Column(db.String(200))
    permission = db.Column(db.Integer, primary_key=False, autoincrement=False)

    def __init__(self, adminname, password, permission):
        """
        To fix error:__init__() takes 1 positional argument but 3 were given
        :param adminname:
        :param password:
        """
        self.adminname = adminname
        self.password = password
        self.permission = permission

    def __repr__(self):
        return '<User %s>' % self.adminname


class UserModel(db.Model):
    """
    用户 数据表 模型
    属性：id， name，email, tel, pwd, ······
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(200))
    password = db.Column(db.String(200))

    def __int__(self, username, email, tel, password):
        self.username = username
        self.email = email
        self.tel = tel
        self.password = password

    def __repr__(self):
        return '<User> %s' % self.username


class ProductsModel(db.Model):
    """
    商品 数据表 模型
    属性：id， name······
    """
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productname = db.Column(db.String(200))
