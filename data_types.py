class Object3D():
    def __init__(self, array=[], pairs=[], char="#") -> None:
        self.array = array
        self.pairs = pairs
        self.char = char

        self.axis_dict = {"y": 0, "x": 1, "z": 2}

    def __str__(self) -> str:
        return f"Array: {self.array}\nPairs: {self.pairs}\nChar: {self.char}"
    
    def move(self, axis, amount):
        for point in self.array[0]:
            point[self.axis_dict[axis]] += amount