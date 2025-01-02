from math import pi


class Gear:
    def __init__(self, chainring, cog, wheel=None):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)

    def circumference(self):
        return self.diameter() * pi


wheel = Wheel(26, 1.5)
print(wheel.circumference())
print(Gear(52, 11, wheel).gear_inches())
print(Gear(52, 11, wheel).ratio())
