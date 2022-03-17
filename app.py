from flask import Flask

from flask import render_template, session, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ('login.html')

if __name__ == '__main__':
    app.run