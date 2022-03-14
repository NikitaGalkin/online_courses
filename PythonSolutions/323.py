import sys

for line in sys.stdin:
    line = line.rstrip()
    
    for i in range(len(line) - 4):
        if (line[i] == "z" and "z" == line[i + 4]):
            print(line)
            break