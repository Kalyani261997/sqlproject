from src import app
from src.models.list_model import list_model
from flask import request 
lobj=list_model()


@app.route("/add_task",methods=["post"])
def listS():
    return lobj.list_model(request.form)

@app.route("/delete_task/<taskid>")
def deletefn(taskid):
    return lobj.delete_model(taskid)

@app.route("/select_task")
def selectfn():
    return lobj.select_model()

@app.route("/urlid/<id>")
def urlid(id):
    return lobj.urlid_model(id)
