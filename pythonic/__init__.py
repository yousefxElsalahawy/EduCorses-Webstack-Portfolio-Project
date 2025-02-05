from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap


app = Flask(__name__)

app.config[
    "SECRET_KEY"
] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)


ckeditor = CKEditor(app)


# CKEditor config
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_CODE_THEME'] = 'monokai_sublime'
app.config['CKEDITOR_ENABLE_CODESNIPPET'] = True
app.config['CKEDITOR_EXTRA_PLUGINS'] = ['youtube', 'codesnippet']


bootstrap = Bootstrap(app) 

login_manager.login_view = "login"
login_manager.login_message_category = "info"
from pythonic import routes
