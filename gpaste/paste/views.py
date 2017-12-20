from paste import app, db
from paste.models import Post

@app.route('/')
def index():
    return 'Hello world!'
