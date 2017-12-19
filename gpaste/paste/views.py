from paste import app
from paste import models

@app.route('/')
def index():
    return 'Hello world!'
