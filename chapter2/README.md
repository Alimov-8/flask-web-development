`models` are a means of abstracting and providing a common
interface to access data

`relational database management system (RDBMS)` - database that holds data in
a tabular format with rows and columns and is able to implement a relational model with
data across tables (MSSQL)

`SQLAlchemy` is a database API at its lowest level, and performs object
relational mapping at its highest level.

`ORM (object relational mapper)` store and retrieve data using object-oriented approaches and solve
object-relational mismatches

<br>

## Database URI

`databasetype+driver://user:password@host:port/db_name`

    # SQLite connection string/uri is a path to the database file - relative or
    absolute.
    sqlite:///database.db

    # MySQL
    mysql+pymysql://user:password@ip:port/db_name

    # Postgres
    postgresql+psycopg2://user:password@ip:port/db_name

    # MSSQL
    mssql+pyodbc://user:password@dsn_name

    # Oracle
    oracle+cx_oracle://user:password@ip:port/db_name

Types

    db.String
    db.Text
    db.Integer
    db.Float
    db.Boolean
    db.Date
    db.DateTime
    db.Time

`SQLALCHEMY_ECHO = True` - shows how SQLAlchemy translates your code
into SQL queries

    # Tell Flask where to load our shell context
    $ export FLASK_APP=manage.py (linux)
    $ set "FLASK_APP=manage.py" (windows)

    $ flask shell

    >>> db.create_all()
    $ sqlite3 database.db .tables
    user

## CRUD

create, read, update, and delete

### CREAT

    >>> user = User(username='fake_name')
    >>> db.session.add(user)
    >>> db.session.commit()

### READ

    >>> users = User.query.all()

    >>> users = User.query.limit(10).all()

    # ascending
    >>> users = User.query.order_by(User.username).all()
    # descending
    >>> users = User.query.order_by(User.username.desc()).all()

    >>> user = User.query.first()
    >>> user.username

    # PK
    >>> user = User.query.get(1)

    # Chain
    >>> users = (
            User
            .query
            .order_by(User.username.desc())
            .limit(10)
            .first()
        )

## READ PAGINATION

    # Pagination pages 1-10, 11-20
    >>> User.query.paginate(1, 10)
    >>> User.query.paginate(2, 10)

    >>> page.items
    [<User 'fake_name'>]

    # what page?
    >>> page.page

    # How many pages?
    >>> page.pages

    >>> page.has_prev, page.has_next
    (False, False)

    # return the next or previous page pagination object
    # if one does not exist returns the current page
    >>> page.prev(), page.next()

## READ FILTER

    # query.filter_by on exact values
    >>> users = User.query.filter_by(username='fake_name').all()

    #
    >>> user = User.query.filter(
            User.id > 1
        ).all()

## READ COMPLEX with NOT, IN, OR

    >>> from sqlalchemy.sql.expression import not_, or_

    >>> user = User.query.filter(
            User.username.in_(['fake_name']),
            User.password == None
        ).first()

    # find all of the users with a password
    >>> user = User.query.filter(
            not_(User.password == None)
        ).first()

    # all of these methods are able to be combined
    >>> user = User.query.filter(
            or_(not_(User.password == None), User.id >= 1)
        ).first()

## UPDATE

    >>> User.query.filter_by(username='fake_name').update({
        'password': 'test'
    })

    # The updated models have already been added to the session
    >>> db.session.commit()

## DELETE

    >>> user = User.query.filter_by(username='fake_name').first()
    >>> db.session.delete(user)
    >>> db.session.commit()

# Relationships between models

## One to Many

    class User(db.Model):
        posts = db.relationship(
            'Post',
            backref='user',
            lazy='dynamic',
        )

    class Post(db.Model):
        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

`dynamic` - option, the related objects will be loaded upon
access and can be filtered down before returning.

    >>> user = User.query.get(1)
    >>> new_post = Post('Post Title')
    >>> new_post.user_id = user.id
    >>> user.posts
    []
    >>> db.session.add(new_post)
    >>> db.session.commit()
    >>> user.posts
    [<Post 'Post Title'>]

## One to Many

    tags = db.Table(
        'post_tags',

        db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
        db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    )

    post_id   tag_id
    1         1
    1         3
    2         3

    post = Post.query.get(1)
    tag1 = Tag('first')
    tag2 = tag('second')
    post.tags = [tag1, tag2]
    db.session.add(post)
    db.session.commit()

## Constraints & Indexes

Constraints is considered a good practice. Restrict the domain of a
certain model attribute and ensure data integrity and quality

- Not NULL (ensures that a certain attribute contains data)
- UNIQUE (ensures that a certain attribute value is always unique in the database
  table, which contains the model data)
- DEFAULT (sets a default value for the attribute when no values were provided)
- CHECK (used to specify range of values)

indexes are used to improve query performance, but be careful to IUD and Storage
index is used to reduce the
O(N) lookup on certain table columns that may be frequently used.

## SQLAlchemy sessions

- transactions automatically determine which objects are to be saved first when
  objects have relations (session automatically knew to save the tags
  first despite the fact that we did not add them to be committed)

- the session makes it impossible for there to be two different references to the same
  row in the database. This is accomplished by ensuring that all queries go through the
  session (Model.query is actually db.session.query(Model)),

`Important` - Flask SQLAlchemy creates a new session for every request and discards
any changes that were not committed at the end of the request.

## Alembic

`Alembic` - which
automatically creates and tracks database migrations from the changes in our SQLAlchemy
models (allows upgrade and downgrade between versions)

`Database migrations` are records of all the changes of our schema

    # Tell Flask where is our app
    $ export FLASK_APP=main.py
    
    $ flask db init

    $ flask db migrate -m"initial commit"

    $ flask db upgrade/downgrade

    $ flask db history


## Creating our views

    GET /post/<POST_ID> to render a specific post by its ID. This also renders all recent posts and tags.

    @app.route('/post/<int:post_id>')
    def post(post_id)
        post = Post.query.get_or_404(post_id)


## Template Structuring
- Include navbar: Jinja2 template: navbar.html—Renders a navigation bar.
- Block head: The header with the name of the site. Already includes
the head.html Jinja2 template.
- Include messages: Jinja2 template: messages.html—Renders alerts for the
users with different categories.
- Block body:
- Block left body: Normally, templates will override this block.
- Block right body: This will display the most recent posts and tags.
- Block footer: Jinja2 template: footer.html.

        #Example 

        {% extends "base.html" %}
        {% import 'macros.html' as macros %}
        {% block title %}Home{% endblock %}
        {% block leftbody %}
        {{ macros.render_posts(posts) }}
        {{ macros.render_pagination(posts, 'home') }}
        {% endblock %}


## Database fake data

    def generate_users(n):
        users = list()
        
        for i in range(n):
            user = User()
            user.username = faker.name()
            user.password = "password"
            
            try:
                db.session.add(user)
                db.session.commit()
                users.append(user)
            
            except Exception as e:
                log.error("Fail to add user %s: %s" % (str(user), e))
                db.session.rollback()
        
        return users
