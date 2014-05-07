from flask import Blueprint

__author__ = 'Regis'

tags_bp = Blueprint('tags', __name__, template_folder="templates")


@tags_bp.route('/')
def tags():
    return "Display all tags"


@tags_bp.route("/<name>")
def tag_name(name):
    return "Display all post for: " + name

