from marshmallow import validate, Schema, fields,post_load

from orm import Edit,Note,Allow,engine,User


class User_valid(Schema):
    id = fields.Integer()
    email = fields.String(validate=validate.Email())
    username = fields.String(required =True)
    firstName = fields.String()
    lastName = fields.String()
    password = fields.String()
    phone = fields.String()
    userRole = fields.Integer()

    @post_load
    def get_user(self,data,**kwargs):
        return User(**data)

class Note_valid(Schema):
    id = fields.Integer()
    tag = fields.String()
    text = fields.String()
    numbofEditors = fields.Integer(validate=validate.Range(min=1, max=4))

    @post_load
    def get_note(self,data,**kwargs):
        return Note(**data)

class Edit_valid(Schema):
    id = fields.Integer()
    noteId = fields.Integer()
    userId = fields.Integer()
    timeOfEdit = fields.DateTime()
    @post_load
    def get_edit(self,data,**kwargs):
        return Edit(**data)

class Allow_valid(Schema):
    id = fields.Integer()
    noteId = fields.Integer()
    userId = fields.Integer()
    @post_load
    def get_allow(self,data,**kwargs):
        return Allow(**data)

