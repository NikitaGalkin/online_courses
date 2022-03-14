class Node:
    def __init__(self, name):
        self.name = name
        self.kids = []
        
    def add_one(self, node):
        self.kids.append(node)

global current_kid

def find_class(node):
    for elem in our_nodes:
        if (elem.name == node):
            return elem
    return -1;

def find_kid(current_node):
    #print("Current node >> ", end = "")
    #print(current_node.name)

    if (current_node.name == current_kid.name):
        return True
    
    for i in range(0, len(our_nodes)):
        if (our_nodes[i].name == current_node.name):
            for kid in our_nodes[i].kids:
                if find_kid(kid):
                    return True
    
    return False

amount_of_classes = int(input())
name_of_class = ""
our_nodes = []

for i in range(0, amount_of_classes):
    input_text = input()
    name_of_class = input_text.split(" : ")[0]
    current_node = Node(name_of_class)
    if (find_class(name_of_class) == -1):
        our_nodes.append(current_node)

    if (len(input_text.split(" : ")) > 1):
        for class_elem in (input_text.split(" : ")[1]).split(" "):
            if (find_class(class_elem) != -1):
                find_class(class_elem).add_one(current_node)
            else:
                created_node = Node(class_elem)
                our_nodes.append(created_node)
                created_node.add_one(current_node)

#print("Current success >>")
#for elem in our_nodes:
#    print(elem.name, end = ": ")
#    for kid in elem.kids:
#        print(kid.name, end = " ")
#    print()

amount_of_calls = int(input())

for i in range(0, amount_of_calls):
    input_text = input().split(" ")
    sus_par_text, sus_kid_text = input_text[0], input_text[1]
    sus_par, sus_kid = find_class(sus_par_text), find_class(sus_kid_text)

    current_kid = sus_kid

    if (sus_par == sus_kid):
        print("Yes")
    elif (sus_par == -1 or sus_kid == -1):
        print("No")
    else:
        #print("here")
        if find_kid(sus_par):
            print("Yes")
        else:
            print("No")