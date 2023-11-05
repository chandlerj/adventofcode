from data import puzzle

testInput = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def findDirUnder100k(log: str) -> int:
    splitLog = log.split("\n")
    directories = {}
    Pwd = []
    for line in splitLog:
        splitLine = line.split(" ")
        if line.startswith("$ cd"):
            directory = splitLine[2]
            if directory == "..":
                Pwd.pop() # remove the last thing appended to the current dir
            else:
                Pwd.append(directory)
                if str(Pwd) not in directories:
                    directories[str(Pwd)] = 0
        if splitLine[0].isdigit():
            # create new list, append one directory at a time, 
            # update sizes of directories in dictionary
            tempList = []
            for directory in Pwd:
                tempList.append(directory)
                directories[str(tempList)] += int(splitLine[0])
    directoryTotals = list(directories.values())
    sumUnder100k = 0
    for value in directoryTotals:
        if value <= 100000:
            sumUnder100k += value
    return sumUnder100k


def findDirToDelete(log: str) -> int:
    splitLog = log.split("\n")
    directories = {}
    Pwd = []
    for line in splitLog:
        splitLine = line.split(" ")
        if line.startswith("$ cd"):
            directory = splitLine[2]
            if directory == "..":
                Pwd.pop() # remove the last thing appended to the current dir
            else:
                Pwd.append(directory)
                if str(Pwd) not in directories:
                    directories[str(Pwd)] = 0
        if splitLine[0].isdigit():
            # create new list, append one directory at a time, 
            # update sizes of directories in dictionary
            tempList = []
            for directory in Pwd:
                tempList.append(directory)
                directories[str(tempList)] += int(splitLine[0])
    
    directoryTotals = list(directories.values())

    TOTAL_STORAGE_AVAILABLE = 70000000
    SPACE_REQUIRED_FOR_UPDATE = 30000000
    totalSpaceUsed = directories["['/']"] 
    unusedSpace = TOTAL_STORAGE_AVAILABLE - totalSpaceUsed
    spaceNeeded = SPACE_REQUIRED_FOR_UPDATE - unusedSpace
    print(f'total space used: {totalSpaceUsed}; space available {unusedSpace}\nspace needed for update: {spaceNeeded}')
    currentDelDirSize = TOTAL_STORAGE_AVAILABLE
    for value in directoryTotals:
        if value >= spaceNeeded and value < currentDelDirSize:
            currentDelDirSize = value
    return currentDelDirSize 

        
# print(findDirUnder100k(testInput))
print(findDirToDelete(puzzle))
