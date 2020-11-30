from flask import Blueprint, abort, jsonify, request
from schemas.AccountSchema import account_schema, accounts_schema
from models.Account import Account
from models.User import User
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta


account = Blueprint("account", __name__, url_prefix="/account")


@account.route("/", methods=["POST"])
@jwt_required
def new_account():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    account_fields = account_schema.load(request.json)
    
    new_account = Account()
    new_account.company_name = account_fields["company_name"]
    new_account.website = account_fields["website"]
    new_account.industry = account_fields["industry"]
    new_account.is_active= account_fields["is_active"]
        
    user.account_id.append(new_account)
        
    db.session.add(new_account)
    db.session.commit()
        
    return jsonify(account_schema.dump(new_account))
