from flask import render_template, request, redirect, url_for, abort, session, Response
import os
from hashids import Hashids
from datetime import datetime
from paste import app, db
from paste.forms import languageBox, expirationDate, expiryDateAndType
from paste.models import Post

hashids = Hashids(salt="change this string in production please")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['paste-content']
        language = request.form['language']
        expiration = request.form['expiration']
        if language not in set(languageBox):
            language = 'nohighlight'

        if content.isspace():
            return redirect(url_for('index'))

        burn, expiry = expiryDateAndType(expiration)
        p = Post(content=content, language_highlight=language,
                 expiry_date=expiry, burn_after_reading=burn)
        db.session.add(p)
        db.session.commit()

        id_hash = hashids.encode(p.id)
        try: session['history']
        except KeyError: session['history'] = []
        postHistory = session['history']
        postHistory.append(id_hash)
        session['history'] = postHistory

        return redirect(url_for('content_page', id_hash=id_hash))

    return render_template('index.html', languages=languageBox, expiration=expirationDate)

@app.route('/<string:id_hash>')
def content_page(id_hash):
    deletePermission = False
    try:
        plain_id = hashids.decode(id_hash)[0]
    except IndexError:
        abort(404)
    q = Post.query.get_or_404(plain_id)

    if q.expiry_date < datetime.now():
        db.session.delete(q)
        db.session.commit()
        abort(404)

    try:
        if id_hash in set(session['history']):
            deletePermission = True
            
            if q.burn_after_reading and q.viewed:
                db.session.delete(q)
                db.session.commit()
                abort(404)
        else:
            if q.burn_after_reading and q.viewed:
                db.session.delete(q)
                db.session.commit()
                abort(404)
            elif q.burn_after_reading and not q.viewed:
                q.viewed = True
                db.session.commit()
            
    except KeyError:
        if q.burn_after_reading and q.viewed:
            db.session.delete(q)
            db.session.commit()
            abort(404)
        elif q.burn_after_reading and not q.viewed:
            q.viewed = True
            db.session.commit()

    return render_template('content.html', pasteData=q.content, pasteHighlight=q.language_highlight, permission=deletePermission, expiryDate=q.expiry_date)

@app.route('/<string:id_hash>/d')
def delete(id_hash):
    try:
        if id_hash in set(session['history']):
            plain_id = hashids.decode(id_hash)[0]
            q = Post.query.get_or_404(plain_id)
            db.session.delete(q)
            db.session.commit()

            session['history'].remove(id_hash)

            return redirect(url_for('index'))

        return redirect(url_for('content_page', id_hash=id_hash))

    except KeyError:
        return redirect(url_for('content_page', id_hash=id_hash))

@app.route('/<string:id_hash>/r')
def raw(id_hash):
    try:
        plain_id = hashids.decode(id_hash)[0]
    except IndexError:
        abort(404)
    q = Post.query.get_or_404(plain_id)

    if q.expiry_date < datetime.now():
        db.session.delete(q)
        db.session.commit()
        abort(404)

    try:
        if id_hash in set(session['history']):
            if q.burn_after_reading and q.viewed:
                db.session.delete(q)
                db.session.commit()
                abort(404)
        else:
            if q.burn_after_reading and q.viewed:
                db.session.delete(q)
                db.session.commit()
                abort(404)

            elif q.burn_after_reading and not q.viewed:
                q.viewed = True
                db.session.commit()
            
    except KeyError:
        if q.burn_after_reading and q.viewed:
            db.session.delete(q)
            db.session.commit()
            abort(404)
        elif q.burn_after_reading and not q.viewed:
            q.viewed = True
            db.session.commit()

    return Response(q.content, mimetype='text/plain')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
