my_array = []

with open("test.txt") as f:
	for line in f:
		my_array.append(line.rstrip())

my_array.reverse()

with open("test.txt") as f, open("test_copy.txt",  "w") as w:
	for line in my_array:
		w.write(line + "\n")
