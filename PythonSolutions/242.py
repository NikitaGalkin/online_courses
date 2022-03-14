import os
import os.path

def check_contains(path):
	for elem_index in range(len(answer)):
		if (answer[elem_index] == path):
			return False
	return True


def find_all_paths(current_path):
	current_list = os.listdir(current_path)

	for elem in current_list:
		if (os.path.splitext(elem)[1] == ".py"):
			if (check_contains(current_path)):
				answer.append(current_path)
		elif (os.path.splitext(elem)[1] == ""):
			find_all_paths(current_path + "/" + elem)

answer = []
find_all_paths("main")
answer.sort()

for elem in answer:
	elem.replace('/', '\\')

with open("answers242.txt",  "w") as w:
	for line in answer:
		w.write(line + "\n")