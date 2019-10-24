from flask import Flask
from flask import render_template, flash, redirect, stream_with_context, request, Response
from app.forms import InputForm
from config import Config
from flask_bootstrap import Bootstrap

APP = Flask(__name__)
APP.config.from_object(Config)
bootstrap = Bootstrap(APP)

@APP.route('/', methods=['GET', 'POST'])
@APP.route('/index', methods=['GET', 'POST'])
def index():
    '''
    Handles the route for the index page.\n
    Serves the html and handles the requests for the flask wtf forms\n
    on the index page used to input the server ip and port.
    '''
    form = InputForm()
    if form.validate_on_submit():
        return redirect(f'/')
    return render_template('form.html', form=form)