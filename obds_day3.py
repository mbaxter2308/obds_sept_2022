
#1) Create a list called 'participants' containing the of the names of your fellow trainees

def task1():
    participants = ["dan" , "felix" , "judy" , "ayesha" , "yu" , "kinam" , "emily" , "christina" , "matt" , "nicole" , "li-hsin"]

#2) Create the following new variables participants_2 and participants_3by typing:•participants_2 = participants•participants_3 =participants.copy()

def task2():
    participants_2 = participants
    participants_3 = participants.copy()

#3) Add the names of today's trainers to the list 'participants' using append

def task3():
    participants.append("david")
    participants.append("andrea")

#4) Print the 'participants', 'participants_2' and 'participants_3' lists –what do you notice and why does this happen?

def task4():
    participants
    participants_2
    participants_3

#5) Select the 3rd and 5th names from your participants list

def task5():
    print(participants[2:5:2])

#6) Sort your list & select the 3rd to the 5th names from yourparticipantslist

def task6():
    participants.sort()
    participants
    print(participants[2:5:2])


#7) Select the first 2 letters of the string in the third value of yourparticipantslist

def task7():
    print(participants[2][0:2])

#8) Iterate over the participants list and set the names to keys in a dictionary with the value as 'trainee’ or ‘trainer’ depending on thier role.

def task8():
    dic_participants={}
    for name in participants:
        if name == "david" or name == "andrea":
            dic_participants[name] = "trainer"
        else:
            dic_participants[name] = "trainee"


        

#9) Use a for loop to iterate over your dictionary and print the values of the keys only if they are trainees

def task9():
    for name in dic_participants.keys():
        if dic_participants.get(name) == "trainee":
            print(name)

#10) Repeat exercises 1-7 but create a tuple for 'participants' in step1 instead of a list –what do you notice about thebehaviourof tuples compared to lists?

participants = ("dan" , "felix" , "judy" , "ayesha" , "yu" , "kinam" , "emily" , "christina" , "matt" , "nicole" , "li-hsin")

task5()


