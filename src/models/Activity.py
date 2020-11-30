from main import db
from datetime import datetime


class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("accounts.id"), nullable=False)

    def __repr__(self):
        return f"<User {self.id}>"