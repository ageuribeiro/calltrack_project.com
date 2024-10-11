from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', flask_token='my_token')


app.run(debug=True)