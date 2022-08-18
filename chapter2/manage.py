from main import app, db, User, Post, Comment, Tag


@app.shell_context_processor
def make_shell_context():
    """Allow us to work with our models in the Flask shell."""

    return dict(
        app=app, 
        db=db, 
        User=User,
        Post=Post,
        Comment=Comment,
        Tag=Tag,
    )
