import sys

rows = []
with open(sys.argv[1], "r") as inFile:
    rows.append(inFile.readline())

for y in range(len(rows)):
    for x in range(len(rows[x])):
