import sys

for line in sys.stdin:
    line = line.rstrip()
   
    for i in range(len(line) - 2):
        if (line[i:i + 3] == "cat"):
            counter += 1
    if (counter >= 2):
        print(line)

#catcat
#cat and cat
#catac
#cat
#ccaatt