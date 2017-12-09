from init import app, db

class Post(db.Model):
    __tablename__='Post'
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.BigInteger)
    user_hash = db.Column(db.String(150))
    header = db.Column(db.String(120))
    signature = db.Column(db.String(120))
    body = db.Column(db.String(1000))


    def __init__(self, header, signature, body, url_id, user_hash):
       self.header = header
       self.signature = signature
       self.body = body
       self.url_id = url_id
       self.user_hash = user_hash
