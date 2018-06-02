from flask import  render_template, session, redirect, url_for, escape, request
from app import app, models

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return render_template('home.html', username=escape(session['username']))
    return render_template('home.html', username='nobody')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))

@app.route('/u/<username>')
def profile(username):
    if username == session['username']:
        return redirect(url_for('editprofile'))
    return "Userprofile of " + username
@app.route('/editprofile/<username>/')
def editprofile(username):
    return render_template('editprofile.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)
