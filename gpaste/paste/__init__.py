from flask import Flask

app = Flask(__name__)

import paste.views, paste.models
