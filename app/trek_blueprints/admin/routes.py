"""Routes for the admin blueprint."""

#!CRITICAL THIS ROUTE WILL CONTAIN SESSIONS AND AUTHENTICATION

#First I must import the blueprint object
from flask import render_template, redirect, flash, g, session
from sqlalchemy.exc import IntegrityError

from app.trek_blueprints.admin import admin_bp
# import the forms here
from app.trek_blueprints.admin.forms.signup import AddUserForm
from app.trek_blueprints.admin.forms.login import LoginForm
# import database models and instances here
from app.trek_blueprints.admin.models.user import User, DEFAULT_IMAGE_URL
from app.extensions import db

CURR_USER_KEY = "curr_user"

#********** User Routes **********#

#!Todo must implement a method to store the user as g in the session
# Store the logged in user in Flask global
@admin_bp.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None

# **This is a helper function that is used in the login and logout routes. It is not a route itself.
def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@admin_bp.route('/admin')
def show_admin():
    """Displays the admin page."""
    users = User.query.limit(10).all()
    return render_template('/admin/index.html', users=users)

# Todo implements a route for a user to signup
@admin_bp.route('/admin/users/signup')
def show_signup():
    """Displays the signup page."""
    signup_form = AddUserForm()
    return render_template('/admin/users/signup.html', form=signup_form)

#Todo create a post route for the user signup that handles the authentication method available on the classmethod signup
@admin_bp.route('/admin/signup', methods=['POST'])
def handle_signup_form():
    """Creates a new user and adds them to the database."""
     
    form = AddUserForm()
    if form.validate_on_submit():   
        try:
            new_user = User.signup(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            avatar = form.avatar.data,
            bio = form.bio.data
            )
            
            db.session.add(new_user)
            db.session.commit()
            do_login(new_user)
            # *Currently setting up a dummy route to test the form 

            return redirect('/admin/users/secret.html')

        except IntegrityError:
            print('IntegrityError')
            # Integrate the flash messages into the form
            # if User.query.filter_by(username=username).first() is not None:
            #     flash("Username already taken", 'danger')
            # elif User.query.filter_by(email=email).first() is not None:
            #     flash("Email already taken", 'danger')
            # Indicate what went wrong  with the form
        
        return redirect('/admin/signup', form=form)
    
    
@admin_bp.route('/admin/users')
def test():
    return render_template('admin/users/secret.html')

#Todo create a route for the user to login
@admin_bp.route('/admin/users/login')
def show_login():
    """Displays the login page."""
    login_form = LoginForm()
    return render_template('/admin/users/login.html', form=login_form)

#TODO 
#!UPDATE THIS ROUTE TO HANDLE GLOBAL USER OBJECT 
@admin_bp.route('/admin/users/login', methods=['POST'])
def handle_login_form():
    """Handles user authentication and authorization."""
    
    form = LoginForm()
    try:
       if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data        
        user = User.authenticate(username=username, email=email, password=password)
        
        if user:
            flash('You have successfully logged in!')
            return redirect('/admin/users')
        else:
            flash('Invalid username or password. Please try again.')
            return redirect('/admin/users/login')
        
    except IntegrityError:
        # ?How can error handling be done better here?
        # if the email is not found in the database we will return a message to the user 
        if User.query.filter_by(email=email).first() is None:
            flash("Email not found", 'danger')
            return render_template('users/login.html', form=form)
        if User.query.filter_by(username=username).first() is None:
            flash("Username not found", 'danger')
            return render_template('users/login.html', form=form)
        if User.query.filter_by(password=password).first() is None:
            flash("Incorrect password", 'danger')
            return render_template('users/login.html', form=form)
        return redirect('/admin/users/login')
   
    
    
    
#Todo create a route for the user to logout
#!in order to logout the user, you must clear the session
#*Would be best to make a g.user object that stores the user's information that can be accessed throughout the app
#*A great deal of this application particularly post and engagement routes will require the user to be logged in so a g.user object would be useful
# @admin_bp.route('/admin/users/logout')



    
    