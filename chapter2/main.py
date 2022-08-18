from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)  # app.config['DEBUG']

db = SQLAlchemy(app)


class User(db.Model):
    # __tablename__ = 'user_table_name'


    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    # username = db.Column('user_name', db.String(255))

    def __init__(self, username) -> None:
        self.username = username

    def __repr__(self) -> str:
        return f"<User '{self.username}'>"



# if __name__ == '__main__':
#     app.run()
