scores = {
"X": {"A":3,"B":1,"C":2},
"Y": {"A":1 + 3,"B":2 + 3,"C":3 + 3},
"Z": {"A":2 + 6,"B":3 + 6,"C":1 + 6}}


inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip())


playerTotalScore = 0
for i in inputArray:
    moves = i.split(" ")
    playerTotalScore += scores[moves[1]][moves[0]]

print(playerTotalScore)