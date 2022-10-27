currentFloor = 0
basementFloor = None

with open("input.txt", "r") as inFile:
    text = inFile.read()

for i in range(len(text)):
    if text[i] == "(":
        currentFloor += 1
    elif text[i] == ")":
        currentFloor -= 1

    if currentFloor == -1 and basementFloor == None:
        basementFloor = i

print(basementFloor)