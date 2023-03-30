"""This is a module for seeding the database with users."""

import random
import string
from app.extensions import db
from app.trek_blueprints.admin.models.user import User, DEFAULT_IMAGE_URL

def seed_users():
    # Define a list of random first and last names to choose from
    db.drop_all()
    db.create_all()
    
    first_names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Hannah", "Isabella", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

    # Create 10 random users
    for i in range(10):
        # Generate a random username and email
        username = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        email = f"{username}@example.com"
        
        # Choose a random first and last name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        # Generate a random password
        password = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        
        # Generate a random bio
        bio = "".join(random.choices(string.ascii_letters + string.digits, k=50))
        
        # Create a new user with the generated data
        user = User(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            avatar=DEFAULT_IMAGE_URL,
            bio=bio
        )
        
        # Add the user to the database
        db.session.add(user)
        
    # Commit the changes to the database
    db.session.commit()


