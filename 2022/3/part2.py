def findCommonChar(first, second, third):
    comparisonDict = dict()
    comparisonDict2 = dict()
    for character in first:
        comparisonDict[character] = 1

    for character in second:
        if character in comparisonDict.keys():
            comparisonDict2[character] = 1
    
    for character in third:
        if character in comparisonDict2.keys():
            return character

def getCharacterVal(character: str):
    val = ord(character)

    if ord("a") <= val <= ord("z"):
        val -= ord("a") - 1
    elif ord("A") <= val <= ord("Z"):
        val -= ord("A") - 1 - 26
    else:
        print(character)
        return None
    return val

inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip())

prioritySum = 0

grouped = list()
for lineNum in range(0, len(inputArray), 3):
    print(lineNum)
    grouped.append([inputArray[lineNum], inputArray[lineNum + 1], inputArray[lineNum + 2]])

for lines in grouped:
    print(lines)
    
    commonChar = findCommonChar(lines[0], lines[1], lines[2])
    prioritySum += getCharacterVal(commonChar)
print(prioritySum)
