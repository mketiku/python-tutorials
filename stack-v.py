#! /usr/bin/env/python3

memberList = []
# get first menu selection from user and store in control value variable


class MemberList():
    '''
    Problem from stackoverflow.
    '''
    def __init__(self, name, phone, number):
        self.__name = name
        self.__phone = phone
        self.__number = number


    def setName(self, name):
        self.__name = name


    def setPhone(self, phone):
        self.__phone = phone


    def setnumber(self, number):
        self.__number = number


    def getName(self):
        return self.__name


    def getPhone(self):
        return self.__phone


    def getNumber(self):
        return self.__number


    def displayData(self):
        print("")
        print("Player's Information")
        print("-------------------")
        print("Player's Name:", self.getName)
        print("Player's Telephone number:", self.getPhone)
        print("Player's Jersey number:", self.getNumber)


    def displayMenu():
        print("==========Main Menu==========")
        print("1. Display Team Roster")
        print("2. Add Member")
        print("3. Remove Member")
        print("4. Edit Member")
        print("9. Exit Program")
        print()
        return int(input("Selection>"))
    menuSelection = displayMenu()


    def printMembers(memberList):
        print("Current members: ")
        if len(memberList) == 0:
            print("No current members in memory.")
        else:
            x = 1
            while x < len(memberList):
                print(memberList[x],)
                x = x + 1


    def addPlayer(memberList):  # players as an argument
        newName = input("Add a player's Name: ")
        newPhone = input("Telephone number: ")
        newNumber = input("Jersey number: ")
        memberList.append(newName)
        return memberList


    def removePlayer(memberList):
        removeName = input("What name would you like to remove? ", )
        # Don't redefine it!
        if removeName in memberList:
            del memberList[removeName]
        else:
            print("Sorry", removeName, "was not found!")
        return memberList


    def editPlayer(memberList):
        oldName = input("What name would you like to change? ", )
        if oldName in memberList:
            newName = input("What is the new name? ")
            print("***", oldName, "has been changed to", newName)
        else:
            print("***Sorry", oldName, "was not found!")
        return memberList


    def saveData(memberList):
        filename = input("Filename to save: ", )
        print("saving data...")
        outfile = open(filename, "wt")
        filename = '/Users\nativ\ Documents'
        for x in memberList:
            name = memberList[x].getName()
            phone = memberList[x].getPhone()
            number = memberList[x].getNumber()
            outfile.write("name", "age", 'number')
        print("Data Saved")
        outfile.close()


    def loadData():
        filename = input("Filename to load: ")
        inFile = open(filename, "rt")


    def exitProgram(memberList):
        print("Exiting Program...")
    while menuSelection != 9:
        if menuSelection == 1:
            printMembers = printMembers(memberList)
            menuSelection = displayMenu()
        elif menuSelection == 2:
            memberList = addPlayer(memberList)
            menuSelection = displayMenu()
        elif menuSelection == 3:
            memberList = removePlayer(memberList)
            menuSelection = displayMenu()
        elif menuSelection == 4:
            memberList = editPlayer(memberList)
            menuSelection = displayMenu()
        elif menuSelection == 5:
            memberList = saveData(memberList)
            menuSelection = displayMenu()
        elif menuSelection == 6:
            memberList = loadData()
        menuSelection = displayMenu()
    print('Welcome to the Team Manager')
    displayMenu()


# member_instance = MemberList()