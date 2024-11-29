# Létrehozunk egy légitársaságot
from foglalas import FoglalasiRendszer
from jarat import BelfoldiJarat, NemzetkoziJarat
from legi_tarsasag import LegiTarsasag


wizzair = LegiTarsasag("WizzAir")

# Hozzáadunk néhány járatot
jarat1 = BelfoldiJarat("W123", "Budapest", 15000)
jarat2 = NemzetkoziJarat("W456", "London", 45000)
jarat3 = NemzetkoziJarat("W789", "New York", 120000)

wizzair.jarat_hozzaadas(jarat1)
wizzair.jarat_hozzaadas(jarat2)
wizzair.jarat_hozzaadas(jarat3)

# Járatok listázása
wizzair.listaz_jaratokat()

# Foglalási rendszer létrehozása
rendszer = FoglalasiRendszer()

# Foglalások hozzáadása
rendszer.jegy_foglalasa(jarat1, "Kiss János")
rendszer.jegy_foglalasa(jarat2, "Nagy Anna")
rendszer.jegy_foglalasa(jarat3, "Tóth Béla")

# Foglalások listázása
rendszer.listaz_foglalasok()

# Foglalás lemondása
rendszer.foglalas_lemondasa("Nagy Anna")

# Frissített foglalások listázása
rendszer.listaz_foglalasok()
