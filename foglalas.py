class JegyFoglalas:
    def __init__(self, jarat, utas_neve):
        self.jarat = jarat
        self.utas_neve = utas_neve

    def __str__(self):
        return f"Foglalás: {self.utas_neve} - {self.jarat}"