import sqlite3 as sql
from sqlite3 import Error
from datetime import datetime as d

def printTable(table, tablenames):
    print(tablenames)
    print("---------------------------------")
    i = 0
    for row in table:
        i += 1
        #print(*row)
        string = str(i)
        for element in row:
            if string == str(i):
                string += "   "
            else: 
                string += ",   "
            string += str(element)
        print(string)
    print("---------------------------------")
     

def db_file():
    return str("datdatInnlevering\\main\\databaser\\database.db")


#Brukerhistorie 1:
def Brukerhistorie_1(email):
    v1 = "Vinterkaffe 2022"
    v2 = "Trondheims-brenneriet Jacobsen & Svart"
    v3 = 10
    v4 = "Wow - en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!"
    
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
            print("") # bare for å få litt avstand fra det som kommer under

    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()



def Brukerhistorie_2(): #Funker
    connection = None
    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT navn, COUNT(DISTINCT kaffeNavn) as antall FROM Bruker 
        INNER JOIN KaffeSmaking ON (Bruker.email = KaffeSmaking.email)
        GROUP BY navn 
        ORDER BY antall DESC
        """)
        data = cursor.fetchall()
        printTable(data, "   navn og antall smakte kaffer:")
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()


def Brukerhistorie_3():
    connection = None
    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT FerdigbrentKaffe.brenneri, FerdigbrentKaffe.kaffeNavn, 
            FerdigbrentKaffe.kilopris,
            AVG(KaffeSmaking.score) AS Gjennomsnittsscore
                FROM KaffeSmaking
                    INNER JOIN FerdigbrentKaffe ON (KaffeSmaking.kaffeNavn=FerdigbrentKaffe.kaffeNavn)  
            GROUP BY FerdigbrentKaffe.kaffeNavn
            ORDER BY Gjennomsnittsscore/FerdigbrentKaffe.kilopris DESC;
        """)
        #denne var i select, og det skal den ikkke være
        #AVG(Kaffesmaking.score)/FerdigbrentKaffe.kilopris AS 'Gjennomsnittsscore/kilopris'
        data = cursor.fetchall()
        printTable(data, "   Brenneri, kaffe, kilopris og gjennomsnittvurdering:")
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def Brukerhistorie_4():
    connection = None
    try:
        connection = sql.connect(db_file())
        print(sql.version)
        cursor = connection.cursor()
        
        # torbjørn sin kode, fant en feil, lar bli foreløpig hvis torbjørn har innvendinger. 
        # cursor.execute("""
        #     SELECT 
        #     DISTINCT FerdigbrentKaffe.brenneri, FerdigbrentKaffe.kaffeNavn
        #     FROM FerdigbrentKaffe
        #     INNER JOIN KaffeSmaking ON (KaffeSmaking.kaffeNavn=FerdigbrentKaffe.kaffeNavn)  
        #     WHERE lower(KaffeSmaking.kommentar) LIKE '%floral%' 
        #     OR lower(FerdigbrentKaffe.beskrivelse) LIKE '%floral%'
        # """)

        
        cursor.execute("""
            SELECT 
            DISTINCT FerdigbrentKaffe.brenneri, FerdigbrentKaffe.kaffeNavn
            FROM FerdigbrentKaffe
                LEFT JOIN KaffeSmaking
                    ON FerdigbrentKaffe.kaffeNavn = KaffeSmaking.kaffeNavn
            WHERE lower(KaffeSmaking.kommentar) LIKE '%floral%' 
            OR lower(FerdigbrentKaffe.beskrivelse) LIKE '%floral%'
            UNION 
            SELECT DISTINCT KaffeSmaking.brenneri, KaffeSmaking.kaffeNavn
            FROM KaffeSmaking
                LEFT JOIN FerdigbrentKaffe
                    ON FerdigbrentKaffe.kaffeNavn = KaffeSmaking.kaffeNavn
            WHERE lower(KaffeSmaking.kommentar) LIKE '%floral%' 
            OR lower(FerdigbrentKaffe.beskrivelse) LIKE '%floral%'
            
        """)
        data = cursor.fetchall()
        printTable(data, "    Brenneri og kaffenavn:")
        
        #Det over er oversatt fra disse spørringene. Lar de bli foreløpig 
        # cursor.execute("""
        #     SELECT 
        #     DISTINCT FerdigbrentKaffe.brenneri, FerdigbrentKaffe.kaffeNavn
        #     FROM FerdigbrentKaffe
    
        #     WHERE lower(FerdigbrentKaffe.beskrivelse) LIKE '%floral%'
        # """)
        # data = cursor.fetchall()
        # print(data)
        # cursor.execute("""
        #     SELECT 
        #     DISTINCT KaffeSmaking.brenneri, KaffeSmaking.kaffeNavn
        #     FROM KaffeSmaking
    
        #     WHERE lower(KaffeSmaking.kommentar) LIKE '%floral%'
        # """)
        # data = cursor.fetchall()
        # print(data)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()

def Brukerhistorie_5():
    connection = None
    try:
        connection = sql.connect(db_file())
        print(sql.version)  
        cursor = connection.cursor()
        cursor.execute("""
            SELECT FerdigbrentKaffe.brenneri, FerdigbrentKaffe.kaffeNavn
                FROM FerdigbrentKaffe
                    INNER JOIN KaffeParti ON (FerdigbrentKaffe.partiID = KaffeParti.partiID)
                        INNER JOIN Foredlingsmetode ON (Foredlingsmetode.foredlingsnavn = KaffeParti.foredlingsnavn)
                            INNER JOIN Kaffegaard ON (Kaffeparti.gaardID = Kaffegaard.gaardID)
                                INNER JOIN Regioner ON (KaffeGaard.regionID = Regioner.regionID)
                WHERE (lower(Foredlingsmetode.foredlingsnavn) NOT LIKE "vasket")
                    AND (Regioner.land LIKE "Rwanda" OR Regioner.land LIKE "Colombia")
        """)
        data = cursor.fetchall()
        printTable(data, "   Brenneri og kaffe fra Rwada eller Colombia, som ikke er vasket:")
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()
