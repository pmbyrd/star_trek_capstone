"""Routes for the admin blueprint."""

#!CRITICAL THIS ROUTE WILL CONTAIN SESSIONS AND AUTHENTICATION

#First I must import the blueprint object
from flask import render_template, redirect, flash
from app.trek_blueprints.admin import admin_bp
# import the forms here
from app.trek_blueprints.admin.forms.signup import AddUserForm
# import database models and instances here
from app.trek_blueprints.admin.models.user import User, DEFAULT_IMAGE_URL
from app.extensions import db

@admin_bp.route('/admin')
def show_admin():
    """Displays the admin page."""
    users = User.query.limit(10).all()
    return render_template('/admin/index.html', users=users)

# Todo implements a route for a user to signup
@admin_bp.route('/admin/signup')
def show_signup():
    """Displays the signup page."""
    signup_form = AddUserForm()
    return render_template('/admin/signup.html', form=signup_form)

#Todo create a post route for the user signup that handles the authentication method available on the classmethod signup
@admin_bp.route('/admin/signup', methods=['POST'])
def handle_signup_form():
    """Creates a new user and adds them to the database."""
    
    form = AddUserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        avatar = form.avatar.data
        bio = form.bio.data
        
        new_user = User.signup(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar or DEFAULT_IMAGE_URL,
            bio=bio
        )
        
        db.session.add(new_user)
        db.session.commit()
        # import pdb; pdb.set_trace()
        return redirect('/admin/users/secret.html')
        # *Currently setting up a dummy route to test the form
    else:
        return redirect('/admin/signup')
    
    
@admin_bp.route('/admin/users')
def test():
    return render_template('admin/users/secret.html')

    