from flask import render_template, request, redirect, url_for, abort
from hashids import Hashids
from paste import app, db
from paste.languages import languageBox
from paste.models import Post

hashids = Hashids(salt="change this string in production please")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['paste-content']
        language = request.form['language']
        if language not in set(languageBox):
            abort(404)

        p = Post(content=content, language_highlight=language)
        db.session.add(p)
        db.session.commit()

        id_hash = hashids.encode(p.id)

        return redirect(url_for('content_page', id_hash=id_hash))

    return render_template('index.html', languages=languageBox)

@app.route('/<string:id_hash>')
def content_page(id_hash):
    try:
        plain_id = hashids.decode(id_hash)[0]
    except IndexError:
        abort(404)
    q = Post.query.get_or_404(plain_id)

    return render_template('content.html', pasteData=q.content, pasteHighlight=q.language_highlight)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
