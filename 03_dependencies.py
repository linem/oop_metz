class Gear:
    def __init__(self, chainring, cog):
        self.chainring = chainring
        self.cog = cog

    def gear_inches(self, diameter):
        return self.ratio() * diameter

    def ratio(self):
        return self.chainring / float(self.cog)


class Wheel:
    def __init__(self, rim, tire, chainring, cog):
        self.rim = rim
        self.tire = tire
        self.gear = Gear(chainring, cog)

    def diameter(self):
        return self.rim + (self.tire * 2)

    def gear_inches(self):
        return self.gear.gear_inches(self.diameter())


print(Wheel(
    rim=26,
    tire=1.5,
    chainring=52,
    cog=11).gear_inches()
      )
