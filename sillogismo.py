class Sillogismo:
    def __init__(self):
        self.forma_1 = ""
        self.forma_2 = ""
        self.forma_3 = ""

        self.figura = None
        self.frasi = []
        self.modo = ""

        self.modo_1 = {"AAA", "EAE", "AII", "EIO", "AAI", "EAO"}
        self.modo_2 = {"EAE", "AEE", "EIO", "AOO", "EAO", "AEO"}
        self.modo_3 = {"AAI", "IAI", "AII", "EAO", "OAO", "EIO"}
        self.modo_4 = {"AAI", "AEE", "IAI", "EAO", "EIO", "AEO"}
        self.validità = None

        self.premessa_1 = ""
        self.premessa_2 = ""
        self.conclusione = ""

        self.non = "non"

        self.Nessuno = "Nessuno"
        self.Nessuna = "Nessuna"
        self.Nessun = "Nessun"
        self.nessuno = "nessuno"
        self.nessuna = "nessuna"
        self.nessun = "nessun"

        self.Tutti = "Tutti"
        self.Tutte = "Tutte"
        self.tutti = "tutti"
        self.tutte = "tutte"

        self.ha = "ha"
        self.è = "è"
        self.hanno = "hanno"
        self.sono = "sono"
    
        self.Qualche = "Qualche"
        self.qualche = "qualche"

        self.Ogni = "Ogni"
        self.ogni = "ogni"

        self.Alcuni = "Alcuni"
        self.alcuni = "alcuni"
        self.Alcune = "Alcune"
        self.alcune = "alcune"

        self.parole_valide = {self.non, self.Nessuno, self.nessuno, self.Nessuna, self.nessuna, self.Nessun, self.nessun, self.Tutti, self.tutti, self.Tutte, self.tutte, self.ha, self.è, self.hanno, self.sono, self.Qualche, self.qualche, self.Ogni, self.ogni, self.Alcuni, self.alcuni, self.Alcune, self.alcune}
        self.parole_non_valide = {"i", "un", "una", "uno", "gli", "le", "di", "dei", "degli", "negli", "nelle", "sui", "sulle", "nei", "sugli"}

    def testo_iniziale(self):
        print(" ▌ ▐·▄▄▄ .▄▄▄  ▪  ·▄▄▄▪   ▄▄·           ▪  ▄▄▌      ▄▄▄▄▄▄• ▄▌          .▄▄ · ▪  ▄▄▌  ▄▄▌         ▄▄ • ▪  .▄▄ · • ▌ ▄ ·.       ")
        print("▪█·█▌▀▄.▀·▀▄ █·██ ▐▄▄·██ ▐█ ▌▪▪         ██ ██•      •██  █▪██▌▪         ▐█ ▀. ██ ██•  ██•  ▪     ▐█ ▀ ▪██ ▐█ ▀. ·██ ▐███▪▪     ")
        print(" █▐█•▐▀▀▪▄▐▀▀▄ ▐█·██▪ ▐█·██ ▄▄ ▄█▀▄     ▐█·██▪       ▐█.▪█▌▐█▌ ▄█▀▄     ▄▀▀▀█▄▐█·██▪  ██▪   ▄█▀▄ ▄█ ▀█▄▐█·▄▀▀▀█▄▐█ ▌▐▌▐█· ▄█▀▄ ")
        print(" ███ ▐█▄▄▌▐█•█▌▐█▌██▌.▐█▌▐███▌▐█▌.▐▌    ▐█▌▐█▌▐▌     ▐█▌·▐█▄█▌▐█▌.▐▌    ▐█▄▪▐█▐█▌▐█▌▐▌▐█▌▐▌▐█▌.▐▌▐█▄▪▐█▐█▌▐█▄▪▐███ ██▌▐█▌▐█▌.▐▌")
        print(". ▀   ▀▀▀ .▀  ▀▀▀▀▀▀▀ ▀▀▀·▀▀▀  ▀█▄▀▪    ▀▀▀.▀▀▀      ▀▀▀  ▀▀▀  ▀█▄▀▪     ▀▀▀▀ ▀▀▀.▀▀▀ .▀▀▀  ▀█▄▀▪·▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀  █▪▀▀▀ ▀█▄▀▪")
        print(" ----------------- Parole utilizzabili: nessun/o/a, qualche, alcuni/e, tutti/e, ogni, è/non è, ha/non ha. -------------------- ")

    def split(self):
        return input(" Scrivi il sillogismo: ").split(", ")

    def verifica_forma(self, frasi):
        for i in range(-1, len(frasi)):
            if i == 0:
                self.premessa_1 = frasi[0]
                self.premessa_1_parole = self.premessa_1.split(" ")
                for j in range(0, len(self.premessa_1_parole)):
                    if j < len(self.premessa_1_parole):
                        if self.premessa_1_parole[j] in self.parole_non_valide:
                            self.premessa_1_parole.pop(j)
                for n in range(0, len(self.premessa_1_parole)):
                    if n < len(self.premessa_1_parole):
                        if self.Nessun in self.premessa_1_parole or self.Nessuna in self.premessa_1_parole or self.Nessuno in self.premessa_1_parole or self.nessun in self.premessa_1_parole or self.nessuna in self.premessa_1_parole or self.nessuno in self.premessa_1_parole:
                            if self.è in self.premessa_1_parole or self.ha in self.premessa_1_parole:
                                self.forma_1 = "E"
                            elif self.non in self.premessa_1_parole and self.è in self.premessa_1_parole or self.non in self.premessa_1_parole and self.ha in self.premessa_1_parole:
                                self.forma_1 = "A"
                        elif self.Tutti in self.premessa_1_parole or self.Tutte in self.premessa_1_parole or self.tutti in self.premessa_1_parole or self.tutte in self.premessa_1_parole:
                            if self.sono in self.premessa_1_parole or self.hanno in self.premessa_1_parole:
                                self.forma_1 = "A"
                            elif self.non in self.premessa_1_parole and self.sono in self.premessa_1_parole or self.non in self.premessa_1_parole and self.hanno in self.premessa_1_parole:
                                self.forma_1 = "E"
                        elif self.Qualche in self.premessa_1_parole or self.qualche in self.premessa_1_parole:
                            if self.ha in self.premessa_1_parole or self.è in self.premessa_1_parole:
                                self.forma_1 = "I"
                            elif self.non in self.premessa_1_parole and self.ha in self.premessa_1_parole or self.non in self.premessa_1_parole and self.è in self.premessa_1_parole:
                                self.forma_1 = "O"
                        elif self.Alcuni in self.premessa_1_parole or self.Alcune in self.premessa_1_parole or self.alcuni in self.premessa_1_parole or self.alcune in self.premessa_1_parole:
                            if self.hanno in self.premessa_1_parole or self.sono in self.premessa_1_parole:
                                self.forma_1 = "I"
                            elif self.non in self.premessa_1_parole and self.hanno in self.premessa_1_parole or self.non in self.premessa_1_parole and self.sono in self.premessa_1_parole:
                                self.forma_1 = "O"
                        elif self.Ogni in self.premessa_1_parole or self.ogni in self.premessa_1_parole:
                            if self.hanno in self.premessa_1_parole or self.sono in self.premessa_1_parole:
                                self.forma_1 = "I"
                            elif self.ha in self.premessa_1_parole or self.è in self.premessa_1_parole:
                                self.forma_1 = "I"
                            elif self.non in self.premessa_1_parole and self.hanno in self.premessa_1_parole or self.non in self.premessa_1_parole and self.sono in self.premessa_1_parole:
                                self.forma_1 = "O"
                            elif self.non in self.premessa_1_parole and self.ha in self.premessa_1_parole or self.non in self.premessa_1_parole and self.è in self.premessa_1_parole:
                                self.forma_1 = "O"
                        
                        if self.premessa_1_parole[n] in self.parole_valide:
                            self.premessa_1_parole.pop(n)
            elif i == 1:
                self.premessa_2 = frasi[1]
                self.premessa_2_parole = self.premessa_2.split(" ")
                for j in range(0, len(self.premessa_2_parole)):
                    if j < len(self.premessa_2_parole):
                        if self.premessa_2_parole[j] in self.parole_non_valide:
                            self.premessa_2_parole.pop(j)
                for n in range(0, len(self.premessa_2_parole)):
                    if n < len(self.premessa_2_parole):
                        if self.Nessun in self.premessa_2_parole or self.Nessuna in self.premessa_2_parole or self.Nessuno in self.premessa_2_parole or self.nessun in self.premessa_2_parole or self.nessuna in self.premessa_2_parole or self.nessuno in self.premessa_2_parole:
                            if self.è in self.premessa_2_parole or self.ha in self.premessa_2_parole:
                                self.forma_2 = "E"
                            elif self.non in self.premessa_2_parole and self.è in self.premessa_2_parole or self.non in self.premessa_2_parole and self.ha in self.premessa_2_parole:
                                self.forma_2 = "A"
                        elif self.Tutti in self.premessa_2_parole or self.Tutte in self.premessa_2_parole or self.tutti in self.premessa_2_parole or self.tutte in self.premessa_2_parole:
                            if self.sono in self.premessa_2_parole or self.hanno in self.premessa_2_parole:
                                self.forma_2 = "A"
                            elif self.non in self.premessa_2_parole and self.sono in self.premessa_2_parole or self.non in self.premessa_2_parole and self.hanno in self.premessa_2_parole:
                                self.forma_2 = "E"
                        elif self.Qualche in self.premessa_2_parole or self.qualche in self.premessa_2_parole:
                            if self.ha in self.premessa_2_parole or self.è in self.premessa_2_parole:
                                self.forma_2 = "I"
                            elif self.non in self.premessa_2_parole and self.ha in self.premessa_2_parole or self.non in self.premessa_2_parole and self.è in self.premessa_2_parole:
                                self.forma_2 = "O"
                        elif self.Alcuni in self.premessa_2_parole or self.Alcune in self.premessa_2_parole or self.alcuni in self.premessa_2_parole or self.alcune in self.premessa_2_parole:
                            if self.hanno in self.premessa_2_parole or self.sono in self.premessa_2_parole:
                                self.forma_2 = "I"
                            elif self.non in self.premessa_2_parole and self.hanno in self.premessa_2_parole or self.non in self.premessa_2_parole and self.sono in self.premessa_2_parole:
                                self.forma_2 = "O"
                        elif self.Ogni in self.premessa_2_parole or self.ogni in self.premessa_2_parole:
                            if self.hanno in self.premessa_2_parole or self.sono in self.premessa_2_parole:
                                self.forma_2 = "I"
                            elif self.ha in self.premessa_2_parole or self.è in self.premessa_2_parole:
                                self.forma_2 = "I"
                            elif self.non in self.premessa_2_parole and self.hanno in self.premessa_2_parole or self.non in self.premessa_2_parole and self.sono in self.premessa_2_parole:
                                self.forma_2 = "O"
                            elif self.non in self.premessa_2_parole and self.ha in self.premessa_2_parole or self.non in self.premessa_2_parole and self.è in self.premessa_2_parole:
                                self.forma_2 = "O"
                                
                        if self.premessa_2_parole[n] in self.parole_valide:
                            self.premessa_2_parole.pop(n)
            elif i == 2:
                self.conclusione = frasi[2]
                self.conclusione_parole = self.conclusione.split(" ")
                for j in range(0, len(self.conclusione_parole)):
                    if j < len(self.conclusione_parole):
                        if self.conclusione_parole[j] in self.parole_non_valide:
                            self.conclusione_parole.pop(j)
                for n in range(0, len(self.conclusione_parole)):
                    if n < len(self.conclusione_parole):
                        if self.Nessun in self.conclusione_parole or self.Nessuna in self.conclusione_parole or self.Nessuno in self.conclusione_parole or self.nessun in self.conclusione_parole or self.nessuna in self.conclusione_parole or self.nessuno in self.conclusione_parole:
                            if self.è in self.conclusione_parole or self.ha in self.conclusione_parole:
                                self.forma_3 = "E"
                            elif self.non in self.conclusione_parole and self.è in self.conclusione_parole or self.non in self.conclusione_parole and self.ha in self.conclusione_parole:
                                self.forma_3 = "A"
                        elif self.Tutti in self.conclusione_parole or self.Tutte in self.conclusione_parole or self.tutti in self.conclusione_parole or self.tutte in self.conclusione_parole:
                            if self.sono in self.conclusione_parole or self.hanno in self.conclusione_parole:
                                self.forma_3 = "A"
                            elif self.non in self.conclusione_parole and self.sono in self.conclusione_parole or self.non in self.conclusione_parole and self.hanno in self.conclusione_parole:
                                self.forma_3 = "E"
                        elif self.Qualche in self.conclusione_parole or self.qualche in self.conclusione_parole:
                            if self.ha in self.conclusione_parole or self.è in self.conclusione_parole:
                                self.forma_3 = "I"
                            elif self.non in self.conclusione_parole and self.ha in self.conclusione_parole or self.non in self.conclusione_parole and self.è in self.conclusione_parole:
                                self.forma_3 = "O"
                        elif self.Alcuni in self.conclusione_parole or self.Alcune in self.conclusione_parole or self.alcuni in self.conclusione_parole or self.alcune in self.conclusione_parole:
                            if self.hanno in self.conclusione_parole or self.sono in self.conclusione_parole:
                                self.forma_3 = "I"
                            elif self.non in self.conclusione_parole and self.hanno in self.conclusione_parole or self.non in self.conclusione_parole and self.sono in self.conclusione_parole:
                                self.forma_3 = "O"
                        elif self.Ogni in self.conclusione_parole or self.ogni in self.conclusione_parole:
                            if self.hanno in self.conclusione_parole or self.sono in self.conclusione_parole:
                                self.forma_3 = "I"
                            elif self.ha in self.conclusione_parole or self.è in self.conclusione_parole:
                                self.forma_3 = "I"
                            elif self.non in self.conclusione_parole and self.hanno in self.conclusione_parole or self.non in self.conclusione_parole and self.sono in self.conclusione_parole:
                                self.forma_3 = "O"
                            elif self.non in self.conclusione_parole and self.ha in self.conclusione_parole or self.non in self.conclusione_parole and self.è in self.conclusione_parole:
                                self.forma_3 = "O"
                        
                        if self.conclusione_parole[n] in self.parole_valide:
                            self.conclusione_parole.pop(n)

        return self.forma_1 + self.forma_2 + self.forma_3

    def verifica_validità(self, figure):
        if figure in self.modo_1:
            self.validità = True
        elif figure in self.modo_2:
            self.validità = True
        elif figure in self.modo_3:
            self.validità = True
        elif figure in self.modo_4:
            self.validità = True
        else:
            self.validità = False
            print("Sillogismo non valido!")
        
        return self.validità

    def verifica_figura(self, premessa_1, premessa_2, conclusione):
        if len(premessa_1) == 2 and len(premessa_2) == 2:
            if premessa_1[0] == premessa_2[0]:
                self.figura = 3
                return self.figura
            elif premessa_1[0] == premessa_2[1]:
                self.figura = 1
                return self.figura
            elif premessa_1[1] == premessa_2[0]:
                self.figura = 4
                return self.figura
            elif premessa_1[1] == premessa_2[1]:
                self.figura = 2
                return self.figura
            else:
                self.validità = False
                print("Sillogismo non valido!")
        else:
            print("Perfavore inserisci un sostantivo composto da una sola parola nelle frasi!")

    def main(self):
        self.testo_iniziale()
        self.frasi = self.split()
        self.modo = self.verifica_forma(self.frasi)
        self.validità = self.verifica_validità(self.modo)

        if self.validità:
            self.figura = self.verifica_figura(self.premessa_1_parole, self.premessa_2_parole, self.conclusione_parole)
        
        if self.validità:
            print("Il sillogismo è corretto!")
            print(f"Figura: {self.figura}")
            print(f"Modo: {self.modo}")

Sillogismo().main()