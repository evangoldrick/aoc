def isDuplicate(s:str) -> bool:
    counts = set()
    for i in s:
        if i in counts:
            return True
        else:
            counts.add(i)
    return False

def getMarkerIndex(text:str, markerLength:int) -> int:
    finalIndex = 0
    for i in range(len(text) - markerLength):
        if not isDuplicate(text[i:i+markerLength]):
            finalIndex = i + markerLength
            break
    return finalIndex

def main():
    text = ""
    with open("input.txt", "r") as inFile:
        text = inFile.readline()

    p1Index = getMarkerIndex(text, 4)
    if p1Index == 0:
        print("Packet not found")
    else:
        print(p1Index)

    p2Index = getMarkerIndex(text, 14)
    if p2Index == 0:
        print("Packet not found")
    else:
        print(p2Index)

if __name__ == "__main__":
    main()