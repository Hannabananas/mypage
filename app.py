from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Factory function ta avoid cyclic imports
class Loginmaneger:
    pass


class Loginmanager:
    pass


class LoginManager:
    pass


def create_app():
    app = Flask(__name__)
    
    # Secret key to flask
    app.config['SECRET_KEY'] = '123secret'
    # configure with database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    
    

    db.init_app(app)
    
    # handle flask-login stuff
    
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from models import User
        return User.query.filter_by(id=user_id).first()

    from blueprint.open import bp_open
    app.register_blueprint(bp_open)

    from blueprint.user import bp_user
    app.register_blueprint(bp_user)

    return app
