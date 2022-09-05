from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def page_not_found(error):
    return render_template('404.html'), 404


def create_app(obbject_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    
    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """

    # Flask app setup
    app = Flask(__name__)
    app.config.from_object(obbject_name)
    
    # Database setup
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Modules setup
    from .blog import create_module as blog_create_module
    from .main import create_module as main_create_module
    from .auth import create_module as auth_create_module
    from .api import create_module as api_create_module
    blog_create_module(app)
    main_create_module(app)
    auth_create_module(app)
    api_create_module(app)
    
    # Error handlers
    app.register_error_handler(404, page_not_found)

    return app
