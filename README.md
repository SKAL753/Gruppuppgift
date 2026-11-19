# Gruppuppgift
Ett grupparbete på programmering nivå 1
jobbade med programmet, inmatningssäkerhet och annat. Fixat ordlista i annan fil och importerat den. fixar svårighets grad och gjort så programmet fungerar för det mesta men har lite kvar. la till kommentarer.

Ordgissning Kodflöde och funktion===

Programmet är ett ordgissningsspel där spelaren ska lista ut ett hemligt ord genom att gissa en bokstav i taget.

Först importeras ordlistan från en separat fil (ordlista.py) plus så importerar jag "random" så jag kan använda det senare för att hitta ett ord i mina listor där det finns massa ord sparade.

Programmet använder flera funktioner för att dela upp arbetet

kontrollera_gissning() kontrollerar att användaren bara skriver in en giltig bokstav och inte gissar samma bokstav flera gånger, det är min inmatningssäkerhet.
visa_ord() visar vilka bokstäver som har gissats rätt och döljer resten med understreck, det gör det fint.
visa_spelstatus() visar hur många försök som finns kvar och vilka bokstäver som gissats fel.
ar_ordet_gissat() kontrollerar om alla bokstäver i ordet har hittats.
Efter att svårighetsgraden valts startar en while-loop som kör spelet så länge spelaren har försök kvar. Rätt gissningar sparas i en lista och fel gissningar sparas i en annan. Vid en felaktig gissning minskar antalet försök med ett. Spelet avslutas när spelaren har gissat hela ordet eller fått slut på försök.

Datalagring===

Informationen sparas tillfälligt i variabler och listor medan spelet körs. De rätta och felaktiga gissningarna lagras separat i två listor. Det hemliga ordet och antalet försök kvar sparas också i variabler. Själva ordlistan ligger i en separat Python-fil som importeras när programmet startar.

Programmet använder ingen permanent databas.
