class Stand:
    def __init__(self, codice, superficie, padiglione,prezzo_base):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base
        self.disponibile = True   #stand è ancora libero, quando lo assegno ad un espositore -->false
        self.espositore =None #adesso è vuoto dopo quando lo assegnno diventa  = all'espositore
    #calcolo il prezzo finale per stand base
    def prezzo_finale(self):
        return self.prezzo_base #poi li ridefinisco per le sottoclassi,

    def assegna_espositore(self, espositore):
        self.espositore = espositore
        self.disponibile = False

    def __str__(self):
        #controllo la disponibilità
        if self.disponibile:  #se è self.disponibile allora disponibile
            stato="Disponibile"
        else:
            stato="Non disponibile"
        return f"{self.codice}: Standard | {self.superficie}mq - Padiglione {self.padiglione}- Prezzo {self.prezzo_finale():.2f}€ - {stato} "
    #metodo che controlla se due stand sono uguali attraverso il codice
    def __eq__(self, other):
        return self.codice == other.codice
    #metodo che mi fa il confronto tra due oggetti
    def __lt__(self, other):
        return self.prezzo_finale() < other.prezzo_finale()




