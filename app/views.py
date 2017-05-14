from flask import render_template
from app import app
import phonequeue

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/other')
def other():
    return render_template("other.html", data=phonequeue.fakeData(), fakeAgents=phonequeue.processedFakeAgents())