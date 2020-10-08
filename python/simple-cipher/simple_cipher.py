class Cipher:
    def __init__(self, key=None):
        # Set key if None
        self.key = key if key else 'a' * 100

    def encode(self, text):
        # Extend key if smaller than text
        key = self.key * ((len(text) // len(self.key)) + 1)
        aux = zip(text, key[:len(text)])
        asciiList = [ord(chrKey) + (ord(chrText) - ord('a')) for chrKey, chrText in aux]
        return ''.join([chr(code) if code <= ord('z') else chr(code - 26) for code in asciiList])

    def decode(self, text):
        key = self.key * ((len(text) // len(self.key)) + 1)
        aux = zip(text, key[:len(text)])
        asciiList = [ord(chrKey) - (ord(chrText) - ord('a')) for chrKey, chrText in aux]
        print(asciiList)
        return ''.join([chr(code) if code >= ord('a') else chr(code + 26) for code in asciiList])
