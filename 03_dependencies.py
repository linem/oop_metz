class Gear:
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def gear_inches(self):
        """
        Now Gear object only depends on:
        b) a 'duck' object with a diameter method,
        """
        return self.ratio() * self.wheel.diameter()

    def ratio(self):
        return self.chainring / float(self.cog)


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


print(Gear(52, 11, Wheel(26, 1.5)).gear_inches())
