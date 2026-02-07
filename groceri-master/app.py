from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Use an absolute path for the SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite3')
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models
import routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # create admin if admin does not exist
        admin = models.User.query.filter_by(username='admin').first()
        if not admin:
            admin = models.User(username='admin', password='admin', name='admin', is_admin=True)
            db.session.add(admin)
            db.session.commit()
    app.run(host='0.0.0.0', port=5000)
