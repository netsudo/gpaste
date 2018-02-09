from paste import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=True)
    language_highlight = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expiry_date = db.Column(db.DateTime, nullable=False)

    burn_after_reading = db.Column(db.Boolean, nullable=False, default=False)
    viewed = db.Column(db.Boolean, nullable=False, default=False)

    salt = db.Column(db.Binary, nullable=True)
    encrypted_content = db.Column(db.LargeBinary, nullable=True)

    def __repr__(self):
        return '<Date %r> <Content %r>' % (self.pub_date, self.content)
