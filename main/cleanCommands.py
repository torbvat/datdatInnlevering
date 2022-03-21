
import sqlite3 as sql
from sqlite3 import Error

def db_file():
    return str("C:\\Users\\torbj\\OneDrive\\Documentos\\Studie\\VAR-SEMESTER-2022\\Database\\Prosjekt\\datdatInnlevering\\main\\databaser\\database.db")

def newForedlingsmetode():
    print("foredlingsnavn:")
    v1 = input()
    print("beskrivelse:")
    v2 = input()
    # litt usikker om det er nødvendig å sjekke om den allerede finnes.
    string = ("""INSERT INTO Foredlingsmetode (foredlingsnavn, beskrivelse) VALUES (?,?);""", (v1, v2))
    return string

def newRegioner():
    print("navn:")
    v1 = input()
    print("land:")
    v2 = input()

    string = ("""INSERT INTO Regioner (navn, land) VALUES (?,?);""", (v1, v2))
    return string
        

def newKaffegaard():
    print("navn:")
    v1 = input()
    print("moh:")
    v2 = input()
    print("regionId:")
    v3 = int(input())

    string = ("""INSERT INTO Kaffegaard (moh, navn, region) VALUES (?,?,?);""", (v2, v1,v3))
    return string


def newKaffeParti():
    print("foreldringsnavn(nb navnet må finnes i foredlingstabellen):")
    v1 = input()
    print("kilopris:")
    v2 = float(input())
    print("gaardID:")
    v3 = int(input())
    print("innhøstelsesår:")
    v4 = int(input())

    string = ("""INSERT INTO Kaffegaard (foreldringsnavn, kilopris, gaardID,innhøstelsesår) VALUES (?,?,?,?);""", (v1, v2,v3,v4))
    return string

def newFerdigbrentKaffe():
    print("kaffeNavn:")
    v1 = input()
    print("partiID:")
    v2 = int(input())
    print("dato YYYY-MM-DD:")
    v3 = (input())
    print("brennerinavn:")
    v4 = (input())
    print("brenningsgrad:")
    v5 = (input())
    print("beskrivelse:")
    v6 = (input())
    print("kilopris:")
    v7 = float(input())

    string = ("""INSERT INTO FerdigbrentKaffe (kaffeNavn, partiID, dato, brenneri, brenningsgrad, beskrivelse, kilopris ) VALUES (?,?,?,?,?,?,?);""", (v1, v2,v3,v4,v5,v6,v7))
    return string
      

def SortSqlString(table):
    # if table == "Bruker":
    #     return newBruker()
    if table == "Foredlingsmetode":
        return newForedlingsmetode()
    if table == "Regioner":
        return newRegioner()
    if table == "Kaffegaard":
        return newKaffegaard()
    if table == "KaffeParti":
        return newKaffeParti()
    if table == "FerdigbrentKaffe":
        return newFerdigbrentKaffe()
    # if table == "KaffeSmaking":
    #     return newKaffeSmaking()
    if table == "KaffeBonne":
        return newKaffeBonne()
    if table == "BestaarAv":
        return newBestaarAv()
    if table == "DyrketAv":
        return newDyrketAv()

    
        
        


def insert(table):
    connection = None
    sqlString = newFerdigbrentKaffe()

    try:
        connection = sql.connect(db_file())
        cursor = connection.cursor()
        cursor.execute(sqlString)
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def newKaffeSmaking(email):
    print("kaffeNavn:")
    v1 = input()
    print("brennerinavn:")
    v2 = (input())
    print("din vurdering, 0-10")
    v3 = int(input())
    print("kommentar:")

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO FerdigbrentKaffe (email, kaffeNavn, brenneri, tidspunkt, score, kommentar ) VALUES (?,?,?,?,?,?);
        """, (email,v1, v2, None, v3, v4, v5, v6, v7))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

newKaffeSmaking("test@ntnu.no")