from flask import render_template
from paste import app, db
from paste.models import Post

@app.route('/')
def index():
    return render_template('index.html')
