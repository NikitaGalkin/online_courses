import sys

def check_tandem(line):
    if (len(line) % 2 == 0):
        if (line[:len(line)//2] == line[len(line)//2:]):
            return True
    return False

for line in sys.stdin:
    line = line.rstrip()
    line_elems = line.split(" ")

    for elem in line_elems:
        if check_tandem(elem):
            print(line)
            break