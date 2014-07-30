# -*- coding: utf-8 -*-
# Strawberry Blog Engine
#
# Copyright (c) 2014 Regis FLORET
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = 'Regis FLORET'

from flask import Flask

# Connect to the database
from strawberrylib.db.database import create_connection

create_connection()

# Import blueprints
from strawberrylib.blueprints.pages import page_bp
from strawberrylib.blueprints.category import category_bp
from strawberrylib.blueprints.tags import tags_bp


#
# Create the application
#
app = Flask(__name__)
app.register_blueprint(page_bp, url_prefix="/page")
app.register_blueprint(category_bp, url_prefix="/category")
app.register_blueprint(tags_bp, url_prefix="/tag")


#
# Route for normal path
#
@app.route('/')
@app.route('/<path>')
def blog(path=None):
    return "Helltesto {}".format(path)


#
# 404 error handler
#
@app.errorhandler(404)
def do_error(error):
    return "Page inconnue"


#
# For standalone
#
if __name__ == '__main__':
    from strawberrylib.config import settings

    app.debug = settings.Debug
    app.run()
