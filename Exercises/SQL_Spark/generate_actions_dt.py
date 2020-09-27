# SQL for Marekters: Dominate data analytics, data science, and big data

import sys
import random
# from datetime import datetime

NAMES = ['Alice', 'Bob', 'Carol', 'Dave', 'Emily', 'Frank', 'Gina']
PRODUCTS = ['Apple', 'Orange', 'Banana', 'Blueberry', 'Raspberry', 'Apricot', 'Cherry', 'Grape', 'Mango']

def generate(N, fn):
    with open(fn, 'w') as f:
        i = 0
        while i < N:
            name = random.choice(NAMES)
            product = random.choice(PRODUCTS)
            price = str(0.99)

            year = random.choice(['2014', '2015'])
            month = str(random.choice(range(12)) + 1)
            if len(month) == 1:
                month = "0" + month
            day = str(random.choice(range(28)) + 1)
            if len(day) == 1:
                day = "0" + day
            dt = "%s-%s-%s 00:00:00" % (year, month, day)

            f.write("%s,%s,%s,%s,%s\n" % (name, product, 'purchase', price, dt))
            i += 1


if __name__ == '__main__':
    generate(1000000, 'dt_actions.csv')
