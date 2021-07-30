from src import app
from src.models.users_model import users_model
import os
from werkzeug.utils import secure_filename
import time
from flask import request 
from flask import make_response
import json

uobj=users_model()


@app.route("/login",methods=["post"])
def login():
    # email = request.form.get('email')
    # password = request.form.get('password')
    return uobj.login_model(request.form.to_dict())

@app.route("/add_user",methods=["post"])
def add_user():
    return uobj.add_user_model(request.form)


@app.route("/users/get_single_user_details/<user_id>")
def user_profile(user_id):
    return uobj.user_profile_model(user_id)

@app.route("/mylist/<id>")
def mylist(id):
    return uobj.mylist_model(id)

@app.route("/image_uploading")
def image():
    return uobj.image_model()
  
@app.route("/mydate/<date1>/<date2>")
def mydate(date1,date2):
    return uobj.mydate_model(date1,date2)
    
        


@app.route("/img",methods=["post"])
def img():
    file = request.files['data']
    filename = secure_filename(file.filename)
    extension  = os.path.splitext(filename)[1]
    allowed_extension = [".jpg",".jpeg",".png"]
    if extension in allowed_extension:
        extension = os.path.splitext(filename)[1]
        currenttime = time.time()
        finalfile = str(currenttime).split(".")[0]+str(currenttime).split(".")[1]+extension
        file.save(os.path.join(app.root_path+"/uploads",finalfile))
        return make_response({"success":"File uploaded","file_path":finalfile},200)
    else:
        return make_response({"Error":"File Extension Not Supported"},200) 







