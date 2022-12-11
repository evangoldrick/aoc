
valueXYZ = {"X":1,"Y":2,"Z":3}

def createPlayerScoreDict():
    playAmounts = {"A":dict(), "B":dict(), "C":dict()}
    for opponent in ["A", "B", "C"]:
        for player in ["X", "Y", "Z"]:
            if opponent == "A" and player == "X" or opponent == "B" and player == "Y" or opponent == "C" and player == "Z":
                playAmounts[opponent][player] = 3 + valueXYZ[player]
            elif opponent == "A" and player == "Y" or opponent == "B" and player == "Z" or opponent == "C" and player == "X":
                playAmounts[opponent][player] = 6 + valueXYZ[player]
            else:
                playAmounts[opponent][player] = valueXYZ[player]
    return playAmounts


# player rock | paper | scissors
playAmounts = createPlayerScoreDict()
print(playAmounts)


inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip())


playerTotalScore = 0
for i in inputArray:
    moves = i.split(" ")
    playerTotalScore += playAmounts[moves[0]][moves[1]]

print(playerTotalScore)