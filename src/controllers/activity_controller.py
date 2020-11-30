from flask import Blueprint, abort, jsonify, request
from schemas.ActivitySchema import activity_schema, activities_schema
from models.Account import Account
from models.User import User
from models.Activity import Activity
from main import db, bcrypt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from datetime import timedelta


activity = Blueprint("activity", __name__, url_prefix="/activity")


@activity.route("/", methods=["POST"])
@jwt_required
def new_account():
    user_id = get_jwt_identity()
    user_account = Account.query.get(user_id)
    if not user_account:
        return abort(401, description="Invalid user")
    
    activity_fields = activity_schema.load(request.json)
    
    new_activity = Activity()
    new_activity.description = activity_fields["description"]
    new_activity.created_by = user_account.id

    user_account.activity_id.append(new_activity)
        
    db.session.add(new_activity)
    db.session.commit()
        
    return jsonify(activity_schema.dump(new_activity))
