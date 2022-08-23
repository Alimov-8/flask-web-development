import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = '\xdc\x84I\xc44\xe7@m$V\xd3\xc3\x106:G7\xebL\xa35\x9bcW'
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    # SQLALCHEMY_ECHO = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
