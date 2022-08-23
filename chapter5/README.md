# Modular application

    ./
        manage.py
        main.py
        config.py
        database.db
        webapp/
            __init__.py
            blog/
                __init__.py
                controllers.py
                forms.py
                models.py
            main/
                __init__.py
                controllers.py
            templates/
                blog/
        migrations/
            versions/

Defenition 

    ./<MODULE_NAME>
        __init__.py -> Declare a python module
        controllers.py -> where our blueprint definition and views are
        models.py -> The module database models definitions
        forms.py -> All the module's web Forms

## environmental variables

    $ export WEBAPP_ENV="dev"
    $ echo $WEBAPP_ENV
    dev
    $ unset $WEBAPP_ENV
    $ echo $WEBAPP_ENV


    env = os.environ.get('WEBAPP_ENV', 'dev')
    app = create_app('config.%sConfig' % env.capitalize())

## Application factories
concept of a factory comes from OOP world, and means function or object that creates another object. Application factory will take one of our
config objects, which we created, and return a Flask application object.

Benefits 
- Allows the context of the environment to change the configuration of the application
- Makes testing much easier because it allows differently configured applications
to be tested quickly
- Multiple instances of the same application using the same configuration can be created very easily


## Run project 
    $ export FLASK_APP=main.py (Unix)
    $ set "FLASK_APP=main.py" (windows)
    
    $ flask db init
    $ flask db migrate -m"initial migrate"
    $ flask db upgrade
    
    # fake data generation (gitbash)
    $ ./init.sh  

    $ flask run
