class JegyFoglalas:
    def __init__(self, jarat, utas_neve):
        self.jarat = jarat
        self.utas_neve = utas_neve

    def __str__(self):
        return f"Foglalás: {self.utas_neve} - {self.jarat}"
    

class FoglalasiRendszer:
    def __init__(self):
        self.foglalasok = []

    def jegy_foglalasa(self, jarat, utas_neve):
        foglalas = JegyFoglalas(jarat, utas_neve)
        self.foglalasok.append(foglalas)
        print(f"Sikeresen lefoglalt egy jegyet: {foglalas}")

    def foglalas_lemondasa(self, utas_neve):
        for foglalas in self.foglalasok:
            if foglalas.utas_neve == utas_neve:
                self.foglalasok.remove(foglalas)
                print(f"Sikeresen törölte a foglalást: {utas_neve}")
                return
        print(f"Nem található foglalás az utas neve alatt: {utas_neve}")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek aktív foglalások.")
        else:
            print("Aktív foglalások:")
            for foglalas in self.foglalasok:
                print(foglalas)
