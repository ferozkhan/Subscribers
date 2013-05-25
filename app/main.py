
import os
from flask import Flask, request, redirect, render_template
from module import subscriber
app = Flask(__name__)

MONGO_ENV = {
    "DB": "f27",
    "API_KEY": "uljBLBoFbq9e_9PhDcD5eX17R58qe6s2",
    "COLLECTION": "subscribers"
}


@app.route('/')
def home(action=None):
    subs = subscriber.Subscriber(**MONGO_ENV)
    return render_template('index.html', subscribers=subs.subscribers())


@app.route('/<action>', methods=["GET", "POST"])
def action(action=None):
    subs = subscriber.Subscriber(**MONGO_ENV)
    if action == 'subscribe':
        email = request.form["email"]
        subs.subscribe(email)
    return redirect('/')


if __name__ == '__main__':
    app.run()
