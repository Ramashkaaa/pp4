from flask import Flask,request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash,check_password_hash
from wsgiref.simple_server import make_server
from orm import Edit,Note,Allow,engine,User
from sqlalchemy.orm import Session
from datetime import datetime

import json
from collections import namedtuple
from json import JSONEncoder
from marshmallow import Schema, fields, INCLUDE, ValidationError

from flask_marshmallow import Marshmallow


app = Flask(__name__)
ma = Marshmallow(app)
auth = HTTPBasicAuth()

session = Session(engine)

class NoteSchema(ma.Schema):
    class Meta:
        fields = ("tag","text","numbofEditors")
    numbofEditors = fields.Integer(required=True) 
note_schema = NoteSchema()

@app.route('/',methods=['POST'])
@auth.login_required
def index():
    return "ASSA"

@app.route('/note',methods=['POST'])
##@auth.login_required
def add_note():
    try:
        d = request.get_json()
        print(note_schema.load(d),"ASA")
        if d["numbofEditors"]>0 and d["numbofEditors"]<=5:
            session.add(Note(d["tag"],d["text"],d["numbofEditors"]))
            session.commit()
            return 'created note',201
        else:
            return 'number of editors can"t be less then 1 and more then 5',405
    except TypeError as err:
        print(err)
        return "invalid input",404
@app.route('/note/<id>',methods=['GET'])
def get_note(id):
    x = session.query(Note).filter_by(id=id).first()
    return (json.dumps(x.as_dict()),200) if x != None else ("not found",404)

@app.route('/note/<id>',methods=['PUT'])
def put_note(id):
    obj = session.query(Note).filter_by(id=id).first()
    if obj==None:
        return "not found",404
    d = request.get_json()
    if d["numbofEditors"]<=0 or d["numbofEditors"]>5:
        return "invalid input",405
    obj.tag,obj.text,obj.numbofEditors = d["tag"],d["text"],d["numbofEditors"]
    session.add(Edit(d["text"],id,1,datetime.now()))
    session.commit()
    return 'The note has been edited',201

@app.route('/note/<id>',methods=['DELETE'])
def delete_note(id):
    x = session.query(Note).filter_by(id=id)
    if x.first()==None:
        return "not found",404
    session.query(Note).filter_by(id=id).delete()
    session.commit()
    return 'deleted note '+id

@app.route('/user/createWithArray',methods=['POST'])
def create_list_of_users():
    l = request.get_json()
    for i in range(len(l)):
        o = l[i]
        if len(o)!=7:
            return "invalid input",405
        session.add(User(*o.values()))
    session.commit()
    return "created list of users",201

@app.route('/user/login',methods=['GET'])
def login():
    return "login"

@app.route('/user/logout',methods=['GET'])
def logout():
    return "logout"

@app.route('/user/<id>',methods=['GET'])
def get_user(id):
    x = session.query(User).filter_by(id=id).first()
    print(x==None,x!=None)
    return (json.dumps(x.as_dict()),200) if x != None else ("not found",404)

@app.route('/user/<id>',methods=['PUT'])
def put_user(id):
    obj = session.query(User).filter_by(id=id).first()
    if obj==None:
        return "not found",404
    d = request.get_json()
    if len(d)!=7:
        return "invalid input",405
    obj.username,obj.firstName,obj.lastName,obj.email,obj.password,obj.phone,obj.userRole = d.values()
    session.commit()
    return 'The user has been updated',201

@app.route('/user/<id>',methods=['DELETE'])
def delete_user(id):
    x = session.query(User).filter_by(id=id)
    if x.first()==None:
        return "not found",404
    session.query(User).filter_by(id=id).delete()
    session.commit()
    return 'deleted user '+id,

if __name__ == '__main__':
    app.run(debug=True)

##with make_server('', 5000, app) as server:
##    print("That is working!!!")
##
##    server.serve_forever()

##// {
##//     "username":"yahiko",
##//     "firstname":"andrii",
##//     "lastname":"riabchuk",
##//     "email":"darwindokinz@",
##//     "password":"2204",
##//     "phone":"098728911",
##//     "userRole":"1"
##// }
