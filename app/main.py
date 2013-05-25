# -*- encoding: utf-8 -*-

import os
from flask import Flask, request, redirect, render_template, flash
from module import subscriber, validator
app = Flask(__name__)

MONGO_ENV = {
    "DB": "f27",
    "API_KEY": "uljBLBoFbq9e_9PhDcD5eX17R58qe6s2",
    "COLLECTION": "subscribers"
}


@app.route('/')
@app.route('/<action>', methods=["POST"])
def App(action=None):
    try:
        subs = subscriber.Subscriber(**MONGO_ENV)
        if action == 'subscribing':
            email = request.form['email']
            print(type(email), '<<<<<<<<<')
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
