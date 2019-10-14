from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing application
app = Flask(__name__,instance_relative_config= True)

# Initializing Flask Extensions
bootstrap = Bootstrap(app)

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #from .requests import configure_request
    #configure_request(app)


    return app
