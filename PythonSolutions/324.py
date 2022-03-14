import sys

for line in sys.stdin:
    line = line.rstrip()
    
    for i in range(len(line)):
        if (line[i] == "\\"):
            print(line)
            break