import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    
    if re.search(r'\b(.+)\1\b', line):
        print(line)