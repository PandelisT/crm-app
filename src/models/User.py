from main import db
from models.Account import Account

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    account_id = db.relationship(Account, backref="user", uselist=True)

    def __repr__(self):
        return f"<User {self.email}>"