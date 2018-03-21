from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)



@app.route("/")
@app.route("/login", methods = ['GET','POST'])
def login():
    return render_template('include.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = 'localhost', port = 5000)