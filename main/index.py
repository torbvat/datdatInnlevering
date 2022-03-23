import sqlite3 as sql
from sqlite3 import Error
import hashlib 
import cleanCommands as command
import login as l
import brukerhistorier as b

class User:
    def __init__(self,full_name, password, mail):
        self.full_name = full_name
        self.password = password
        self.mail = mail
    

#=======================================================================
# user interface


session = False
while True:
    print("ny bruker? Y/N")
    userInput = input()
    if (userInput == "Y" or userInput == "y"):
        l.newUser()
        continue
    elif (userInput == "N" or userInput == "n"):
        data = l.logIn()
        if data != None:
            session = True
            user = User(data[0][2], data[0][1], data[0][0])

    
    while True:
        if session == False:
            break
        print("Velg hva du vil gjøre:")
        print("(skriv tallet til alternativet du velger)")
        print("1: vurder en kaffe")
        print("2: sett inn informasjon i en tabell")
        print("3: test en brukerhistorie")
        print("4: logg ut")

        userInput = input()

        if userInput == "1":
            command.newKaffeSmaking(user.mail)
            continue

        if userInput == "2":
            while True:
                print("velg tabell")
                print("(skriv tallet til alternativet du velger)")
                print("1: Foredlingsmetode")
                print("2: Regioner")
                print("3: Kaffegaard")
                print("4: KaffeParti")
                print("5: FerdigbrentKaffe")
                print("6: KaffeBonne")
                print("7: BestaarAv")
                print("8: DyrketAv")
                print("9: gå tilbake")
            
                tableInput = input()
                if tableInput == "1": table = "Foredlingsmetode"
                elif tableInput == "2": table = "Regioner"
                elif tableInput == "3": table = "Kaffegaard"
                elif tableInput == "4": table = "KaffeParti"
                elif tableInput == "5": table = "FerdigbrentKaffe"
                elif tableInput == "6": table = "KaffeBonne"
                elif tableInput == "7": table = "BestaarAv"
                elif tableInput == "8": table = "DyrketAv"
                elif tableInput == "9": break
                else: 
                    print("noe gikk galt, prøv igjen") 
                    continue
                command.insert(table)
                break
        
        elif userInput == "3":
            print("velg brukerhistorie")
            print("1")
            print("2")
            print("3")
            print("4")
            print("5")

            bInput = input()

            if bInput == "1":
                b.Brukerhistorie_1(user.mail)
            elif bInput == "2":
                b.Brukerhistorie_2()
            elif bInput == "3":
                b.Brukerhistorie_3()
            elif bInput == "4":
                b.Brukerhistorie_4()
            elif bInput == "5":
                b.Brukerhistorie_5()

            continue

        elif userInput == "4":
            session = False
            continue

        else:
            print("something went wrong")
            continue

        





