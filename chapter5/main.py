import os
from webapp import create_app


env = os.environ.get('WEBAPP_ENV', 'dev')  # load env vars
app = create_app('config.%sConfig' % env.capitalize())  # congif/DevConfig


if __name__ == '__main__':
    app.run()


