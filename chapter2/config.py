class Config(object):
    POSTS_PER_PAGE = 10


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SECRET_KEY = '\xdc\x84I\xc44\xe7@m$V\xd3\xc3\x106:G7\xebL\xa35\x9bcW'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # SQLALCHEMY_ECHO = True
    SECRET_KEY = '\xdc\x84I\xc44\xe7@m$V\xd3\xc3\x106:G7\xebL\xa35\x9bcW'
