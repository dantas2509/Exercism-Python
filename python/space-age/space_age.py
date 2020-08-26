class SpaceAge:
    def __init__(self, seconds):
        self.convertions = { 'Earth': 1,
                        'Mercury': 0.2408467,
                        'Venus': 0.61519726,
                        'Mars': 1.8808158,
                        'Jupiter': 11.862615,
                        'Saturn': 29.447498,
                        'Uranus': 84.016846,
                        'Neptune': 164.79132}
        self.earthYearInSecond = 31557600
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Earth'], 2)
    def on_mercury(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Mercury'], 2)
    def on_venus(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Venus'], 2)
    def on_mars(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Mars'], 2)
    def on_jupiter(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Jupiter'], 2)
    def on_saturn(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Saturn'], 2)
    def on_uranus(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Uranus'], 2)
    def on_neptune(self):
        return round(self.seconds / self.earthYearInSecond / self.convertions['Neptune'], 2)
    
x = SpaceAge(2134835688)
print(x.on_mercury)
