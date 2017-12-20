from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:password@localhost/Paste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import paste.views, paste.models
