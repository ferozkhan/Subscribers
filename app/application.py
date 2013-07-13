# -*- encoding: utf-8 -*-

import os
from ConfigParser import SafeConfigParser
from flask import Flask, request, redirect, render_template, flash
from module import subscriber, validator
from module.app_exceptions import InvalidConfigSection
import module.decorators as decor


app = Flask(__name__)
CONFIG_FILE = os.path.join(os.environ.get('HOME'), 'subs_app.cfg')


@app.route('/')
def home():
    mongo_config = parse_config(CONFIG_FILE)
    subs = subscriber.Subscriber(**mongo_config)
    subscribers = subs.subscribers()
    return render_template('index.html', subscribers=subscribers)


@app.route('/add', methods=['POST'])
def add_subscriber():
    email = request.form['email']
    valid_email = validator.email(email)
    if not valid_email:
        flash('Invalid Email Address', 'error')
        return redirect('/')

    mongo_config = parse_config(CONFIG_FILE)
    subs = subscriber.Subscriber(**mongo_config)
    status = subs.add_subscriber(email)

    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete_subscriber():
    mongo_config = parse_config(CONFIG_FILE)
    subs = subscriber.Subscriber(**mongo_config)
    status = subs.delete_subscriber(request.form['_id'])
    return redirect('/')


@decor.cache
def parse_config(config_file, section='mongo'):
    parser = SafeConfigParser()
    parser.read(config_file)

    return dict(parser._sections.get(section))


app.secret_key = '\xbey<O\xb7\x1c\x8ay\xc1\x8ez/\xd7vUE\xc3\xe4\x99 4\xe30\x1d'
if __name__ == '__main__':
    app.run()
