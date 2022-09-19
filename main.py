
from flask import Flask
from app.views import view_blueprint


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


app.register_blueprint(view_blueprint)

if __name__ == '__main__':
    app.run()
