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

` databasetype+driver://user:password@host:port/db_name `

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






