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


class ObscuringReferences:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def diameters(self):
        for wheel in self.data:
            print("wheel diameter:", wheel[0] + (wheel[1] * 2))

obj = ObscuringReferences([[622, 20], [622, 23], [559, 30], [559, 40]])
obj.diameters()
