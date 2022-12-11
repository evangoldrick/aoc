def splitRange(r:str):
    ret = r.split("-")
    ret = [int(i) for i in ret]
    return ret

def overlaps(left:str, right:str):
    l = splitRange(left)
    r = splitRange(right)
    if r[0] <= l[0] <= r[1] or r[0] <= l[1] <= r[1] or l[0] <= r[0] <= l[1] or l[0] <= r[1] <= l[1]:
        return True
    else:
        return False

inputArray = list()
with open("input.txt", "r") as inFile:
    for i in inFile:
        inputArray.append(i.strip())

overlapsCount = 0
for line in inputArray:
    first, second = line.split(",")
    if overlaps(first, second):
        overlapsCount += 1




print(overlapsCount)
print("tests")
print(overlaps("1-9", "2-3"))
print(overlaps("1-2", "2-3"))
print(overlaps("1-3", "2-3"))
