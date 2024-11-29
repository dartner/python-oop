from jarat import Jarat


class JegyFoglalas:
    def __init__(self, jarat, utas_neve):
        self.jarat = jarat
        self.utas_neve = utas_neve

    def __str__(self):
        return f"Foglalás: {self.utas_neve} - {self.jarat}"
    

class FoglalasiRendszer:
    def __init__(self):
        self.foglalasok = []
        self.legitarsasagok = []

    def legitarsasag_hozzaadas(self, legitarsasag):
        self.legitarsasagok.append(legitarsasag)

    def jegy_foglalasa(self, legitarsasag_nev, jaratszam, utas_neve):
        legitarsasag = next((lt for lt in self.legitarsasagok if lt.nev == legitarsasag_nev), None)
        if not legitarsasag:
            print(f"Nincs ilyen nevű légitársaság: {legitarsasag_nev}")
            return

        jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == jaratszam), None)
        if not jarat:
            print(f"Nincs ilyen járat a(z) {legitarsasag_nev} légitársaságnál: {jaratszam}")
            return

        foglalas = JegyFoglalas(jarat, utas_neve)
        self.foglalasok.append(foglalas)
        print(f"Sikeresen lefoglalt egy jegyet: {foglalas}")

    def foglalas_lemondasa(self, legitarsasag_nev, jaratszam, utas_neve):
        legitarsasag = next((lt for lt in self.legitarsasagok if lt.nev == legitarsasag_nev), None)
        if not legitarsasag:
            print(f"Nincs ilyen nevű légitársaság: {legitarsasag_nev}")
            return

        jarat = next((j for j in legitarsasag.jaratok if j.jaratszam == jaratszam), None)
        if not jarat:
            print(f"Nincs ilyen járat a(z) {legitarsasag_nev} légitársaságnál: {jaratszam}")
            return

        for foglalas in self.foglalasok:
            if foglalas.utas_neve == utas_neve and foglalas.jarat == jarat:
                self.foglalasok.remove(foglalas)
                print(f"Sikeresen törölte a foglalást: {utas_neve} - {legitarsasag_nev} ({jaratszam})")
                return
        print(f"Nem található foglalás az adott adatokkal: {utas_neve}, {legitarsasag_nev}, {jaratszam}")

    def listaz_foglalasok(self):
        if not self.foglalasok:
            print("Nincsenek aktív foglalások.")
        else:
            print("Aktív foglalások:")
            for foglalas in self.foglalasok:
                print(foglalas)

    def listaz_legitarsasagokat(self):
        print("Elérhető légitársaságok:")
        for lt in self.legitarsasagok:
            print(lt.nev)
