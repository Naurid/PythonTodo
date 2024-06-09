FILEPATH = "Files/Todos.txt"

def GetList(fileName = FILEPATH):
    with open(fileName, "r") as file:
        list = file.readlines()
        file.close()
        return list

def WriteList(listToWrite, fileName = FILEPATH):
    with open(fileName, "w") as file:
        file.writelines(listToWrite)
        file.close()


def GetIndex(userAction):
    index = int(input(f"Write the index of the task you wish to {userAction}: "))
    index -= 1
    return index