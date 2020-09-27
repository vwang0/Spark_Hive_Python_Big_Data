# SQL for Marekters: Dominate data analytics, data science, and big data

from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future

import sys
import random

NAMES = ['Alice', 'Bob', 'Carol', 'Dave', 'Emily', 'Frank', 'Gina']
PRODUCTS = ['Apple', 'Orange', 'Banana', 'Blueberry', 'Raspberry', 'Apricot', 'Cherry', 'Grape', 'Mango']
ACTIONS = ['view', 'addtocart', 'purchase']

def generate(N, fn):
    with open(fn, 'w') as f:
        i = 0
        while i < N:
            name = random.choice(NAMES)
            product = random.choice(PRODUCTS)
            # action = random.choice(ACTIONS)
            price = str(0.99)

            # make sure every purchase has an addtocart and view
            # make sure every addtocart has a view
            a = random.randint(1, 3)
            for j in range(a):
                action = ACTIONS[j]
                f.write("%s,%s,%s,%s\n" % (name, product, action, price))
                i += 1


if __name__ == '__main__':
    generate(int(sys.argv[1]), sys.argv[2])
