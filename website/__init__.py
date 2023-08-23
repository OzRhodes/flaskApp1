from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'




def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'A secret key but will be removed on a production'
    
    # config database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # models are in models.py

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')

    app.register_blueprint(auth, url_prefix='/')

    import .models 


    return app