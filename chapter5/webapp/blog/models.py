from datetime import datetime

from .. import db


# Many to Many relationship table for (Post, Tag)
tags = db.Table(
    'post_tags',
    
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
)


class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime(), default=datetime.now)
    
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

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
    
    def __init__(self, title='') -> None:
        self.title = title
    
    def __repr__(self) -> str:
        return f'<Post \'{self.title}\'>'


class Comment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text())
    date = db.Column(db.DateTime(), default=datetime.now)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment \'{self.text[:15]}\'>'


class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    publish_date = db.Column(db.DateTime(), default=datetime.now)

    
    def __init__(self, title='') -> None:
        self.title = title
    
    def __repr__(self) -> str:
        return f'<Tag \'{self.title}\'>'
