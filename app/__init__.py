from flask import Flask
from flask_login import LoginManager
from .auth import load_user

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.secret_key = '21!nov1996'

    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from .routes import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app