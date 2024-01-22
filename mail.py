from address import Address

class Mailing:

    def __init__(self, to_address, from_address, cost:int, track:str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return "{} {} {} {}".format(self.track, self.from_address, self.to_address, self.cost)