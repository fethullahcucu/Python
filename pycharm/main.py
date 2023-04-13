import re



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
                print(e)


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
        while True:
            try:
                userInputRemove = int(input ("which information you want to search?\n1-Id\n2-name\n3-surname\n5-age\n6-mail"))
                if userInputRemove < 5 and userInputRemove > 0:
                    break
                else:
                    print("pls enter a valid number")
            except Exception as e :
                print("remove e "+ e )

        if userInputRemove == 1:
            userInput1 = input("what is the number of user?")
            with open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt", "a+", encoding=("utf-8")) as File:
                for line in File:
                    line = line.strip()
                    line = line.split("-")
                    print("line worked")
                    if line[0] == userInput1:
                        lines = File.readlines()
                        del lines[userInput1+1]
                        print("line0 worked")
                        with open("C:/Python/Fundemantel/Fethullah_Cucu_Demo.txt", "a+", encoding=("utf-8")) as File1:
                            File1.writelines(lines)
                            print("second with worked")







                File.close()
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

