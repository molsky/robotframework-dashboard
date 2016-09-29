from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from rfwebui.configs.config import config


app = Flask("rfwebui")
app.config.from_object(config['development'])
toolbar = DebugToolbarExtension(app)


from rfwebui import views
