from flask import Blueprint, render_template 



api = Blueprint("api", __name__)






@api.route("/", methods=["GET"])
def get_home():
    return render_template("home.html")






