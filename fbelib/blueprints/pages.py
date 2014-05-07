from flask import Blueprint

__author__ = 'Regis'

page_bp = Blueprint('page', __name__, template_folder="templates")

@page_bp.route('/<page_name>')
def page(page_name):
    return "You ask a page: " + page_name
