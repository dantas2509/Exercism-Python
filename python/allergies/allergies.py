class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        allergieList = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']
        allergicTo = list()
        pos = 0
        aux = self.score
        while 2 ** pos < self.score:
            pos += 1

        while pos >= 0 and aux > 0:
            if 2 ** pos <= aux:
                aux -= 2 ** pos
                if pos < len(allergieList):
                    allergicTo.append(allergieList[pos])
            pos -= 1
        return allergicTo