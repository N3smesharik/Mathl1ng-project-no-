from pathlib import Path
import os
import re
i = input("Please enter 1, if you are a student, or 2, if you are a teacher\n")
if i == "1":
    print("Under construction\n")
else:
    while True:
        i = input("What are you want to do? Enter 1, if you are want to add a new discipline, 2, if you are want to add a new question, 3, if you are want to see a text of questions 4, if you are want to exit\n")
        if i == "1":
            Discip = input("Enter the name of discipline\n")
            if not os.path.isdir(Discip):
                os.mkdir(Discip)
            else:
                print("Sorry, but this discipline has been created early\n")
        if i == "2":
            Discip = input("Enter the name of discipline\n")
            if not os.path.isdir(Discip):
                print("Error: there is no discipline with this name\n")
            Quest = input("Enter the number of question\n")
            if not os.path.isdir(Discip):
                print("Error: there is no discipline with this name\n")
            else:
                os.chdir(Discip)
                f = open(Quest, "w")
                Text = input("Enter the question")
                p = re.search("[\d]\)", Text[0:4])
                if (Text[-1] != 0 and Text[-1] != 1) or (p == 0):
                    print("Error: incorrect format")
                    continue
                f.write(Text)
                k = 1
                while True:
                    s1 = input("Enter the answer: enter 0 after the question if true or 1 if false. Enter 2 when you are stopped\n")
                    if s1 == "2":
                        f.close()
                        break
                    f.write(str(k) + ") " + s1 + "\n")
        if i == "3":
            Discip = input("Enter the name of discipline\n")
            if not os.path.isdir(Discip):
                print("Error: there is no discipline with this name\n")
                continue
            os.chdir(Discip)
            Quest = input("Enter the number of question\n")
            if not os.path.isfile(Quest):
                print("Error: there is no question with these number")
                continue
            f  = open(Quest, "r")
            print(f.read())
        if i == "4":
            break
