from base import db

class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(128), index=True, unique=True)
    answer = db.Column(db.String(128))

    def __repr__(self):
        return '<Question {}>'.format(self.question)