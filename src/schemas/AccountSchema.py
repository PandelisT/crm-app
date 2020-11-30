from main import ma
from models.Account import Account
from marshmallow.validate import Length, Email

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account

    website = ma.String(required=True, validate=Length(min=4))
    company_name = ma.String(required=True, validate=Length(min=4))


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)