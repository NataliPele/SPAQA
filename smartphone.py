class Smartphone:
 
    def __init__(self, brand_, model_, number_):
        self.brand = brand_
        self.model = model_
        self.number = number_
        Smartphone.catalog.append(self)

    def __str__(self):
        return "{} {} {}".format(self.brand, self.model, self.number)
