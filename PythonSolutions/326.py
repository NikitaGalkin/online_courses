import sys

for line in sys.stdin:
	line = line.rstrip()

	print(line.replace("human", "computer"))