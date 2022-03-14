class Error:
	def __init__(self, name):
		self.name = name
		self.kids = []
		self.appearance = 0

	def add_error(self, error):
		self.kids.append(error)

def find_error(error_name):
	for i in range(len(our_errors)):
		if (our_errors[i].name == error_name):
			return our_errors[i]
	return -1

def get_placement_error(error):
	for i in range(len(our_errors)):
		if (error.name == our_errors[i].name):
			return i;

def find_child_rec(err_index, current_node_name):
	for kid_index in range(len(our_errors[err_index].kids)):
		if (our_errors[err_index].kids[kid_index].name == current_node_name):
			return True
		if (find_child_rec(get_placement_error(our_errors[err_index].kids[kid_index]), current_node_name)):
			return True
	return False
		

def find_used_parent(current_node_name):
	
	for err_index in range(len(our_errors)):
		if (find_child_rec(err_index, current_node_name) and our_errors[err_index].appearance > 0):
			return True
	return False

n = int(input())
input_text = ""
our_errors = []

for i in range(n):
	input_text = input().split(" : ")
	current_error = input_text[0]
	parent_error = ""

	current_error_class = find_error(current_error)
	if (current_error_class == -1):
		current_error_class = Error(current_error)
		our_errors.append(current_error_class)

	if (len(input_text) > 1):
		parent_errors = input_text[1].split(" ")

		for parent_error in parent_errors:
			if (find_error(parent_error) == -1):
				parent_err_class = Error(parent_error)
				our_errors.append(parent_err_class)

			find_error(parent_error).add_error(current_error_class)
		
k = int(input())
input_text = ""

for i in range(k):
	input_text = input()

	find_error(input_text).appearance += 1

	if (find_used_parent(input_text)):
		print(input_text)


