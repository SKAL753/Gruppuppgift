# Gruppuppgift
Ett grupparbete på programmering nivå 1

Programmet är ett klassiskt Sten, Sax eller Påse-spel där spelaren tävlar mot datorn, som har namnet Python311. Målet är att vinna så många omgångar som möjligt och få fler poäng än datorn när matchen avslutas.

**Spelförlopp:**

Först skapas en lista med de tre möjliga valen: sten, sax och påse. Därefter skapas en dictionary som innehåller reglerna för vilket val som besegrar vilket. Programmet håller även reda på spelarens och datorns poäng.

När spelet startar visas ett välkomstmeddelande och spelaren får ange sitt användarnamn. Därefter får spelaren välja hur många omgångar matchen ska bestå av. Programmet kontrollerar att inmatningen är ett giltigt heltal och ber spelaren försöka igen om inmatningen är felaktig.

När matchen börjar körs en loop som upprepas enligt det valda antalet omgångar. I början av varje omgång väljer datorn slumpmässigt ett av de tre alternativen. Spelaren får sedan ange sitt val. Programmet kontrollerar att inmatningen är giltig och fortsätter fråga tills spelaren har angett sten, sax eller påse.

Därefter jämförs spelarens och datorns val för att avgöra resultatet. Om båda väljer samma alternativ blir det oavgjort och inga poäng delas ut. Om spelarens val besegrar datorns val får spelaren en poäng. I annat fall får datorn en poäng. Resultatet av omgången skrivs sedan ut tillsammans med båda spelarnas val.

När samtliga omgångar är färdigspelade jämför programmet spelarnas poäng för att avgöra vem som vunnit hela matchen. Om spelaren har fler poäng visas ett vinstmeddelande, om poängen är lika blir det oavgjort och annars vinner datorn. Därefter skrivs slutpoängen ut.

Slutligen får spelaren välja om den vill spela igen. Om spelaren svarar ja eller j får den välja ett nytt antal omgångar och en ny match startar. Om spelaren väljer något annat avslutas programmet.
