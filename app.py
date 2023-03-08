from flask import Flask, url_for
from flask_migrate import Migrate
from exts import db
from manage import bp_register
from models import AdminModel, UserModel, ProductsModel
import config


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

bp_register(app)


if __name__ == '__main__':
    app.run(host='192.168.1.10',port=5000)
