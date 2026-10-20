class Espositore:
    def __init__(self,codice,nome, cognome):
        self.codice=codice
        self.nome=nome
        self.cognome=cognome
        self.stand =None  #None stato in cui non è stato ancora assegnato nessun stand metto in relazione le due classi,
                        #come chiave di legame


    def __str__(self):
        if self.stand == None:
            return f"{self.codice} : {self.nome} {self.cognome}- Nessun stand assegnato"
        return f"{self.codice}: {self.nome}- {self.cognome}- {self.stand.codice}"  #assegno all'espositore stand con scritto il codice