from stand import Stand
class StandPresaExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice,superficie,padiglione,prezzo_base)
        self.numero_prese = numero_prese

    def prezzo_finale(self):
        return self.prezzo_base * (1+0.07*self.numero_prese)


    def __str__(self):
        return f"{self.codice} : Prese Extra | {self.superficie}mq - Padiglione {self.padiglione}- Prezzo {self.prezzo_finale():.2f}€ - Prese aggiuntive {self.numero_prese}"


class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione,prezzo_base, posizione):
        super().__init__(codice,superficie, padiglione, prezzo_base)

        self.posizione = posizione

    def prezzo_finale(self):
        return self.prezzo_base *1.30

    def __str__(self):
        return f"{self.codice}: Premium | {self.superficie}mq - Padiglione {self.padiglione}- Prezzo {self.prezzo_finale():.2f}€ - Posizione {self.posizione}"

