currentFloor = 0
with open("input.txt", "r") as inFile:
    text = inFile.read()

for i in range(len(text)):
    if text[i] == "(":
        currentFloor += 1
    elif text[i] == ")":
        currentFloor -= 1

print(currentFloor)