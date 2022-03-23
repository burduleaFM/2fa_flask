import hashlib

from flask import jsonify, request
from datetime import datetime, timedelta

from app import app
from models import db, User, Token
from utils import send_mail


# Register a user
@app.route("/register", methods = ['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    pass_hash = hashlib.sha256(password.encode())
    password_hash = pass_hash.hexdigest()
    email = request.json['email']
    user = User(username = username, password = password_hash, email = email)
    db.session.add(user)
    db.session.commit()
    return jsonify ({"msg": "created", "status code": 201})

# Check if the user exists
@app.route("/login", methods = ['POST'])
def login():
    request_username = request.json['username']
    request_password = request.json['password']
    request_password_hash = hashlib.sha256(request_password.encode()).hexdigest()
    db_user = (User.query.filter_by(username=request_username).first())
    try:  
       if request_username == db_user.username and request_password_hash == db_user.password:
          code = send_mail(db_user.email)
          valid_until= datetime.now() + timedelta(seconds=60)
          token = Token(code = code, time = valid_until, user_id = db_user.id)
          db.session.add(token)
          db.session.commit()
          return jsonify ({"msg": "ok", "status code": 200})
       else:  
          return jsonify ({"msg": "not found", "status code": 404})
    except:
          return jsonify ({"msg": "not found", "status code": 404})
    
# second factor authentication
@app.route("/code", methods = ['POST'])
def code():
    print(code)
    request_code = request.json['code']
    db_code = Token.query.filter_by(code=request_code).first()
    try:
       if db_code.code != None and db_code.time >= datetime.now():
          obj = Token.query.filter_by(time=db_code.time).one()
          db.session.delete(obj)
          db.session.commit() 
          return jsonify ({"msg": "ok", "status code": 200})
       else:
          obj = Token.query.filter_by(time=db_code.time).one()
          db.session.delete(obj)
          db.session.commit() 
          return jsonify ({"msg": "time out", "status code": 408})
    except:
       return jsonify ({"msg": "forbidden", "status code": 403})

