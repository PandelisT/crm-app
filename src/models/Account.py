from main import db
from datetime import datetime


class Account(db.Model):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(), nullable=False)
    industry = db.Column(db.String(), nullable=False)
    website = db.Column(db.String(), nullable=False)
    created_on = db.Column(db.DateTime(), nullable=False, default = datetime.now)
    is_active = db.Column(db.Boolean(), default=True)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<User {self.company_name}>"