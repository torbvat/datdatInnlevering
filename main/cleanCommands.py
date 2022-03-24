
import sqlite3 as sql
from sqlite3 import Error
from datetime import datetime as d


def db_file():
    return str("datdatInnlevering\\main\\databaser\\database.db")


def cleanInput(dataType):
    # print("input her")
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
    
    special_characters = """#$%^*()+_=<>/'";"""
    if any(letter in special_characters for letter in userinput):
        print("du kan ikke bruke spesialtegn, prøv igjen")
        cleanInput(dataType)
    else:
        return userinput




def newForedlingsmetode():
    print("foredlingsnavn:")
    v1 = cleanInput(str)
    print("beskrivelse:")
    v2 = cleanInput(str)
    string = """INSERT INTO Foredlingsmetode (foredlingsnavn, beskrivelse) VALUES (?,?);"""
    args = (v1, v2)
    return string, args

def newRegioner():
    print("navn:")
    v1 = cleanInput(str)
    print("land:")
    v2 = cleanInput(str)

    string = """INSERT INTO Regioner (navn, land) VALUES (?,?);"""
    args = (v1, v2)
    return string,args
        

def newKaffegaard():
    print("navn:")
    v1 = cleanInput(str)
    print("moh:")
    v2 = cleanInput(str)
    print("regionId:")
    v3 = cleanInput(int)

    string = """INSERT INTO Kaffegaard (moh, navn, regionID) VALUES (?,?,?);"""
    args = (v2, v1,v3)
    return string, args


def newKaffeParti():
    print("foreldringsnavn(nb navnet må finnes i foredlingstabellen):")
    v1 = cleanInput(str)
    print("kilopris:")
    v2 = cleanInput(float)
    print("gaardID:")
    v3 = cleanInput(int)
    print("innhøstelsesår:")
    v4 = cleanInput(int)

    string = """INSERT INTO KaffeParti (foredlingsnavn, kilopris, gaardID,innhoestelsesaar) VALUES (?,?,?,?);"""
    args = (v1, v2,v3,v4)
    return string, args

def newFerdigbrentKaffe():
    print("kaffeNavn:")
    v1 = cleanInput(str)
    print("partiID:")
    v2 = cleanInput(int)
    print("dato YYYY-MM-DD:")
    v3 = cleanInput(str)
    print("brennerinavn:")
    v4 = cleanInput(str)
    print("brenningsgrad:")
    v5 = cleanInput(str)
    print("beskrivelse:")
    v6 = cleanInput(str)
    print("kilopris:")
    v7 = cleanInput(float)

    string = """INSERT INTO FerdigbrentKaffe (kaffeNavn, partiID, dato, brenneri, brenningsgrad, beskrivelse, kilopris ) VALUES (?,?,?,?,?,?,?);"""
    args = (v1, v2,v3,v4,v5,v6,v7)
    return string, args


def newKaffeBonne():
    print("navn:")
    v1 = cleanInput(str)
    print("art:")
    v2 = cleanInput(str)

    string = """INSERT INTO KaffeBonne (navn, art) VALUES (?,?);"""
    args = (v1, v2)
    return string, args

def newBestaarAv():
    print("partiID:")
    v1 = cleanInput(int)
    print("navn på kaffebonne:")
    v2 = cleanInput(str)
        
    string = """INSERT INTO BestaarAv (partiID, navn) VALUES (?,?);"""
    args = (v1, v2)
    return string, args

def newDyrketAv():
    print("navn på kaffebønne:")
    v1 = cleanInput(str)
    print("gård id:")
    v2 = cleanInput(int)

    string = """INSERT INTO BestaarAv (navn, gaardID) VALUES (?,?);""" 
    args = (v1, v2)
    return string, args

      

def sortSqlString(table):
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
        print("Informasjonen er lagt inn i tabellen!")

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def newKaffeSmaking(email):
    print("kaffeNavn:")
    v1 = cleanInput(str)
    print("brennerinavn:")
    v2 = cleanInput(str)
    print("din vurdering, 0-10")
    v3 = cleanInput(float)
    print("smaksnotat:")
    v4 = cleanInput(str)

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        tidspunkt = d.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO KaffeSmaking (email, kaffeNavn, brenneri, tidspunkt, score, kommentar ) VALUES (?,?,?,?,?,?);
        """, (email,v1, v2, tidspunkt, v3, v4))
        connection.commit()

        cursor.execute("SELECT * FROM KaffeSmaking WHERE (email = ? AND kaffeNavn= ? AND brenneri = ? AND tidspunkt=? )", (email,v1, v2, tidspunkt,))
        newData=cursor.fetchall()
        if len(newData) != 0:
            print("takk for vurdering!")
            print("Din vurdering:")
            for element in newData[0]:
                print(element)
<<<<<<< HEAD
            print("")   
=======
            print("") # bare for å få litt avstand fra det som kommer under


        # cursor.execute("SELECT * FROM KaffeSmaking WHERE email = ?", (mail,))
        # data=cursor.fetchall()
>>>>>>> 016e269bd35e5c3e16a7a7927b05c11b67a2cc65

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

insert("Regioner")
