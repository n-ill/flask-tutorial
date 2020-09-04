from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#key created by secrets module using secrets.token_hex(16) - 16 is num of bytes
app.config['SECRET_KEY'] = 'fe225f22ad6157b6c1dae8f79c359bdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #/// is relative path of current file - so created in this project folder
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #login is the route's method name
login_manager.login_message_category = 'info'

from flaskblog import routes # put down here to avoid circular imports