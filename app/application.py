# -*- encoding: utf-8 -*-

import os
import traceback
from module import subscriber, validator, utils
from module.app_exceptions import InvalidConfigSection
from flask import Flask, request, redirect, render_template, flash


app = Flask(__name__)
CONFIG_FILE = os.path.join(os.environ.get('HOME'), 'subs_app.cfg')


@app.route('/')
def home():
    try:
        mongo_config = utils.parse_config(CONFIG_FILE)
        subscribers = subscriber.get_all_subscribres(mongo_config)
        return render_template('index.html', subscribers=subscribers)
    except:
        print traceback.format_exc()


@app.route('/add', methods=['POST'])
def add_subscriber():
    try:
        email = request.form['email']
        if not validator.is_email_valid(email):
            flash('Invalid Email Address', 'error')
            return redirect('/')

        mongo_config = utils.parse_config(CONFIG_FILE)
        subscriber.add_subscriber(mongo_config, email)
        return redirect('/')
    except:
        print traceback.format_exc()


@app.route('/delete', methods=['POST'])
def delete_subscriber():
    try:
        mongo_config = utils.parse_config(CONFIG_FILE)
        subscriber.delete_subscriber(mongo_config, request.form['_id'])
        return redirect('/')
    except:
        print traceback.format_exc()


app.secret_key = '\xbey<O\xb7\x1c\x8ay\xc1\x8ez/\xd7vUE\xc3\xe4\x99 4\xe30\x1d'
if __name__ == '__main__':
    app.run()
