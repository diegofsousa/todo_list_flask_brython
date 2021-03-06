from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from .model import User

front = Blueprint('front', __name__)


@front.route('/', methods=['GET'])
@login_required
def todo():
    return render_template('todo.html')


@front.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@front.route('/login', methods=['POST'])
def login_post():
    user = User().login(
        request.form.get('email', ''), request.form.get('senha', '')
    )
    if user:
        login_user(user)
        return redirect('/')

    return render_template('login.html', error=True)


@front.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('.login'))


@front.route('/register', methods=['GET'])
def register():
    return render_template('register.html')


@front.route('/register', methods=['POST'])
def register_post():
    user = User().register(
        request.form.get('nome'),
        request.form.get('email'),
        request.form.get('senha'),
    )

    if user:
        login_user(user)
        return redirect('/')

    return render_template('register.html', error=True)
