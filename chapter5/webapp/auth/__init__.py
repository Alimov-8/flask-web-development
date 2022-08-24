from flask_login import LoginManager


"""
The preceding configuration values define which view should be treated as the login page,
and what the message should be to the user after a successful login. Setting the
session_protection option to strong better protects against malicious users tampering
with their cookies. When a tampered cookie is identified, the session object for that user is
deleted and the user is forced to log back in.
"""
login_manager = LoginManager()
login_manager.login_view = "auth.login" 
login_manager.session_protection = "strong" 
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"



@login_manager.user_loader
def load_user(userid):
    """
    The load_user function takes an ID and returns the User object. When a cookie is
    validated, Flask-Login will use our function to fetch the user into the current session.
    """
    from models import User
    return User.query.get(userid)


def create_module(app, **kwargs):
    login_manager.init_app(app)
    from .controllers import auth_blueprint
    app.register_blueprint(auth_blueprint)
