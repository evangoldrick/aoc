def interperateStacks(diagram:list) -> dict:
    columns = {int(i):list() for i in diagram[-1].split("   ")}
    for layer in reversed(diagram[:-1]):
        coulumnDataList = [layer[i:i+4].strip(" []") for i in range(0, len(layer), 4)]
        for colNum in columns.keys():
            if coulumnDataList[colNum - 1] != "":
                columns[colNum].append(coulumnDataList[colNum - 1])

    return columns




inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip("\n"))

moveSectionStart = 0

for lineNum in range(len(inputArray)):
    if inputArray[lineNum].strip() == "":
        moveSectionStart = lineNum


stacks = interperateStacks(inputArray[:moveSectionStart])

for lineNum in range(moveSectionStart + 1, len(inputArray)):
    lineData = inputArray[lineNum].split(" ")

    numReps = int(lineData[1])
    fromStack = int(lineData[3])
    toStack = int(lineData[5])

    for i in range(numReps):
        stacks[toStack].append(stacks[fromStack].pop())


answerString = ""
for col in sorted(stacks.keys()):
    answerString += stacks[col][-1]

print(answerString)
