def findCommonChar(first, second):
    comparisonDict = dict()
    for character in first:
        comparisonDict[character] = 1

    for character in second:
        if character in comparisonDict.keys():
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
for line in inputArray:
    halfLength = int(len(line)/2)
    commonChar = findCommonChar(line[:halfLength], line[halfLength:])
    prioritySum += getCharacterVal(commonChar)
print(prioritySum)
