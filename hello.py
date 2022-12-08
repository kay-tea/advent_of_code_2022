

def readFile():
    with open('numbers.txt') as file:
        lines = file.readlines()
        listofElves = []
        oneElfBoi = []
        for i in lines:
            if i != "\n":
                oneElfBoi.append(int(i))
            else:
                listofElves.append(oneElfBoi)
                oneElfBoi = []
                pass
        return listofElves

def findHighestCals(elfList):
    highestNum = 0
    for i in elfList:
        if sum(i) > highestNum:
            highestNum = sum(i)
    return highestNum

def findTopThree(elfList):
    listOfSums = []
    for i in elfList:
        listOfSums.append(sum(i))
    ascList = sorted(listOfSums)
    return (ascList[-1] + ascList[-2] + ascList[-3])


allElves = readFile()
highest_calories = findHighestCals(allElves)
print(f"The highest number of calories being carried by an elf is: {highest_calories}")
topThree = findTopThree(allElves)
print(f"The total number of calories the top three elves are carrying are: {topThree}")

