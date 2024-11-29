# Létrehozunk egy légitársaságot
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
