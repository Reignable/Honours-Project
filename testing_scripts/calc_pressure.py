#! /usr/bin/env python
import sys

movement = float(sys.argv[1])
result = (0.265 * movement ** 2) - (18.771 * movement) + 442
print result
