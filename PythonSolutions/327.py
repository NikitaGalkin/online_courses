import sys
import re

for line in sys.stdin:
	line = line.rstrip()
	line_elems = line.split(" ")

	for elem in line_elems:
		state = True
		for i in range(len(elem)):
			if (elem[i] != "a" or elem[i] != "A"):
				state = False
				break
		
		if (state):
			elem = "argh"
			break
	print(line_elems.join(" "))


for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(r"\ba+\b", "argh", line, 1, flags=re.IGNORECASE))