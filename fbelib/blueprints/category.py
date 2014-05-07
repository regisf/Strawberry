from flask import Blueprint

__author__ = 'Regis'

category_bp = Blueprint('category', __name__, template_folder="templates")

@category_bp.route('/')
def category():
    """
    Path for all categories
    """
    return "Display all categories"


@category_bp.route('/<name>')
def category_name(name):
    return "Display category: " + name

