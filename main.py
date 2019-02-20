from flask import  render_template, session, redirect, url_for, escape, request, flash, url_for
from flask_login import current_user, login_user
from app import app, models, forms, db
from app.models import User

# TODO: GDPR compliance
#       - cookie prefs.
#       - account deletion

# Landing Page Logic
@app.route('/')
@app.route('/index')
def index():
    '''Checks if the user is logged in and ajusts the user variable accordingly'''
    if 'username' in session:
        return render_template('home.html', username=escape(session['username']))
    return render_template('home.html', username='nobody')


# Login logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember=form.remember_me.data)
        
        flash('Login requested for user {}, remember_me={}'.format(form.email.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


    '''Handles login from the login-form
    if request.method == 'POST':
        session['username'] = request.form['username']
        print(request.form.get('remember'))
        session['logged-in'] = True
        return redirect(url_for('index'))

    if not session.get('logged-in'):
        form = forms.LoginForm()
        return render_template('login.html', form=form)
    '''
    return redirect(url_for('index'))


# TODO: Rewrite for LoginManager
@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop('logged-in', None)
    return redirect(url_for('index'))


# TODO: Show only profiles of existing users
# TODO: Rewrite for LoginManager
@app.route('/user/<username>')
@app.route('/u/<username>')
def profile(username):
    if username == session['username']:
        return redirect(url_for('editprofile'))
    return render_template('templates/editprofile.html', username=username1)


# TODO: Reflect profile changes in database
# TODO: Rewrite for LoginManager
# Set directory for editing profiles
@app.route('/editprofile/<username>/', methods=['GET', 'POST'])
def editprofile(username):
    form = forms.EditProfileForm()
    return render_template('editprofile.html', username=username, form=form)



# Set directory for registration
@app.route('/register', methods=['GET', 'POST'])
def registration():

    form = forms.RegistrationForm()
    if form.validate_on_submit():
        u = User(firstname=form.firstname.data, surname=form.surname.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


    '''if session.get('logged-in'):
        return redirect(url_for('index'))
    form = forms.RegistrationForm()
    return render_template('register.html', form=form)
'''

# TODO: Rewrite for LoginManager
# Set directory for changing Email
@app.route('/editprofile/<username>/change-email/', methods=['GET', 'POST'])
def changeEmail(username):
    return render_template('change-email.html', username=username)


# TODO: Write impressum
# Add impressum.html
@app.route('/impressum')
def impressum():
    return render_template('includes/_impressum.html')


if __name__ == '__main__':
    app.run(debug=True)
