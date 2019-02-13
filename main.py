from flask import  render_template, session, redirect, url_for, escape, request, flash, url_for
from app import app, models, forms

# TODO: GDPR compliance
#       - cookie prefs.
#       - account deletion
# TODO: Rewrite all forms with wtforms

# Landing Page Logic
@app.route('/')
@app.route('/index')
def index():
    '''Checks if the user is logged in and ajusts the user variable accordingly'''
    nav = forms.Nav()
    if 'username' in session:
        return render_template('home.html', username=escape(session['username']))
    return render_template('home.html', username='nobody', nav=nav)




# TODO: Check if user exists in database
# Login logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    nav = forms.Nav()
    if form.validate_on_submit():
        #The Flash function shows the user a message
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, nav=nav)


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
    nav = forms.Nav()
    if username == session['username']:
        return redirect(url_for('editprofile'))
    return render_template('templates/editprofile.html', username=username1, nav=nav)


# TODO: Reflect profile changes in database
# TODO: Rewrite for LoginManager
# Set directory for editing profiles
@app.route('/editprofile/', methods=['GET', 'POST'])
def editprofile(username):
    nav = forms.Nav()
    form = forms.EditProfileForm()
    return render_template('editprofile.html', username=username, form=form, nav=nav)



# TODO: Register user in database
# TODO: Rewrite for LoginManager
# Set directory for registration
@app.route('/register/', methods=['GET', 'POST'])
def registration():
    if session.get('logged-in'):
        return redirect(url_for('index'))
    form = forms.RegistrationForm()
    nav = forms.Nav()
    return render_template('register.html', form=form, nav=nav)


# TODO: Rewrite for LoginManager
# Set directory for changing Email
@app.route('/editprofile/<username>/change-email/', methods=['GET', 'POST'])
def changeEmail(username):
    return render_template('change-email.html', username=username, nav=nav)


@app.route('/impressum')
def impressum():
    nav = forms.Nav()
    return render_template('includes/_impressum.html', nav=nav)

def dropdown():
    nav = forms.Nav()
    
    #if nav.dropdown.data = 1:
       #return redirect(url_for('editprofile'))


if __name__ == '__main__':
    app.run(debug=True)
