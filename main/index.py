import sqlite3 as sql
from sqlite3 import Error
import hashlib 

class User:
    def __init__(self,full_name, password, mail):
        self.full_name = full_name
        self.password = password
        self.mail = mail
        


session = False

db_file = "C:\\Users\\torbj\\OneDrive\\Documentos\\Studie\\VAR-SEMESTER-2022\\Database\\Prosjekt\\datdatInnlevering\\main\\databaser\\database.db"


def db_file():
    return str("C:\\Users\\torbj\\OneDrive\\Documentos\\Studie\\VAR-SEMESTER-2022\\Database\\Prosjekt\\datdatInnlevering\\main\\databaser\\database.db")


def hash(string):
    return str(hashlib.sha9(string.encode()))

    

def login():
    try:
        connection = sql.connect(db_file())
        cursor = connection.cursor()
        mail = input("Skriv din e-postadresse:")
        password = input("Skriv ditt passord: ")
        cursor.execute("SELECT email, passord, navn FROM Bruker WHERE email = ?", (mail,))
        data=cursor.fetchall()
        if len(data)!=0:
            print(data)
            if(data[0][0]==mail and data[0][1]==password):
                print("Velkommen " + data[0][2] + "!")
                return data
            else:
                print("feil passord")
                return None
        else:
            print("Ikke gyldig innlogging")
            return None

    except Error as e:
        print(e)




# bruker1=Bruker("torbjørn vatne","passord123","torb@gmail.com")
# bruker1.login()


def exists(table, element, condition, cursor):
    try:
        sql = "SELECT * FROM "
        sql += str(table)
        sql += " WHERE "
        sql += str(element)
        sql += " = "
        sql += condition
        cursor.execute(sql)
        data=cursor.fetchall()
        if len(data)==0:
            return False
        else:
            return True
    except Error as e:
        print(e)
        return False


def newUser():
    print("epost:")
    email = input()
    print("fullt navn:")
    name = input()
    print("passord:")
    password = input()
    connection = None
    try:

        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()

        cursor.execute("SELECT email FROM Bruker WHERE email = ?", (email,))
        data=cursor.fetchall()
        # if exists('Bruker', 'email', email, cursor) == False:
        if len(data)==0:
            cursor.execute("""INSERT INTO Bruker (email, navn, passord) VALUES (?,?,?);
            """, (email, name, password))
        
            connection.commit()
        else:
            print("Brukeren finnes alt")
            
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


# print("ny bruker? Y/N")
# userInput = input()
# if userInput == "Y":
#     newUser()
# elif userInput == "N":
#     data = login()
#     if data != None:
#         session = True
#         user = User(data[0][2], data[0][1], data[0][0])

# if session:
#     pass

#Brukerhistorie 2:
# def smakt_flest_unike_kaffer(): #Sjekk om dette funker etter at vi har lagt inn data i tabellene
#     connection = sql.connect(db_file())
#     print(sql.version)
#     cursor = connection.cursor()
#     cursor.execute("""
#      SELECT COUNT(DISTINCT kaffeNavn) as antall, navn FROM Bruker 
#      INNER JOIN KaffeSmaking ON (Bruker.email = KaffeSmaking.email)
#      GROUP BY navn 
#      ORDER BY antall DESC
#     """)
#     data = cursor.fetchall()
#     return data

#Brukerhistorie 3:
def mest_for_pengene():
    connection = sql.connect(db_file())
    print(sql.version)
    cursor = connection.cursor()
    cursor.execute("""
     SELECT 
        FerdigbrentKaffe.kaffeNavn AS Kaffenavn, 
        AVG(SELECT Score From KaffeSmaking 
            INNER JOIN FerdigbrentKaffe ON (KaffeSmaking.kaffeNavn=FerdigbrentKaffe.kaffeNavn)) AS Gjennomsnittsscore, 
        AVG(Gjennomsnittsscore)/FerdigbrentKaffe.kilopris AS 'Score/pris'
     FROM KaffeSmaking
     INNER JOIN FerdigbrentKaffe ON (KaffeSmaking.kaffeNavn=FerdigbrentKaffe.kaffeNavn)  
     ORDER BY 'Score/pris' DESC
    """)
    data = cursor.fetchall()
    print(data)
    return data

# Brukerhistorie 4: (funker) - kaffen MÅ finnes i både KaffeSmaking OG FerdigbrentKaffe (gir forsåvidt mening)
# def floral_kaffe():
#     connection = sql.connect(db_file())
#     print(sql.version)
#     cursor = connection.cursor()
    
#     cursor.execute("""
#         SELECT 
#         FerdigbrentKaffe.kaffeNavn,
#         FerdigbrentKaffe.brenneri
#         FROM FerdigbrentKaffe
#         INNER JOIN KaffeSmaking ON (KaffeSmaking.kaffeNavn=FerdigbrentKaffe.kaffeNavn)  
#         WHERE lower(KaffeSmaking.kommentar) LIKE '%floral%' 
#         OR lower(FerdigbrentKaffe.beskrivelse) LIKE '%floral%'
#     """)
#     data = cursor.fetchall()
#     print(data)
#     return data

#Brukerhistorie 5:
# def ikke_vaskede_fra_Rwanda_eller_Colombia():
#     connection = sql.connect(db_file())
#     print(sql.version)  
#     cursor = connection.cursor()
#     cursor.execute("""
#         SELECT 
#         FerdigbrentKaffe.kaffeNavn,
#         FerdigbrentKaffe.brenneri
#         FROM FerdigbrentKaffe
#             INNER JOIN KaffeParti ON (FerdigbrentKaffe.partiID = KaffeParti.partiID)
#                 INNER JOIN Foredlingsmetode ON (Foredlingsmetode.foredlingsnavn = KaffeParti.foredlingsnavn)
#                     INNER JOIN KaffeGaard ON (Kaffeparti.gaardID = KaffeGaard.gaardID)
#                         INNER JOIN Regioner ON (KaffeGaard.region = Regioner.regionID)
#         WHERE lower(Foredlingsmetode.beskrivelse) NOT LIKE '% vasket %' 
#         AND (
#         Regioner.land LIKE 'Rwanda'
#         OR Regioner.land LIKE 'Colombia'
#         )
#     """)
#     data = cursor.fetchall()
#     print(data)
#     return data

# ikke_vaskede_fra_Rwanda_eller_Colombia() #skal få [kaffenavn3,brennerinavn3]    

mest_for_pengene()