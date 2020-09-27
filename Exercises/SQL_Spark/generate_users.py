# SQL for Marekters: Dominate data analytics, data science, and big data


import sys
import random

from generate_actions import NAMES

LOCATIONS = ['Los Angeles', 'New York', 'Chicago', 'Las Vegas']

def generate():
    with open('users.csv', 'w') as f:
        for name in NAMES:
            location = random.choice(LOCATIONS)
            age = random.randint(18, 65)
            f.write("%s,%s,%s\n" % (name, str(age), location))


if __name__ == '__main__':
    generate()
