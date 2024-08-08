class Object3D():
    def __init__(self, array=[], pairs=[], char="#") -> None:
        self.array = array
        self.pairs = pairs
        self.char = char

    def __str__(self) -> str:
        return f"Array: {self.array}\nPairs: {self.pairs}\nChar: {self.char}"