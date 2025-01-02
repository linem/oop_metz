class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire

    def gear_inches(self):
        """
        Gear object depends on:
        a) the class name of the Wheel class,
        b) the Wheel object contains a diameter method,
        c) the Wheel class requires two arguments rim and tire,
        d) the order of the arguments rim and tire
        """
        return self.ratio() * Wheel(self.rim, self.tire).diameter()

    def ratio(self):
        return self.chainring / float(self.cog)


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


print(Gear(52, 11, 26, 1.5).gear_inches())
