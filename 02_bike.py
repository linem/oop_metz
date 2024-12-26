class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.wheel = self.Wheel(rim, tire)

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


print(Gear(52, 11, 26, 1.5).gear_inches())
print(Gear(52, 11, 24, 1.25).gear_inches())
