from flask import render_template, request, redirect, url_for
from hashids import Hashids
from paste import app, db
from paste.models import Post

hashids = Hashids(salt="change this string in production please")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['paste-content']
        p = Post(content=content)
        db.session.add(p)
        db.session.commit()

        id_hash = hashids.encode(p.id)
        print(id_hash)

        return redirect(url_for('content_page', id_hash=id_hash))

    return render_template('index.html')

@app.route('/<string:id_hash>')
def content_page(id_hash):
    q = Post.query.get(hashids.decode(id_hash))

    return render_template('content.html', content=q.content)
