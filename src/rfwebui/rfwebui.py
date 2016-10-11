from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from configs.config import config


app = Flask("rfwebui")
app.config.from_object(config['production'])
toolbar = DebugToolbarExtension(app)


from views import *


if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
