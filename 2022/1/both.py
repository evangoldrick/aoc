inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip())

elfArray = list()
elfArray.append(0)

for i in inputArray:
    if i == "":
        elfArray.append(0)
    else:
        elfArray[-1] += int(i)

elfArray.sort()

print(f"Part1: {elfArray[-1]}")

print(f"Part2: {elfArray[-1] + elfArray[-2] + elfArray[-3]}")
