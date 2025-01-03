from external_gear_module import Gear


class GearWrapper:
    def __init__(self, chainring=None, cog=None, wheel=None):
        self.gear = Gear(chainring, cog, wheel)


class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)


print(GearWrapper(
    wheel=Wheel(26, 1.5),
    chainring=52,
    cog=11).gear.gear_inches()
      )
