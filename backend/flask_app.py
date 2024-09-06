from flask import Flask
from database.db import db
from flask_login import LoginManager
from backend.routes import auth_bp

def create_flask_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "your_default_secret_key"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

    # Inicializar banco de dados
    db.init_app(app)

    # Configurar LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Registrar rotas
    app.register_blueprint(auth_bp)

    return app
