class namespace:
	def __init__(self, name):
		self.name = name
		self.kids = []
		self.variables = []
		
	def add_one(self, variable):
		self.variables.append(variable)

def create_namespace(name, parent_name):
	for elem in our_namespaces:
		if (elem.name == parent_name):
			new_namespace = namespace(name)
			our_namespaces.append(new_namespace)
			elem.kids.append(new_namespace)

def get_namespace(current_namespace_name, variable):
	for i in range(len(our_namespaces)):
		if (our_namespaces[i].name == current_namespace_name):
			for j in range(len(our_namespaces[i].variables)):
				if (our_namespaces[i].variables[j] == variable):
					return current_namespace_name

			for j in range(len(our_namespaces)):
				for k in range(len(our_namespaces[j].kids)):
					if (our_namespaces[j].kids[k].name == current_namespace_name):
						current_result_namespace = get_namespace(our_namespaces[j].name, variable)
						if (current_result_namespace != ""):
							return current_result_namespace
	return ""

def find_namespace(namespace_name):
	for i in range(0, len(our_namespaces)):
		if (our_namespaces[i].name == namespace_name):
			return True
	return False


our_namespaces = []
n = int(input())
input_text = ""

for i in range(0, n):
	input_text = input().split(" ")

	if (input_text[0] == "get"):
		answer = get_namespace(input_text[1], input_text[2])

		if (answer != ""):
			print(answer)
		else:
			print("None")
	elif (input_text[0] == "create"):
		if (not find_namespace(input_text[2])):
			our_namespaces.append(namespace(input_text[2]))
		create_namespace(input_text[1], input_text[2])
	else:
		if (not find_namespace(input_text[1])):
			our_namespaces.append(namespace(input_text[1]))

		for j in range(0, len(our_namespaces)):
			if (our_namespaces[j].name == input_text[1]):
				our_namespaces[j].add_one(input_text[2])
		
#print("All info:")

#for i in range(len(our_namespaces)):
#	print()
#	print(our_namespaces[i].name, end = "\nKIDS: ")
#	for j in range(len(our_namespaces[i].kids)):
#		print(our_namespaces[i].kids[j].name, end = " ")
#	print("\nViriables: ", end = "")
#	for j in range(len(our_namespaces[i].variables)):
#		print(our_namespaces[i].variables[j], end = " ")
#	print()