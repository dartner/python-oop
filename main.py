# Létrehozunk egy légitársaságot
from foglalas import FoglalasiRendszer
from jarat import BelfoldiJarat, NemzetkoziJarat
from legi_tarsasag import LegiTarsasag

# tesztadatok betöltése
wizzair = LegiTarsasag("WizzAir")
jarat1 = BelfoldiJarat("W123", "Budapest", 15000)
jarat2 = NemzetkoziJarat("W456", "London", 45000)
jarat3 = NemzetkoziJarat("W789", "New York", 120000)

wizzair.jarat_hozzaadas(jarat1)
wizzair.jarat_hozzaadas(jarat2)
wizzair.jarat_hozzaadas(jarat3)

ryanair = LegiTarsasag("Ryanair")
jarat4 = BelfoldiJarat("R123", "Debrecen", 12000)
jarat5 = NemzetkoziJarat("R456", "Berlin", 40000)
ryanair.jarat_hozzaadas(jarat4)
ryanair.jarat_hozzaadas(jarat5)

# Foglalási rendszer létrehozása
rendszer = FoglalasiRendszer()
rendszer.legitarsasag_hozzaadas(wizzair)
rendszer.legitarsasag_hozzaadas(ryanair)

# Foglalások hozzáadása
rendszer.jegy_foglalasa("WizzAir", "W123", "Kiss János")
rendszer.jegy_foglalasa("WizzAir", "W456", "Nagy Anna")
rendszer.jegy_foglalasa("Ryanair", "R123", "Tóth Béla")
rendszer.jegy_foglalasa("WizzAir", "W123", "Nagy János")
rendszer.jegy_foglalasa("Ryanair", "R456", "Kiss Anna")
rendszer.jegy_foglalasa("WizzAir", "W789", "Kovács Béla")


def cli_menu():
    print("\n--- Repülőjegy Foglalási Rendszer ---")
    print("1. Járatok listázása")
    print("2. Jegy foglalása")
    print("3. Foglalások listázása")
    print("4. Foglalás lemondása")
    print("5. Kilépés")


while True:
    cli_menu()
    valasztas = input("Válasszon egy lehetőséget: ")

    if valasztas == "1":
        # Légitársaságok listázása és járatok megjelenítése
        rendszer.listaz_legitarsasagokat()
        legitarsasag_nev = input("Adja meg a légitársaság nevét a járatok megtekintéséhez: ")
        legitarsasag = next((lt for lt in rendszer.legitarsasagok if lt.nev == legitarsasag_nev), None)
        if legitarsasag:
            legitarsasag.listaz_jaratokat()
        else:
            print("Nincs ilyen nevű légitársaság.")
    elif valasztas == "2":
        # Jegy foglalása
        rendszer.listaz_legitarsasagokat()
        legitarsasag_nev = input("Adja meg a légitársaság nevét: ")
        jaratszam = input("Adja meg a járatszámot: ")
        utas_neve = input("Adja meg az utas nevét: ")
        rendszer.jegy_foglalasa(legitarsasag_nev, jaratszam, utas_neve)
    elif valasztas == "3":
        # Foglalások listázása
        rendszer.listaz_foglalasok()
    elif valasztas == "4":
            # Foglalás lemondása
            rendszer.listaz_legitarsasagokat()
            legitarsasag_nev = input("Adja meg a légitársaság nevét: ")
            jaratszam = input("Adja meg a járatszámot: ")
            utas_neve = input("Adja meg az utas nevét: ")
            rendszer.foglalas_lemondasa(legitarsasag_nev, jaratszam, utas_neve)
    elif valasztas == "5":
        # Kilépés
        print("Kilépés a rendszerből. Viszlát!")
        break
    else:
        print("Hibás választás. Próbálja újra!")

