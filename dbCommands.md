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
        cursor.execute("""INSERT INTO Kaffegaard (moh, navn, regionID) VALUES (?,?,?);
        """, (v2, v1,v3))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def newKaffeParti():
print("foredlingsnavn(nb navnet må finnes i foredlingstabellen):")
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
        cursor.execute("""INSERT INTO KaffeParti (foredlingsnavn, kilopris, gaardID,innhoestelsesaar) VALUES (?,?,?,?);
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
        cursor.execute("""INSERT INTO BestaarAv (partiID, navn) VALUES (?,?);
        """, (v1, v2))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def newDyrketAv():
print("navn på kaffebønne:")
v1 = (input())
print("gård id:")
v2 = (input())

    connection = None

    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO DyrketAv (navn, gaardID) VALUES (?,?);
        """, (v1, v2))
        connection.commit()

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

newRegioner()
