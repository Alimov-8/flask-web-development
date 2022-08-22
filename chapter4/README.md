# Creating Controllers with Blueprints

`Sessions` are the way Flask will store information across requests; default 31 days lifetime, and can be changed `PERMANENT_SESSION_LIFETIME` config key 

    # Example usage

    from flask import session
    ...
    session['page_loads'] = session.get('page_loads', 0) + 1

`Global` is a thread-safe namespace store to keep data during a request's context, right place to keep data than needs to be shared across views, templates ... within request context

    from flask import g
    ....
    g.book_name = "Python Tricks"
    book_name = g.book_name
    book_name = g.pop('book_name', "default_if_not_present")

    
## Request setup and teardown

`request` contains information such as HTTP headers, URI arguments, URL path,
WSGI environment, and whatnot.

- setup 

`@app.before_request` function is executed every time, before a new request is made

    import random
    from flask import session, g
    ...
    @app.before_request
    def before_request():
        session['page_loads'] = session.get('page_loads', 0) + 1
        g.random_key = random.randrange(1, 10)

- teardown

`@app.teardown_request`, which is called after the end of every request

## Error pages (404 not found)


    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

`app.errorhandler()` function may take multiple
HTTP status codes to define which code it will act on. The returning of a tuple instead of
just an HTML string allows you to define the HTTP status code of the Response object. By
default, this is set to 200


## Class Based Views

    from flask.views import View
    ...
    class GenericView(View):
        methods = ['GET', 'POST']
        
        def __init__(self, template):
            self.template = template
            super(GenericView, self).__init__()
        
        def dispatch_request(self):
            if request.method == 'GET':
                return render_template(self.template)
    
    app.add_url_rule(
        '/', view_func=GenericView.as_view(
        'home', template='home.html'
        )
    )

`dispatch_request()` -  acts as the normal view function and returns an
HTML string

`app.add_url_rule()` - function mimics the `app.route()`


## ListView
    class GenericListView(View):
        def __init__(self, model, list_template='generic_list.html'):
            self.model = model
            self.list_template = list_template
            self.columns = self.model.__mapper__.columns.keys()
            # Call super python3 style
            super(GenericListView, self).__init__()
        
        def render_template(self, context):
            return render_template(self.list_template, **context)
        
        def get_objects(self):
            return self.model.query.all()

        def dispatch_request(self):
            context = {'objects': self.get_objects(), 'columns': self.columns}
            return self.render_template(context)
    
    app.add_url_rule(
        '/generic_posts', view_func=GenericListView.as_view(
        'generic_posts', model=Post)
    )
    app.add_url_rule(
        '/generic_users', view_func=GenericListView.as_view(
        'generic_users', model=User)
    )
    app.add_url_rule(
        '/generic_comments', view_func=GenericListView.as_view(
        'generic_comments', model=Comment)
    )

## Method class views

    from flask.views import MethodView
    
    class UserView(MethodView):
        def get(self):
            ...
    
        def post(self):
            ...
        
        def put(self):
            ...
        
        def delete(self):
            ...

    app.add_url_rule(
        '/user',
        view_func=UserView.as_view('user')
    )


## Blueprints

`Blueprints` - Helps us to architect our project structure to make it scaleable for future. [One app has one actor]

        Let's say that we wanted to add a photo sharing function to our site, we would be able to group all the view functions into one blueprint with its own templates, static folder, and URL prefix without any fear of disrupting the functionality of the rest of the site.

- Example usecase

        from flask import Blueprint
        
        example = Blueprint(
            'example',
            __name__,
            template_folder='templates/example',
            static_folder='static/example',
            url_prefix="/example"
        )
        
        @example.route('/')
        def home():
            return render_template('home.html')

        app.register_blueprint(example)

- Example filestructure 

        ecommerce/
        |
        ├── api/
        |   ├── __init__.py
        |   └── api.py
        |
        ├── auth/
        |   ├── templates/
        |   |   └── auth/
        |   |       ├── login.html
        |   |       ├── forgot_password.html
        |   |       └── signup.html
        |   |
        |   ├── __init__.py
        |   └── auth.py
        |
        ├── cart/
        |   ├── templates/
        |   |   └── cart/
        |   |       ├── checkout.html
        |   |       └── view.html
        |   |
        |   ├── __init__.py
        |   └── cart.py
        |
        ├── general/
        |   ├── templates/
        |   |   └── general/
        |   |       └── index.html
        |   |
        |   ├── __init__.py
        |   └── general.py
        |
        ├── products/
        |   ├── static/
        |   |   └── view.js
        |   |
        |   ├── templates/
        |   |   └── products/
        |   |       ├── list.html
        |   |       └── view.html
        |   |
        |   ├── __init__.py
        |   └── products.py
        |
        ├── static/
        |   ├── logo.png
        |   ├── main.css
        |   └── generic.js
        |
        ├── app.py
        ├── config.py
        └── models.py


