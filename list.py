from src import app
from src.models.list_model import list_model
from flask import request 
lobj=list_model()


@app.route("/add_task",methods=["post"])
def listS():
    return lobj.list_model(request.form)