
CREATE TABLE Bruker (
email varchar(30) NOT NULL,
navn varchar(50),
passord varchar(20) NOT NULL,
CONSTRAINT Bruker_PK PRIMARY KEY (email)
);

CREATE TABLE Foredlingsmetode(
foredlingsnavn varchar(30),
beskrivelse varchar(140),
CONSTRAINT Foredlingsmetode_PK PRIMARY KEY (foredlingsnavn)
);

CREATE TABLE Regioner(
regionID integer NOT NULL,
navn varchar(30),
land varchar(30),
CONSTRAINT Regioner_PK PRIMARY KEY (regionID)
);

CREATE TABLE Kaffegaard(
gaardID integer NOT NULL,
moh integer,
navn varchar(30),
region integer,
CONSTRAINT Kaffegaard_PK PRIMARY KEY (gaardID),
CONSTRAINT Kaffegaard_FK1 FOREIGN KEY (region) REFERENCES Regioner(regionID)
	ON UPDATE CASCADE
	ON DELETE NO ACTION
);


CREATE TABLE KaffeParti (
partiID integer NOT NULL,
foreldringsnavn varchar(30) NOT NULL,
kilopris real,
gaardID integer NOT NULL,
innhoestelsesaar integer(4),
CONSTRAINT kaffeParti_PK PRIMARY KEY (partiID),
CONSTRAINT kaffeParti_FK1 FOREIGN KEY (foreldringsnavn) REFERENCES Foredlingsmetode(foredlingsnavn)
	ON UPDATE CASCADE
	ON DELETE NO ACTION,
CONSTRAINT kaffeParti_FK2 FOREIGN KEY (gaardID) REFERENCES Kaffegaard(gaardID)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);


CREATE TABLE FerdigbrentKaffe(
kaffeNavn varchar(30) NOT NULL,
partiID integer NOT NULL,
dato date NOT NULL,
brenneri varchar(30) NOT NULL,
brenningsgrad varchar(30),
beskrivelse varchar(140),
kilopris real,
CONSTRAINT FerdigbrentKaffe_PK PRIMARY KEY (kaffeNavn, brenneri),
CONSTRAINT FerdigbrentKaffe_FK1 FOREIGN KEY (partiID) REFERENCES KaffeParti(partiID)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);

CREATE TABLE KaffeSmaking (
email varchar(30) NOT NULL,
kaffeNavn varchar(30) NOT NULL,
brenneri varchar(30) NOT NULL,
tidspunkt datetime NOT NULL,
score integer,
kommentar varchar(140),
CONSTRAINT KaffeSmaking_PK PRIMARY KEY (email, kaffeNavn, brenneri, tidspunkt ),
CONSTRAINT KaffeSmaking_FK1 FOREIGN KEY (email) REFERENCES Bruker(email)
	ON UPDATE CASCADE
	ON DELETE NO ACTION,
CONSTRAINT KaffeSmaking_FK2 FOREIGN KEY (kaffeNavn) REFERENCES FerdigBrentKaffe(kaffeNavn)
	ON UPDATE CASCADE
	ON DELETE CASCADE
);


CREATE TABLE KaffeBonne(
navn varchar(30) NOT NULL,
art varchar(30),
CONSTRAINT KaffeBonne_PK PRIMARY KEY (navn)
);

CREATE TABLE BestaarAv(
partiID integer NOT NULL,
navn varchar(30) NOT NULL,
CONSTRAINT BestaarAv_PK PRIMARY KEY (partiID, navn),
CONSTRAINT BestaarAv_FK1 FOREIGN KEY (partiID) REFERENCES KaffeParti(partiID)
	ON UPDATE CASCADE
	ON DELETE NO ACTION,
CONSTRAINT BestaarAv_FK2 FOREIGN KEY (navn) REFERENCES KaffeBonne(Navn)
	ON UPDATE CASCADE
	ON DELETE NO ACTION
);


CREATE TABLE DyrketAv(
navn varchar(30) NOT NULL,
gaardID integer NOT NULL,
CONSTRAINT DyrketAv_PK PRIMARY KEY (navn, gaardID),
CONSTRAINT DyrketAv_FK1 FOREIGN KEY (navn) REFERENCES Kaffebonne(navn)
	ON UPDATE CASCADE
	ON DELETE NO ACTION,
CONSTRAINT DyrketAv_FK2 FOREIGN KEY (gaardID) REFERENCES KaffeGaard(gaardID)
	ON UPDATE CASCADE
	ON DELETE NO ACTION
);