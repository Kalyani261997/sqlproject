from src import app
from src.models.users_model import users_model
uobj=users_model()

@app.route("/signup",methods=["post"])
def signup():
    uobj.signup_model()
    return "<h1> Welcome Guys!! </h1>"


@app.route("/max",methods=["get"])
def max():
    return uobj.max_model()


@app.route("/avg",methods=["get"])
def avg():
    return uobj.avg_model()

@app.route("/sum",methods=["get"])
def sum():
    return uobj.sum_model()


@app.route("/where",methods=["get"])
def where():
    return uobj.where_model()

@app.route("/desc",methods=["get"])
def desc():
    return uobj.desc_model()

@app.route("/asc",methods=["get"])
def asc():
    return uobj.asc_model()



