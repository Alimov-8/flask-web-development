import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)  # app.config['DEBUG']

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    # __tablename__ = 'user_table_name'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, index=True, unique=True)
    password = db.Column(db.String(255))
    posts = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic',
    )   
    
    # username = db.Column('user_name', db.String(255))

    def __init__(self, username) -> None:
        self.username = username

    def __repr__(self) -> str:
        return f"<User '{self.username}'>"


tags = db.Table(
    'post_tags',
    
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    comments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )

    tags = db.relationship(
        'Tag',
        secondary=tags,
        backref=db.backref('posts', lazy='dynamic')
    )


    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    def __init__(self, title) -> None:
        self.title = title
    
    def __repr__(self) -> str:
        return f"<Post '{self.title}'>"


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.datetime.now)
    
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))
    
    def __repr__(self):
        return f"<Comment '{self.text[:15]}'>"


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    publish_date = db.Column(db.DateTime(), default=datetime.datetime.now)

    
    def __init__(self, title) -> None:
        self.title = title
    
    def __repr__(self) -> str:
        return f"<Tag '{self.title}'>"


# if __name__ == '__main__':
#     app.run()
