from flask import (
    render_template,
    Blueprint,
    redirect,
    url_for,
    flash,
    request,
    jsonify,
)
from flask_login import login_user, logout_user
from flask_jwt_extended import create_access_token

from .forms import LoginForm, RegisterForm
from .models import User
from . import authenticate
from .. import db


auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='../templates/auth',
    url_prefix="/auth"
)


@auth_blueprint.route('/login', methods=['GET', 'POST'])
# @oid.loginhandler
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one()
        login_user(user, remember=form.remember.data)
        flash("You have been logged in.", category="success")
        return redirect(url_for('main.index'))

    return render_template('login.html', form=form)


@auth_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out.", category="success")
    return redirect(url_for('main.index'))


@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash("Your user has been created, please login.", category="success")

        return redirect(url_for('.login'))

    return render_template('register.html', form=form)


@auth_blueprint.route('/api', methods=['POST'])
def api():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
        
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400
    user = authenticate(username, password)
    if not user:
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

