from datetime import datetime
from random import uniform


def get_random_datetime(year_gap=5):
    """Get a random datetime within the last few years."""

    now = datetime.now()
    then = now.replace(year=now.year - year_gap)
    random_timestamp = uniform(then.timestamp(), now.timestamp())

    return datetime.fromtimestamp(random_timestamp)

import hashlib
import random

def generate_avatar(email, size=80):
    # Calculate the email hash
    email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()

    # Choose a random default avatar image
    default_avatars = [
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp', # Mystery person
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=identicon', # Geometric pattern
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=monsterid', # Monster
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=robohash', # Robot
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=wavatar', # Cartoon face
    ]
    default_avatar = random.choice(default_avatars)

    # Construct the Gravatar URL
    url = f'https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default_avatar}'

    return url

