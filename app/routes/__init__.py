from flask import Blueprint 



api = Blueprint("api", __name__)






@api.route("/", methods=["GET"])
def get_home():
    return "<h1>Welcome to our homepage</h1>"




