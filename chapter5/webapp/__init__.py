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
    from .blog.controllers import blog_blueprint
    from .main.controllers import main_blueprint

    # Flask app setup
    app = Flask(__name__)
    app.config.from_object(obbject_name)
    
    # Database setup
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(blog_blueprint)
    
    # Error handlers
    app.register_error_handler(404, page_not_found)

    return app