class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def listaz_jaratokat(self):
        print(f"Légi társaság: {self.nev}")
        for jarat in self.jaratok:
            print(jarat)