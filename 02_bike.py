class Gear:
    def __init__(self, chainring, cog):
        self.chainring = chainring
        self.cog = cog

    def ratio(self):
        return self.chainring / float(self.cog)

print(Gear(52, 11).ratio())
print(Gear(30, 27).ratio())
