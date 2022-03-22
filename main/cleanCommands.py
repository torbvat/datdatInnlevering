
import sqlite3 as sql
from sqlite3 import Error

def db_file():
    return str("C:\\Users\\torbj\\OneDrive\\Documentos\\Studie\\VAR-SEMESTER-2022\\Database\\Prosjekt\\datdatInnlevering\\main\\databaser\\database.db")


def cleanInput(dataType):
    print("input her")
    userinput = str(input())
    
    if dataType == int:
        if not type(eval(userinput)) == dataType:
                print("du må skrive et heltall, prøv igjen")
                cleanInput(dataType)
    elif dataType == float:
        if not (type(eval(userinput)) == int or type(eval(userinput)) == float):
                print("du må skrive et heltall eller desimaltall, prøv igjen")
                cleanInput(dataType)
    else:
        userinput = str(userinput)
    
    special_characters = """!#$%^&*()-+?_=,<>/'";"""
    if any(letter in special_characters for letter in userinput):
        print("du kan ikke bruke spesialtegn, prøv igjen")
        cleanInput(dataType)
    else:
        return userinput




def newForedlingsmetode():
    print("foredlingsnavn:")
    v1 = cleanInput()
    print("beskrivelse:")
    v2 = cleanInput()
    # litt usikker om det er nødvendig å sjekke om den allerede finnes.
    string = """INSERT INTO Foredlingsmetode (foredlingsnavn, beskrivelse) VALUES (?,?);"""
    args = (v1, v2)
    return string, args

def newRegioner():
    print("navn:")
    v1 = cleanInput()
    print("land:")
    v2 = cleanInput()

    string = """INSERT INTO Regioner (navn, land) VALUES (?,?);"""
    args = (v1, v2)
    return string,args
        

def newKaffegaard():
    print("navn:")
    v1 = input()
    print("moh:")
    v2 = input()
    print("regionId:")
    v3 = int(input())

    string = """INSERT INTO Kaffegaard (moh, navn, region) VALUES (?,?,?);"""
    args = (v2, v1,v3)
    return string, args


def newKaffeParti():
    print("foreldringsnavn(nb navnet må finnes i foredlingstabellen):")
    v1 = input()
    print("kilopris:")
    v2 = float(input())
    print("gaardID:")
    v3 = int(input())
    print("innhøstelsesår:")
    v4 = int(input())

    string = """INSERT INTO Kaffegaard (foreldringsnavn, kilopris, gaardID,innhøstelsesår) VALUES (?,?,?,?);"""
    args = (v1, v2,v3,v4)
    return string, args

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

    string = """INSERT INTO FerdigbrentKaffe (kaffeNavn, partiID, dato, brenneri, brenningsgrad, beskrivelse, kilopris ) VALUES (?,?,?,?,?,?,?);"""
    args = (v1, v2,v3,v4,v5,v6,v7)
    return string, args


def newKaffeBonne():
    print("navn:")
    v1 = input()
    print("art:")
    v2 = (input())

    string = """INSERT INTO KaffeBonne (navn, art) VALUES (?,?);"""
    args = (v1, v2)
    return string, args
      

def sortSqlString(table):
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
    sqlString, args = sortSqlString(table)

    try:
        connection = sql.connect(db_file())
        cursor = connection.cursor()
        cursor.execute(sqlString,args)
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()



newKaffeSmaking("test@ntnu.no")