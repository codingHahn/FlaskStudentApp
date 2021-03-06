from flask import  render_template, session, redirect, url_for, escape, request, flash
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, models, forms, db
from app.models import User

# TODO: GDPR compliance
#       - cookie prefs.
#       - account deletion

# Landing Page Logic
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = forms.LoginForm()
    '''Checks if the user is logged in and ajusts the user variable accordingly'''
    if current_user.is_authenticated:
        form = forms.LoginForm()
        return render_template('home.html', username=current_user.surname, form=form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
            login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index') 

        flash('Login requested for user {}')
        return redirect(next_page)
    return render_template('home.html', username='nobody', form=form)

  
# Login logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index') 

        flash('Login requested for user {}, remember_me={}'.format(form.email.data, form.remember_me.data))
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# TODO: Rewrite for LoginManager
@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('index'))

    flash("You are currently not logged in.")
    return redirect(url_for('index'))


# TODO: Show only profiles of existing users
# TODO: Rewrite for LoginManager

@login_required
@app.route('/user')
def profile():
    form = forms.EditProfileForm()
    return render_template('profile.html', user=current_user, form=form)



# TODO: Reflect profile changes in database
# TODO: Rewrite for LoginManager
# Set directory for editing profiles


@login_required
@app.route('/editprofile/', methods=['GET', 'POST'])
def editprofile():
    form = forms.EditProfileForm()
    if form.validate_on_submit():
        return redirect(url_for('profile'))
    return render_template('editprofile.html', form=form)



# Set directory for registration
@app.route('/register/', methods=['GET', 'POST'])
def registration():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        u = User(firstname=form.firstname.data, surname=form.surname.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

# TODO: Rewrite for LoginManager
# Set directory for changing Email

@login_required
@app.route('/change-email/', methods=['GET', 'POST'])
def changeEmail():
    form = forms.EditEmailForm()
    #if form.validate_on_submit:
       # current_user.email = form.email.data
    return render_template('change-email.html', username=current_user.firstname, form=form)


@app.route('/impressum')
def impressum():
    return render_template('includes/_impressum.html')

if __name__ == '__main__':
    app.run(debug=True)
