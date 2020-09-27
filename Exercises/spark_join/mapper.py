#!/usr/bin/env python

import sys
import json

for line in sys.stdin:
  line = line.strip()
  j = json.loads(line)
  print "%s\t%s" % (j['user_id'], line)
