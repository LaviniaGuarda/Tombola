#  Developer: $ Lavinia
# -*- coding: utf-8 -*-

"""
Classe Cartella: creazione di un modello di cartella.
N.B: di seguito sarà usata la convenzione per cui se una casella della cartella è vuota (non contiene nessun numero) sarà contrassegnata con il numero 0,
se la casella contiene un numero che però è
già stato estratto al posto di tale numero conterrà -1 (casella abbassata)

Attibuti:
-cartella: matrice di dimensioni 3x9 inizialmente contenente tutti 0; in seguito sono inseriti in 15 posizioni i numeri randomici
compresi tra 1 e 90 rispettando le specifiche
-contatore_elem_c: vettore riga di dimensione 1x9 inizlamente inizializzato a 0, incrementato di 1 per ogni numero aggiunto sulla rispettiva
colonna e decerementato di 1 se eliminato
-contatore_elem_r: vettore colonna di dimensione 3x1 inizlamente inizializzato a 0, incrementato di 1 per ogni numero aggiunto sulla rispettiva
riga e decerementato di 1 se eliminato
"""

import numpy as np
import random

class Cartella:

    "Viene creata la cartella come matrice di zeri, "

    def __init__(self, cartella=None, contatore_elem_c=None, contatore_elem_r=None):

        self.cartella = np.zeros((3,9))

        self.contatore_elem_c = np.zeros(9)

        self.contatore_elem_r = np.zeros(3)
       
  

    """ Metodo incrementa_contatore: metodo che aggiorna (incrementando) i contatori rispettivamente degli elementi sulle righe e sulle colonne
        ogni qual volta viene aggiunto un nuovo numero """

    def incrementa_contatore(self, i_riga, i_colonna):

        # i_riga: indice della riga (int)

        # i_colonna=indice della colonna (int)

        self.contatore_elem_r[i_riga] += 1

        self.contatore_elem_c[i_colonna] += 1

    """
    Metodo decrementa_contatore: metodo che aggiorna (decrementando) i contatori rispettivamente degli elementi sulle righe e sulle colonne
    ogni qual volta viene rimosso un numero
    """

    def decrementa_contatore(self, i_riga, i_colonna):

        self.contatore_elem_r[i_riga] -= 1

        self.contatore_elem_c[i_colonna] -= 1

    """
    Metodo aggiungi_numero: metodo che inserisce un numero nella cartella nella posizione specificata gli indici di riga e colonna,
    e per ogni elemento aggiunto utilizza il metodo incrementa_contatore
    """

    def aggiungi_numero(self, i_riga, i_colonna, num):

        "num (int): numero inserito"

        self.cartella[i_riga, i_colonna] = num

        self.incrementa_contatore(i_riga, i_colonna)
        
    """
    Metodo rimuovi_numero: metodo che rimuove un numero nella cartella nella posizione specificata gli indici di riga e colonna,
    e per ogni elemento aggiunto utilizza il metodo decrementa_contatore
    """

    def rimuovi_numero(self, i_riga, i_colonna):

        self.cartella[i_riga, i_colonna] = 0

        self.decrementa_contatore(i_riga, i_colonna)
        

    def azzera_contatore(self):

        self.contatore_elem_c = np.zeros(9)

        self.contatore_elem_r = np.zeros(3)

    """
    Metodo visualizza_elem_cartella: metodo che restituisce l'elemento (int) presente nella cartella che si trova nella posizione
    individuata dell'indice della riga e della colonna
    """

    def visualizza_elem_cartella(self, i_riga, i_colonna):

        elemento = self.cartella[i_riga, i_colonna]

        return elemento

   

    
    """
    metodo che conta gli elelemti di una colonna 
    """
    def conta_elementi_colonne(self, i_colonna):
        return self.contatore_elem_c[i_colonna]



    """
    Metodo check_vincolo_r:metodo che verifica che sia rispettata la specifica sulle righe --> 5 elementi su ognuna
    restituisce in output un booleano (True se la condizione è verificata, False altrimenti)
    """

    def check_vincolo_r(self, i_riga):
       
        if self.contatore_elem_r[i_riga] == 5:

            return True

        else:

            return False

 

    """
    Metodo casella_occuppata: metodo che controlla se la casella individuata da indice riga e indice colonna è occupata, se la
    casella è occupata conterrà un numero da 1 a 90 oppure -1 (numero estratto)
    Restituisce un boolenano: True--> se la casella è occupata
    """

    def casella_occupata(self, i_riga, i_colonna):

        if self.visualizza_elem_cartella(i_riga, i_colonna) !=0:

            return True

        else:

            return False

   

    """
    Metodo numero_estratto: metodo che restituisce un booleano al fine di controllare se il numero nella posizione specificata
    da indice riga e indice colonna è già stato estratto
    True--> numero estratto (=-1 per convenzione del programma)
    """

    def numero_estratto(self, i_riga, i_colonna):

        if self.cartella[i_riga][i_colonna] == -1:

            return True

        else:

            return False

    """
    Metodo canc_cartella_tale metodo rende nuovamente la cartella una matrice di zeri e azzera i contatori
    """
    def canc_cartella(self):
        self.cartella = np.zeros((3,9))
        self.azzera_contatore()

    """
    metodo posizione_libera_colonna:restituisce in una lista gli indici delle posizioni libere per riga.
    """
    def posizione_libera_riga(self,j):
        indici=[]
        for i in range(3):
            if self.cartella[i][j]==0:
                indici.append(i)
            else:
                pass
        return indici


    '''il metodo genera_posizioni_cartella inserisce un numero 1 per ogni colonna (in totale quindi 9), sfruutando le righe che non rispettano il vincolo (<5 elementi) '''

    def genera_posizioni_cartella(self):
        self.canc_cartella()
        for j in range (9):
          rigacorretta=False
          while not rigacorretta:
            c = random.randrange(0,3) 
            if not self.check_vincolo_r(c):
              self.aggiungi_numero(c, j, 1)
              rigacorretta=True
            else:
              rigacorretta=False   

    ''' il metodo genera_cartella inserisce i restanti sei 1 (per arrivare ai 15 numeri per cartella), verificando che non ci siano più di 5 numeri per riga '''
                   
    def genera_cartella(self):
       self.genera_posizioni_cartella()
       exitcondition=False
       while not exitcondition:
           j=random.randint(0,8)
           if len(self.posizione_libera_riga(j))!=0:
             z=self.posizione_libera_riga(j)   
             i=random.choice(z)
             if not self.check_vincolo_r(i):
                 self.aggiungi_numero(i, j, 1)
             if self.check_vincolo_r(0):
               if self.check_vincolo_r(1):
                 if self.check_vincolo_r(2):               
                    exitcondition=True    
       return self.cartella

if __name__ == "__main__":
    cartella1=Cartella()   
    cartella1.genera_cartella()    
    print(cartella1) 
