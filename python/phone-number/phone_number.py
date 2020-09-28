class PhoneNumber:
    def __init__(self, number):
        self.number = self.cleanNumber(number)
        self.area_code = self.number[:3]

    def cleanNumber(self, number):
        import re
        pattern = re.compile(r'([2-9][0-9]{2}){2}[0-9]{4}')
        cleanedNumber = ''
        for digit in number:
            if digit.isdigit():
                if not (cleanedNumber == '' and digit == '1'):
                    cleanedNumber += digit
        print(cleanedNumber)
        if len(cleanedNumber) != 10 or not pattern.search(cleanedNumber):  # len(cleanedNumber) != 10:
            raise ValueError('Incorrect format')
        return cleanedNumber

    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'