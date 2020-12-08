from flask import Flask,request
from wsgiref.simple_server import make_server
from orm import Edit,Note,Allow,engine,User
from sqlalchemy.orm import Session

import json
from collections import namedtuple
from json import JSONEncoder


app = Flask(__name__)

session = Session(engine)

@app.route('/note',methods=['POST'])
def add_note():
    d = request.get_json()
    if d["numbofEditors"]>0 and d["numbofEditors"]<=5:
        session.add(Note(d["tag"],d["text"],d["numbofEditors"]))
        session.commit()
        return 'created note',201
    else:
        return 'number of editors can"t be less then 1 and more then 5',405

@app.route('/note/<id>',methods=['GET'])
def get_note(id):
    print(session.query(Note).filter_by(id=id).first().__dict__)
    return json.dumps(session.query(Note).filter_by(id=id).first().__dict__)
    return 'get note '+id

@app.route('/note/<id>',methods=['PUT'])
def put_note(id):
    print(id)
    return 'put note '+id

@app.route('/note/<id>',methods=['DELETE'])
def delete_note(id):
    print(id)
    return 'delete note '+id


@app.route('/user/createWithArray',methods=['POST'])
def create_list_of_users():
    request.get_json()[0]["email"]
    return "created list of users"

@app.route('/user/login',methods=['GET'])
def login():
    return "login"

@app.route('/user/logout',methods=['GET'])
def logout():
    return "logout"

@app.route('/user/<id>',methods=['GET'])
def get_user(id):
    return "user "+id

if __name__ == '__main__':
    app.run(debug=True)

##with make_server('', 5000, app) as server:
##    print("That is working!!!")
##
##    server.serve_forever()
