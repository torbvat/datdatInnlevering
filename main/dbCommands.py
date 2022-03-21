from hashlib import new
import sqlite3 as sql
from sqlite3 import Error
from datetime import datetime as d

db_file = "C:\\Users\\torbj\\OneDrive\\Documentos\\Studie\\VAR-SEMESTER-2022\\Database\\Prosjekt\\datdatInnlevering\\main\\databaser\\database.db"
def db_file():
    return str("C:\\Users\\torbj\\OneDrive\\Documentos\\Studie\\VAR-SEMESTER-2022\\Database\\Prosjekt\\datdatInnlevering\\main\\databaser\\database.db")


connection = None
try:
    connection = sql.connect(db_file())
    print(sql.version)
    cursor = connection.cursor()
    # cursor.execute(
        # """CREATE TABLE Bruker (
        #     email varchar(30) NOT NULL,
        #     navn varchar(50),
        #     passord varchar(20) NOT NULL,
        #     CONSTRAINT Bruker_PK PRIMARY KEY (email)
        # );""")
    # cursor.execute("""
    #     CREATE TABLE Foredlingsmetode(
    #     foredlingsnavn varchar(30),
    #     beskrivelse varchar(140),
    #     CONSTRAINT Foredlingsmetode_PK PRIMARY KEY (foredlingsnavn)
    #     );
    # """)
    # cursor.execute("""
    #     CREATE TABLE Regioner(
    #     regionID integer NOT NULL,
    #     navn varchar(30),
    #     land varchar(30),
    #     CONSTRAINT Regioner_PK PRIMARY KEY (regionID)
    #     );
    # """)
    # cursor.execute("""
    #     CREATE TABLE Kaffegaard(
    #     gaardID integer NOT NULL,
    #     moh integer,
    #     navn varchar(30),
    #     region integer,
    #     CONSTRAINT Kaffegaard_PK PRIMARY KEY (gaardID),
    #     CONSTRAINT Kaffegaard_FK1 FOREIGN KEY (region) REFERENCES Regioner(regionID)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION
    #     );
    # """)
    # cursor.execute("""
    #     CREATE TABLE KaffeParti (
    #     partiID integer NOT NULL,
    #     foreldringsnavn varchar(30) NOT NULL,
    #     kilopris real,
    #     gaardID integer NOT NULL,
    #     innhoestelsesaar integer(4),
    #     CONSTRAINT kaffeParti_PK PRIMARY KEY (partiID),
    #     CONSTRAINT kaffeParti_FK1 FOREIGN KEY (foreldringsnavn) REFERENCES Foredlingsmetode(foredlingsnavn)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION,
    #     CONSTRAINT kaffeParti_FK2 FOREIGN KEY (gaardID) REFERENCES Kaffegaard(gaardID)
    #         ON UPDATE CASCADE
    #         ON DELETE CASCADE
    #     );
    # """)
    # cursor.execute("""DROP TABLE FerdigbrentKaffe""")

    # cursor.execute("""
    #     CREATE TABLE FerdigbrentKaffe(
    #     kaffeNavn varchar(30) NOT NULL,
    #     partiID integer NOT NULL,
    #     dato date NOT NULL,
    #     brenneri varchar(30) NOT NULL,
    #     brenningsgrad varchar(30),
    #     beskrivelse varchar(140),
    #     kilopris real,
    #     CONSTRAINT FerdigbrentKaffe_PK PRIMARY KEY (kaffeNavn, brenneri),
    #     CONSTRAINT FerdigbrentKaffe_FK1 FOREIGN KEY (partiID) REFERENCES KaffeParti(partiID)
    #         ON UPDATE CASCADE
    #         ON DELETE CASCADE
    #     );
    # """)
    

    # cursor.execute("""
    #     CREATE TABLE KaffeSmaking (
    #     email varchar(30) NOT NULL,
    #     kaffeNavn varchar(30) NOT NULL,
    #     brenneri varchar(30) NOT NULL,
    #     tidspunkt datetime NOT NULL,
    #     score integer,
    #     kommentar varchar(140),
    #     CONSTRAINT KaffeSmaking_PK PRIMARY KEY (email, kaffeNavn, brenneri, tidspunkt ),
    #     CONSTRAINT KaffeSmaking_FK1 FOREIGN KEY (email) REFERENCES Bruker(email)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION,
    #     CONSTRAINT KaffeSmaking_FK2 FOREIGN KEY (kaffeNavn) REFERENCES FerdigBrentKaffe(kaffeNavn)
    #         ON UPDATE CASCADE
    #         ON DELETE CASCADE
    #     );""")

    # cursor.execute("""
    #     CREATE TABLE KaffeBonne(
    #     navn varchar(30) NOT NULL,
    #     art varchar(30),
    #     CONSTRAINT KaffeBonne_PK PRIMARY KEY (navn)
    #     );
    # """)

    # cursor.execute("""
    #     CREATE TABLE BestaarAv(
    #     partiID integer NOT NULL,
    #     navn varchar(30) NOT NULL,
    #     CONSTRAINT BestaarAv_PK PRIMARY KEY (partiID, navn),
    #     CONSTRAINT BestaarAv_FK1 FOREIGN KEY (partiID) REFERENCES KaffeParti(partiID)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION,
    #     CONSTRAINT BestaarAv_FK2 FOREIGN KEY (navn) REFERENCES KaffeBonne(Navn)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION
    #     );
    # """)

    # cursor.execute("""
    #     CREATE TABLE DyrketAv(
    #     navn varchar(30) NOT NULL,
    #     gaardID integer NOT NULL,
    #     CONSTRAINT DyrketAv_PK PRIMARY KEY (navn, gaardID),
    #     CONSTRAINT DyrketAv_FK1 FOREIGN KEY (navn) REFERENCES Kaffebonne(navn)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION,
    #     CONSTRAINT DyrketAv_FK2 FOREIGN KEY (gaardID) REFERENCES KaffeGaard(gaardID)
    #         ON UPDATE CASCADE
    #         ON DELETE NO ACTION
    #     );
    # """)

    # cursor.execute("""INSERT INTO Bruker (email, navn, passord) VALUES (
    #     'bruker@gmail.com',
    #     'bruker brukersen',
    #     'hei');
    # """)

    connection.commit()
except Error as e:
    print(e)
finally:
    if connection:
        connection.close()
        

def newForedlingsmetode():
    print("foredlingsnavn:")
    v1 = input()
    print("beskrivelse:")
    v2 = input()
    
    connection = None
    try:

        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()

        cursor.execute("SELECT foredlingsnavn FROM Foredlingsmetode WHERE foredlingsnavn = ?", (v1,))
        data=cursor.fetchall()
        if len(data)==0:
            cursor.execute("""INSERT INTO Foredlingsmetode (foredlingsnavn, beskrivelse) VALUES (?,?);
            """, (v1, v2))
        
            connection.commit()
        else:
            print("Noe gikk galt")
            
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def newRegioner():
    print("navn:")
    v1 = input()
    print("land:")
    v2 = input()
    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Regioner (navn, land) VALUES (?,?);
        """, (v1, v2))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def newKaffegaard():
    print("navn:")
    v1 = input()
    print("moh:")
    v2 = input()
    print("regionId:")
    v3 = int(input())
    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Kaffegaard (moh, navn, region) VALUES (?,?,?);
        """, (v2, v1,v3))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def newKaffeParti():
    print("foreldringsnavn(nb navnet må finnes i foredlingstabellen):")
    v1 = input()
    print("kilopris:")
    v2 = float(input())
    print("gaardID:")
    v3 = int(input())
    print("innhøstelsesår:")
    v4 = int(input())
    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO Kaffegaard (foreldringsnavn, kilopris, gaardID,innhøstelsesår) VALUES (?,?,?,?);
        """, (v1, v2,v3,v4))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


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

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO FerdigbrentKaffe (kaffeNavn, partiID, dato, brenneri, brenningsgrad, beskrivelse, kilopris ) VALUES (?,?,?,?,?,?,?);
        """, (v1, v2,v3,v4,v5,v6,v7))
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
    print("smaksnotat:")
    v4 = (input())
    # print("når ble kaffen brent:")
    # v5 = (input())

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO KaffeSmaking (email, kaffeNavn, brenneri, tidspunkt, score, kommentar ) VALUES (?,?,?,?,?,?);
        """, (email,v1, v2, d.now().strftime("%Y-%m-%d %H:%M:%S"), v3, v4))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def newKaffeBonne():
    print("navn:")
    v1 = input()
    print("art:")
    v2 = (input())

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO KaffeBonne (navn, art) VALUES (?,?);
        """, (v1, v2))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def newBestaarAv():
    print("partiID:")
    v1 = int(input())
    print("navn på kaffebonne:")
    v2 = (input())

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO BestaarAv (navn, art) VALUES (?,?);
        """, (v1, v2))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def newDyrketAv():
    print("navn på kaffebønne:")
    v1 = int(input())
    print("gård id:")
    v2 = (input())

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO BestaarAv (navn, art) VALUES (?,?);
        """, (v1, v2))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()
newFerdigbrentKaffe()