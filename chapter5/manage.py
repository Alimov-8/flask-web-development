import os
from webapp import db, migrate, create_app
from webapp.blog.models import User, Post, Tag



env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('config.%sConfig' % env.capitalize())



@app.shell_context_processor
def make_shell_context():
    """Allows access to defined fields in dict using flask shell."""
    return dict(
        app=app,
        db=db,
        User=User,
        Post=Post,
        Tag=Tag,
        migrate=migrate,
    )