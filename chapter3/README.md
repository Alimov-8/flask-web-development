## Jinja's syntax

Jinja is a templating language written in Python. A templating language is a simple format
that is designed to help automate the creation of documents.

Jinja has built in functions for filtering and for other purpose

    {{ variable | filter_name(*args) }}

    {% filter filter_name %}
        A bunch of text
    {% endfilter %}

Example 

    {{ post.date | default('2015-01-01') }}
    {{ 75 | float }}
    {{ ['Python', 'SQLAlchemy'] | join(',') }}
    {{ post.tags | length }}
    {{ 3.141592653589793238462 | round(1) }}  # 3.1
    {{ 4.7 | round(1, "common") }}  # 5
    {{ "<h1>Post Title</h1>" | safe }} to show user inputs
    {{ "post title" | title }}
    {{ "A Longer Post Body Than We Want" | truncate(10) }}

    var collection = new PostCollection({{ posts | tojson | safe }});

    {# Comment: Note to the maintainers of this code #}


Custom filters

`{{ variable | count_substring("string") }}`

    @app.template_filter
    def count_substring(variable, sub_string): 
        return string.count(sub_string)


## Conditions
    {% if ... %}
    {% else %}
    {% endif %}

## Loops 
    {% for i in list %}
    {% endfor %}

    loop.index        The current iteration of the loop (1 indexed)
    loop.index0       The current iteration of the loop (0 indexed)
    loop.revindex     The number of iterations from the end of the loop (1 indexed)
    loop.revindex0    The number of iterations from the end of the loop (0 indexed)
    loop.first        True if the current item is first in the iterator
    loop.last         True if the current item is last in the iterator
    loop.length       The number of items in the iterator
    loop.cycle        The helper function to cycle between the items in the iterator (this is explained later)
    loop.depth        Indicates how deep in a recursive loop the loop currently is (starts at level 1)
    loop.depth0       Indicates how deep in a recursive loop the loop currently is (starts at level 0)

## Macro 
A macro is best understood as a function in Jinja that returns a template

    Function
    {% macro input(name, label, value='', type='text') %}
        <div class="form-group">
        <label for"{{ name }}">{{ label }}</label>
        <input type="{{ type }}" name="{{ name }}"
        value="{{ value | escape }}" class="form-control">
        </div>
    {% endmacro %}

    # Call
    {{ input('name', 'Name') }}

    # Output
    <div class="form-group">
        <label for"name">Name</label>
        <input type="text" name="name" value="" class="form-control">
    </div>


## Flask vars

`Access to config vars` -> {{ config.SQLALCHEMY_DATABASE_URI }}`

`request object` -> {{ request.url }}

`session object` -> {{ session.new }}

URLS 

    {{ url_for('post', post_id=1) }}

    @app.route('/post/<int:post_id>', methods=('GET', 'POST'))
    def post(post_id):
        pass


## Flash messages
    views.py 

    @app.route('/post/<int:post_id>', methods=('GET', 'POST'))
    def post(post_id):
        ...
        db.session.commit()
        flash("New post added.", 'info')


    template.html 

    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }} alert-dismissible"
                role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-
                label="Close"><span aria-hidden="true">&times;</span></button>
                {{ message }}
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}


--- 




