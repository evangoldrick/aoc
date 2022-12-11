def splitRange(r:str):
    ret = r.split("-")
    ret = [int(i) for i in ret]
    return ret

def containsRange(left:str, right:str):
    l = splitRange(left)
    r = splitRange(right)
    if l[0] <= r[0] and l[1] >= r[1] or l[0] >= r[0] and l[1] <= r[1]:
        return True
    else:
        return False

inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip())

containsCount = 0
for line in inputArray:
    first, second = line.split(",")
    if containsRange(first, second):
        containsCount += 1




print(containsCount)
print("tests")
print(containsRange("1-9", "2-3"))
print(containsRange("1-9", "1-9"))


