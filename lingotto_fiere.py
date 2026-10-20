from espositore import Espositore
from stand import Stand
from StandSpeciali import StandPresaExtra, StandPremium
from operator import attrgetter

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome= nome
        self.espositori = {}
        self.stand={}

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome =nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        try:
            filein=open(file_path,'r',encoding="utf-8")
            for riga in filein:
                campi= riga.strip().split(",")
                codice= campi[0]
                if codice.startswith("ST"):
                    superficie= int(campi[1].strip())
                    padiglione= int(campi[2].strip())
                    prezzo_base= float(campi[3].strip())
                    if len(campi) == 4:
                        StandBase=Stand(codice,superficie, padiglione, prezzo_base)
                        self.stand[codice]=StandBase
                    elif len(campi) == 5:
                        if campi[4].isdigit():
                            numero_prese= int(campi[4])
                            StandExtra=StandPresaExtra(codice, superficie, padiglione, prezzo_base, numero_prese)
                            self.stand[codice]=StandExtra
                        else:
                            posizione= campi[4]
                            StrandP=StandPremium(codice,superficie,padiglione, prezzo_base,posizione)
                            self.stand[codice]=StrandP

                elif codice.startswith("ES"):
                    nome=campi[1]
                    cognome= campi[2]
                    espositore=Espositore(codice,nome,cognome)
                    self.espositori[codice]=espositore

        except FileNotFoundError:
            print( f"file {file_path} non trovato")



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        #controllo se esiste lo stand
        if codice_stand not in self.stand:
            raise Exception("Stand non trovato")

        stand = self.stand[codice_stand]

        # controllo se esiste l'espositore
        if codice_espositore not in self.espositori:
            raise Exception("Espositore non trovato")

        espositore = self.espositori[codice_espositore]

        # controllo che lo stand sia disponibile
        if not stand.disponibile:
            raise Exception("Stand non disponibile")

        # controllo che l'espositore non abbia già uno stand
        if espositore.stand is not None:
            raise Exception("Espositore già associato")

        # abbino lo stand all'espositore
        stand.disponibile = False
        stand.espositore = espositore
        espositore.stand = stand



    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for codice in self.espositori:
            espositore = self.espositori[codice]
            print(f"{espositore}")
    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand.values(),key=attrgetter('prezzo_base'))
