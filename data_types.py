import math

Y = 0
X = 1
Z = 2

pi = 3.14159265359

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

    def rotate(self, origin, rads):
        x_o = origin[X]
        z_o = 10

        for point in self.array[0]:
            x_i = point[X]
            z_i = point[Z]

            x_from_origin = abs(x_i - x_o)
            z_from_origin = abs(z_i - z_o)

            radius = math.sqrt((x_from_origin)**2 + z_from_origin**2)

            if z_i > z_o and x_i > x_o:
                angle_corrector = math.atan( (z_from_origin) / (x_from_origin) )

            elif z_i > z_o and x_i < x_o:
                angle_corrector = math.atan( (x_from_origin) / (z_from_origin) ) + (.5 * pi)

            elif z_i < z_o and x_i < x_o:
                angle_corrector = math.atan( (z_from_origin) / (x_from_origin) ) + (pi)

            elif z_i < z_o and x_i > x_o:
                angle_corrector = math.atan( (x_from_origin) / (z_from_origin) ) + (1.5 * pi)

            x_f = radius * math.cos(rads+angle_corrector) + x_o
            z_f = radius * math.sin(rads+angle_corrector) + z_o

            point[X] = x_f
            point[Z] = z_f