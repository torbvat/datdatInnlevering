
import cleanCommands as command
import login as l
import brukerhistorier as b

class User:
    def __init__(self,full_name, password, mail):
        self.full_name = full_name
        self.password = password
        self.mail = mail

def printTable(table, tablenames):
    if len(table) == 0: 
        print("noe har gått galt")
        return
    print(tablenames)
    print("---------------------------------")
    i = 0
    for row in table:
        i += 1
<<<<<<< HEAD
=======
        #print(*row)
>>>>>>> 016e269bd35e5c3e16a7a7927b05c11b67a2cc65
        string = str(i)
        for element in row:
            if string == str(i):
                string += "   "
            else: 
                string += ",   "
            string += str(element)
        print(string)
    print("---------------------------------")
     
    

#=======================================================================
# user interface


session = False
while True:
    print("ny bruker? Y/N")
    userInput = input().upper()
    if (userInput == "Y"):
        l.newUser()
        continue
    elif (userInput == "N"):
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
                printTable(b.Brukerhistorie_2(), "   navn og antall smakte kaffer:")
            elif bInput == "3":
                printTable(b.Brukerhistorie_3(), "   Brenneri, kaffe, kilopris og gjennomsnittvurdering:")
            elif bInput == "4":
                printTable(b.Brukerhistorie_4(), "    Brenneri og kaffenavn:")
            elif bInput == "5":
                printTable(b.Brukerhistorie_5(), "   Brenneri og kaffe fra Rwada eller Colombia, som ikke er vasket:")

            continue

        elif userInput == "4":
            print("Du er nå logget ut. Ha en fin dag")
            session = False
            continue

        else:
            print("something went wrong")
            continue

        





