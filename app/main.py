# -*- encoding: utf-8 -*-

import os
from ConfigParser import SafeConfigParser
from flask import Flask, request, redirect, render_template, flash
from module import subscriber, validator
app = Flask(__name__)

parser = SafeConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), 'config.cfg'))
MONGO_ENV = {
    "DB": parser.get('mongo', 'db')),
    "API_KEY": parser.get('mongo', 'api_key'),
    "COLLECTION": parser.get('mongo', 'collection')
}


@app.route('/')
@app.route('/<action>', methods=["POST"])
def App(action=None):
    try:
        subs = subscriber.Subscriber(**MONGO_ENV)
        if action == 'subscribing':
            email = request.form['email']
            validator.email(email)
            status = subs.subscribe(email)
        elif action == 'unsubscribing':
            id = request.form['_id']
            status = subs.unsubscribe(id)
        else:
            return render_template('index.html', subscribers=subs.subscribers())

        if status:
            if status != '200':
                flash("Oops! Something went wrong.", "error")
            else:
                flash("%s Successful" % (action.title()), "message")

    except ValueError:
        flash("Email address can not be empty", "error")
    except TypeError:
        flash("Invalid Email Format", "error")

    return redirect('/')


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run()
