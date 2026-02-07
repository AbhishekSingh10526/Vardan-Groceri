from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        import models
        import routes
        db.create_all()
        # create admin if admin does not exist
        admin = models.User.query.filter_by(username='admin').first()
        if not admin:
            admin = models.User(username='admin', password='admin', name='admin', is_admin=True)
            db.session.add(admin)
            db.session.commit()
    
    return app
