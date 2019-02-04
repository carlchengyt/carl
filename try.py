def contains(list1,list2):
    length1 = len(list1)
    length2 = len(list2)
    for n1 in range (0,(int(length1)-int(length2))+1):
        counter = 0
        if length1>=length2:
            for n2 in range (0,int(length2)):
                if list1[n1+n2] == list2[n2]:
                    counter+=1
        if counter == length2:
            return True
    return False


def inputUI():
    print("Welcome to Chore Chart\n\n"
          + "   About                   (A)\n"
          + "   Create Household        (C)\n"
          + "   View Household          (V)\n"
          + "   Log Chores Done         (L)\n"
          + "   Show Leaderboard        (S)\n"
          + "   Quit                    (Q)\n\n")

    return input("   Please choose an option and press <Enter> : ")


def createHousehold():
    household_name = input("Enter the household name: ")
    ifcontains = contains(household_name_list,household_name)
    participants = []
    chores = []
    timesPerWeek = []

    # get participants' names
    print("\nEnter participants' names: \n\n")
    # assuming Maximum of ten participants in a household
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        person = str(input("    Enter the name of participant " + str(i) + ":"))
        if person != "":
            participants.append(person)
        else:
            break

    # get chores
    print("\nEnter Chores: \n")
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        chore = str(input("     Chore " + str(i) + ":"))
        if chore != "":
            chores.append(chore)
            # get times per week
            time_input = str(input("         Times per week: "))
            while int(time_input) <= 0:
                time_input = str(input("         Please enter a valid time:"))
            timesPerWeek.append(time_input)

        else:
            break
    if ifcontains == False:
        household_name_list.append(household_name)
        householdInfo.append(timesPerWeek)
        householdInfo.append(chores)
        householdInfo.append(participants)
        householdInfo.append(household_name)
    else:
        position = household_name_list.index(household_name)
        householdInfo.pop(position*4)
        householdInfo.insert(position*4,timesPerWeek)
        householdInfo.pop(position * 4+1)
        householdInfo.insert(position * 4+1, chores)
        householdInfo.pop(position * 4+2)
        householdInfo.insert(position * 4+2, participants)
        householdInfo.pop(position * 4+3)
        householdInfo.insert(position * 4+3, household_name)

    return householdInfo


def viewHousehold(householdInfo,inputname):
    if household_name_list == []:
        print("\n\nPlease create a household first(C)")
        return
    if contains(household_name_list,inputname)==False:
        print("\n\nPlease enter a correct household name")
        return
    number_of_households=len(household_name_list)
    n = int(household_name_list.index(inputname))
    print("\n")
    print(household_name_list[n])
    print("\n\n")


    print("Participants: \n")
    index = 1
    for i in householdInfo[2+4*n]:
        print("     " + str(index) + ". " + i)
        index += 1
    print("\n")


    print("Weekly Chores: \n")
    index = 1
    for i in householdInfo[1+4*n]:
        time = householdInfo[0+4*n][index - 1]
        print("     " + str(index) + ". " + i + " (" + str(time) + ")")
        index += 1
    input("\n\nPress enter to return to main menu")

householdInfo=[]
household_name_list=[]
choice = inputUI()
info = []
iteration = 1
while choice != 'Q':
    print("\n\n")
    if(iteration != 1):
        choice = inputUI()
    iteration += 1

    if choice == 'A':
        print("Thank you for using our chore chart\nCheck the function from the table below \nType in Capital letters to activate each function")
    if choice == 'C':
        info = createHousehold()
        continue
    if choice == 'V':
        inputname=str(input("\nEnter the name you want to check:"))
        viewHousehold(info,inputname)
        continue