import sys
import re

for line in sys.stdin:
	line = line.rstrip()
	new_line = ""

	for i in range(len(line) - 1):
		if (line[i] != line[i + 1]):
			new_line += line[i]

	if (new_line[len(new_line) - 1] != line[len(line) - 1]): new_line += line[len(line) - 1]
	print(new_line)

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'\b(.+)\1\b', line):
        print(line)

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"(\w)(\1)+", r"\1", line))