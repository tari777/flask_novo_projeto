from flask import Flask

from flask import render_template, session, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template ('login.html', title='Pagina Login')
if __name__ == '__main__':
    app.run