from init import app, db

class Posts(db.Model):
    __tablename__='Posts'
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.BigInteger)
    header = db.Column(db.String(120))
    signature = db.Column(db.String(120))
    body = db.Column(db.String(1000))


    def __init__(self, header, signature, body, url_id):
       self.header = header
       self.signature = signature
       self.body = body
       self.url_id = url_id
