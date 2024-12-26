class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * (self.rim + (self.tire * 2))

# print(Gear(52, 11, 26, 1.5).gear_inches())
# print(Gear(52, 11, 24, 1.25).gear_inches())


class RevealingReferences:
    def __init__(self, data):
        self.wheels = self.wheelify(data)

    def diameters(self):
        for wheel in self.wheels:
            print("wheel diameter:", self.diameter(wheel))

    def diameter(self, wheel):
        return wheel.rim + (wheel.tire * 2)


    class Wheel:
        def __init__(self, rim, tire):
            self.rim = rim
            self.tire = tire

    def wheelify(self, data):
        return [self.Wheel(cell[0], cell[1]) for cell in data]



obj = RevealingReferences([[622, 20], [622, 23], [559, 30], [559, 40]])
obj.diameters()
