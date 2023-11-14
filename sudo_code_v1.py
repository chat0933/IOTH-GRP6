"""
HUSK!!!!!:
AT LAVE ET VIRTUAL ENVIROMENT!!!
NAVNE PÅ VARIABLER ER SKREVET MED SMÅT OG MELLEMRUMS ERSTATNING ER : _ dvs. her_er_et_variable_navn
BRUG IKKE ENKELTE BOGSTAVER TIL VARIABLE NAVNE
KALD FUNKTIONS NAVNENE NOGET SOM GIVER MENING I FORHOLD TIL HVAD DE GØR
KLASSER SKAL STARTE MED STORT BOGSTAV
LAV KUN KLASSER HVIS DEN INDEHOLDER FLERE FUNKTIONER SOM SKAL BRUGES FORSKELLIGE STEDER


Hjertemåler
- Checker pulsen på patinet
- if statements, med else if og else
- Hvis pulsen er for lav (else if) så send en advarsel til database som viser advarslen på hjemmesiden
og aktiver buzzer
- Hvis den er tilpads så vær inaktiv (else)
- MÅSKE: (for høj Så send til database)

Gyroskop:
- Hold øje med om personen står op eller er faldet
- if statements checker
- Hvis de står op så gør ikke noget
- Hvis de er faldet så skriv det ind i databasen med deres koodrinater fra GPS
- Vis data på hjemmesiden
- Se på om vi kan zigge Google Maps api :D

Buzzer:
- Anvender Gyroskop data til at allarmere folk at der er en som er faldet
- if statement checker
- Hvis de står op så gør ikke noget
- Hvis de er faldet så giv lyd
- (Vi skal lige blive enige om buzzeren skal give lyd i andre situationer)
- Hvis hjerterytme er lav så giv lyd!

GPS:
- Fortæl lægerne hvor patienten befinde sig
- Hvis der er hjerteproblemer eller personen er faldet så send data fra gps og hjerterytme/ om de er faldet ind i DB

DB:
- Modtager data fra vores komponenter og alt afhængig af hvad der er problemet opdatere den hjemmesiden og allarmere sunhedspersonalet
- Vi laver en enkelt database hvori alt fra vores sensorer bliver sendt til i den samme table
- Hvis fx hjerterytme er okay men patienten er faldet, så send alt data til database
og vis på hjemmesiden at hjerterytme er stabil men patienten er faldet samt deres GPS koordinat :D
- GPS skal altid sendes!!!! hvis der opstår noget

Andet:
- Brug sleep så vi ikke spammer DB
- Husk at åben og luk DB for sikkerheds skyld og for at den kan opdateres

Hjemmside:
- Vis hvad der står i DB på hjemmesiden
- Aktuator: En form for alarm når der opstår et problem (RØD SKÆRM / LYD)
- login (MFA,)
- https: Vi vil opnå https gennem hosting på azure appservice
- MQTT sender vores data fra database til hjemmeside
"""
# Ny version