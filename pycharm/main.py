import re
import traceback

list_id = []
list_name = []
list_surname = []
list_age = []
list_nationalid = []
list_mail = []
list_all = []
class Record:

    def __init__(self,programName):
        self.programName = programName
        self.loop = True
        print("welcome {}.".format(programName))
    def program(self):
        while True:
            try:
                userInput = int(input ("what you want to do?\n1-addRecord\n2-removeRecord\n3-listRecord\n4-exitRecord\n"))
                if userInput < 5 and userInput > 0:
                    self.menu(userInput)
                    break
                else:
                    print("pls enter a valid number")
            except Exception as e :
                traceback.print_exc()


    def menu(self,userInput):
        self.userInput = userInput
        if  userInput == 1:
            print("addRecord is opening")
            self.addRecord()
        if userInput == 2:
            print("removeRecord is opening")
            self.removeRecord()
        if userInput == 3:
            print("list Record are opening")
            self.listRecord()
        if userInput == 4:
            self.exitRecord()

    def addRecord(self):
        while True:

            user_name = input("pls enter your name")
            if user_name.isalpha() == True:
                print ("addRecord_name worked")
                break
            else:
                print ("enter a valid name")
        while True:
            user_surname = input("pls enter your surname")
            if user_surname.isalpha() == True:
                print ("addRecord_surname worked")
                break
            else:
                print ("enter a valid surname")
        while True:
            user_age = input("pls enter your age")
            if user_age.isdigit() == True:
                print ("addRecord_age worked")
                break
            else:
                print ("enter a valid age")
        while True:
            user_nationalid = input("pls enter your nationalid")
            if user_nationalid.isdigit() == True:
                print("addRecord_nationalid worked")
                break
            else:
                print("enter a valid nationalid")
        while True:
            user_mail = input("pls enter your mail")
            if re.search("@" and ".com",user_mail):
                print ("addRecord_mail worked")
                break
            else:
                print ("enter a valid mail")

        File = open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt", "r+", encoding=("utf-8"))
        user_id = (len(File.readlines()) + 1)
        File.close()
        with open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt", "a+", encoding=("utf-8")) as File:
            File.write("{}-{}-{}-{}-{}-{} \n".format(user_id,user_name,user_surname,user_age,user_nationalid,user_mail))
        self.backToMenu()
    def removeRecord(self):
        userInputRemove = 0
        def removeLine(self,line_number):
            # asagida dosyayi acip, istedigin line i silip, yenideni duzenliyor. senin removeListten secilen item in
            #hangi line da oldugunu bulman lazim



            # Prompt the user for the file name and line number to remove
            file_name = open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt")
            # Open the file for reading and store its contents in a list
            with open(file_name, "r") as f:
                lines = f.readlines()

            # Remove the specified line from the list
            del lines[line_number - 1]

            # Prompt the user for the new content to replace the remaining lines
            new_content = []
            while True:
                line = input("Enter new line (or 'q' to quit): ")
                if line == 'q':
                    break
                new_content.append(line)

            # Open the file for writing and write the new content to it
            with open(file_name, "w") as f:
                for line in new_content:
                    f.write(line + "\n")



        while True:
            try:
                userInputRemove = int(input ("which information you want to search?\n1-Id\n2-name\n3-surname\n4-age\n5-mail"))
                if userInputRemove < 6 and userInputRemove > 0:
                    break
                else:
                    print("pls enter a valid number")
            except Exception as e :
                print("remove "+ e )
        #--------------------------------------------------
        # Open the file for reading
        with open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt", "r") as f:
            lines = f.readlines() # everyline is an item into this "lines"array
            split_lines = []
            removeList = []
            # Loop through each line and split it by the "-" character
            for line in lines:
                split_line = line.split("-")
                if len(split_line) < 5:
                    print(f"bad data format on line {split_line}")
                else:
                split_lines.append(split_line)

            if userInputRemove == 1:
                requestedId = input("which name you looking for?")
                for i in split_lines:
                    if requestedId in i[0]:
                        removeList.append(i)
                        print(i)
            if userInputRemove == 2:
                requestedName = input("which name you looking for?")
                for i in split_lines:
                    if requestedName in i[1]:
                        print(i)
            if userInputRemove == 3:
                requestedSurname = input("which surname you looking for?")
                for i in split_lines:
                    if requestedSurname in i[2]:
                        print(i)
            if userInputRemove == 4:
                requestedAge = input("which age you looking for?")
                for i in split_lines:
                    if requestedAge in i[3]:
                        print(i)
            if userInputRemove == 5:
                requestedMail = input("which mail you looking for?")
                for i in split_lines:
                    if requestedMail in i[4]:
                        print(i)

    def listRecord(self):
        File = open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt", "r+", encoding=("utf-8"))
        x = File.readlines()
        print(x)
        File.close()


    def backToMenu(self):
        while True:
            x = input("for menu `6` for exit `5`")
            if x == "6":
                print("backToMenu working")
                self.program()
                break
            elif x == "5":
                print("exitRecord working")
                self.exitRecord()
            else:
                print("see u ")



    def exitRecord(self):
        pass

System = Record("fethullah")
System.program()

