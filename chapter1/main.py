from flask import Flask
from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)  # app.config['DEBUG']

@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
