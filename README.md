# Gruppuppgift
Ett grupparbete på programmering nivå 1

Mastermind spelet
Dokumentation 

Programmet är ett Mastermind-liknande sifferbaserat spel där spelaren ska lista ut ett hemligt fyrsiffrigt nummer med maximalt 12 försök.

**Spelförlopp:**

Först visas ett välkomstmeddelande och spelaren får välja mellan två svårighetsgrader: lätt eller svår. Därefter genereras ett slumpmässigt fyrsiffrigt nummer utifrån spelarens val. På den lätta svårighetsgraden kan varje siffra endast förekomma en gång, medan den svåra svårighetsgraden tillåter upprepade siffror.

När spelet startar körs en loop med maximalt 12 omgångar, där varje omgång motsvarar en gissning. Spelaren får ange en fyrsiffrig gissning som sparas tillsammans med tidigare gissningar i en lista. Programmet jämför sedan gissningen med det korrekta numret och genererar feedback i form av symbolerna ✔ och ☐. Symbolen ✔ betyder att en siffra är korrekt och står på rätt plats, medan ☐ betyder att en siffra är korrekt men står på fel plats. Feedbacken visas utan någon särskild ordning, vilket innebär att spelaren inte får veta vilka specifika siffror som är rätt.

Efter varje gissning skrivs en tabell ut med samtliga tidigare försök, tillhörande gissningar och feedback. Slutligen kontrollerar programmet om spelaren har gissat rätt. Om hela numret är korrekt visas ett vinstmeddelande och spelet avslutas. Annars fortsätter spelet tills spelaren antingen gissar rätt eller förbrukar samtliga 12 försök.

