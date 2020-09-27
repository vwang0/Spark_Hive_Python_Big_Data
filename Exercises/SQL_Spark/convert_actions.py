# SQL for Marekters: Dominate data analytics, data science, and big data

import json

with open('big_actions.json', 'w') as f:
    for line in open('big_actions.csv'):
        r = line.split(',')
        j = {
            'name': r[0],
            'product': r[1],
            'action': r[2],
            'price': r[3],
        }
        f.write("%s\n" % json.dumps(j))
