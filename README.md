# datdatInnlevering

Beskrivelse av applikasjonen:

Når man kjører index.py er det første som blir kjørt 'user interface'-delen. Den spør først om det er en ny bruker. Hvis man svarer ja, kan man skrive inn den nødvendige informasjonen som man blir bedt om, og dette blir lagt inn i tabellen 'Bruker' gjennom funkjsonen newUser(). Hvis man svarer nei, blir man bedt om å logge inn. Da skal man skrive inn innloggingsinformasjonen sin, og hvis den stemmer overens med brukertabellen, vil variabelen session bli true, i tillegg til at klassen User blir instansiert. Under er innloggingsinformasjonen til en bruker vi har lagt inn:

email: bruker@gmail.com
passord: hei

Når session er true får du alternaiver over hva du vil gjøre. Her kan du vurdere en kaffe, sette inn ny informasjon i en tabell, teste brukerhistorier eller logge ut.
Vi valgte å gjøre det mulig å sette informasjon inn i tabellen selv om det ikke er presisert i oppgaven, fordi dette gjør det enklere for oss når vi skal ha informasjon som vi kan teste ut.
Når man skal teste ut brukerhistoriene kan man velge hvilken brukerhistoriene som ble presisert i oppgaven. Vi gikk ut ifra at man ikke trenger å lage brukergrensesnitt som gir andre valgmuligheter enn det som er spesifisert i brukerhistoriene, ettersom at dette ikke er nevnt i oppgaven.

Når man skal skrive inn inputs for å legge ny informasjon inn i en tabell, eller logge inn, bruker vi en valideringsfunksjon som heter cleanInput(datatype). Den sjekker at datatypen i inputen stemmer overens med det som er forventet, for at man skal unngå at det skjer noen feil. Funksjonen sørger også for at man ikke kan bruke tegn som man kan finne i sql spørringer, for å gjøre systemet mer robust, slik at en ondsinnet bruker ikke skal kunne gjøre skade på databasen. I tillegg til dette er passordene hashet, slik at man ikke kan logge seg inn på en bruker man ikke eier. På et slikt prosjekt er det gunstig å ha tilgang til passordene til brukerne, så påssordene står nedenfor.

oversikt over brukere (ikke slett siden passordene er hashet):
tob@gmail.com Tobias Fremming passord
torbjorn@gmail.com torbjørn vatne passord123
bruker@gmail.com bruker brukersen hei
test@ntnu.no test bruker test passord
torbvat@stud.no Test test test 123
torbvat@stud.ntnu.no Torbjørn Vatne 1234
torbvat@ntnu.no Torbjørn V 12345
test2@ntnu.no test2 navn 321
