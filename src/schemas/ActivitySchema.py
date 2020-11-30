from main import ma
from models.Activity import Activity
from marshmallow.validate import Length, Email

class ActivitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Activity


activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)