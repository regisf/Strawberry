from flask import Flask

# Import blueprints
from fbelib.blueprints.pages import page_bp
from fbelib.blueprints.category import category_bp
from fbelib.blueprints.tags import tags_bp


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
#
#
if __name__ == '__main__':
    app.debug = True
    app.run()
