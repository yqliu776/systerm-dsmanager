from exts import db
from datetime import date


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

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.adminname,
            'permission': self.permission
        }

    def __repr__(self):
        return '<User %s>' % self.adminname


class UserModel(db.Model):
    """
    用户 数据表 模型
    属性：id, username, email, tel, password, browse_history, search_history, purchase_history, click_history, favorite_products, social_media_interaction, cart_data, time_spent_on_products, age, gender, location
    """
    __tablename__ = 'user'

    # 用户id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    tel = db.Column(db.String(200))
    password = db.Column(db.String(200))

    # 用户搜索历史
    search_history = db.Column(db.String(1000))
    # 用户购买历史
    purchase_history = db.Column(db.Text())
    # 用户收藏的产品
    favorite_products = db.Column(db.String(1000))
    # 用户购物车数据
    cart_data = db.Column(db.String(1000))
    # 用户年龄
    age = db.Column(db.Integer)
    # 用户性别
    gender = db.Column(db.String(10))
    # 用户地理位置
    location = db.Column(db.String(200))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User> %s' % self.username


class ProductsModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(100), unique=True)
    product_name = db.Column(db.String(200))
    product_image_url = db.Column(db.String(500))
    original_price = db.Column(db.Float)
    discount_price = db.Column(db.Float)
    product_url = db.Column(db.String(500))
    category = db.Column(db.String(100))
    subcategory = db.Column(db.String(200))

    def __init__(self, product_id, product_name, product_image_url, original_price, discount_price, product_url, category, subcategory):
        self.product_id = product_id
        self.product_name = product_name
        self.product_image_url = product_image_url
        self.original_price = original_price
        self.discount_price = discount_price
        self.product_url = product_url
        self.category = category
        self.subcategory = subcategory
