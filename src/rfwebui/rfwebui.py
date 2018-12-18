from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from configs.config import config


app = Flask("rfwebui", static_folder="static")
app.config.from_object(config['development'])
toolbar = DebugToolbarExtension(app)


from views import *


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
