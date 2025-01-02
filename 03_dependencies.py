from functools import cached_property


class Gear:
    def __init__(self, chainring=40, cog=11, wheel=None):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    def gear_inches(self):
        return self.ratio() * self.diameter()

    def diameter(self):
        return self.wheel.diameter()

    def ratio(self):
        return self.chainring / float(self.cog)


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


print(Gear(
    wheel=Wheel(26, 1.5),
    chainring=52,
    cog=11).gear_inches()
      )
print(Gear(
    wheel=Wheel(26, 1.5)).chainring
      )
