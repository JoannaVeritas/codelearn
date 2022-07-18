class Kobieta:

    def __init__(self, wiek, kolor_wlosow):
        self.wiek = wiek
        self.kolor = kolor_wlosow
        self.opisKoloru = {
            "blond": "madra!",
            "szatynka": "odwazna",
            "brunetka": "silna"    
        }


    
    def opiszSiebie(self):
        wiekOpis = ""
        if (self.wiek) < 25:
            wiekOpis = "Jestem mloda" 
        else: 
            wiekOpis = "Jestem nadal mloda"

        kolorOpis = ""
        if self.kolor not in self.opisKoloru:
            kolorOpis = "zwariowana"
        else:
            kolorOpis = self.opisKoloru[self.kolor]

        print(wiekOpis + " i " + kolorOpis)

k1 = Kobieta(19, "blond")
k2 = Kobieta(2, 'brunetka')
k3 = Kobieta(66, 'szatynka')
k4 = Kobieta (23, 'platyna')
k5 = Kobieta (30, 'blond')

lista_kobiet = []
lista_kobiet.append(k1)
lista_kobiet.append(k2)
lista_kobiet.append(k3)
lista_kobiet.append(k4)
lista_kobiet.append(k5)
#+print(lista_kobiet) # eeeeee....
(lista_kobiet[1].opiszSiebie()) # hmmmmmmm

n = 0
while n <10:
    kobieta = lista_kobiet[n]
    kobieta.opiszSiebie()
    n = n + 1

for i in lista_kobiet:
    i.opiszSiebie()

#k1.opiszSiebie()
#k2.opiszSiebie()