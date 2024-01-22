class User:

    first_name = 'noName'
    last_name = "no surname"

    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name

    def sayName(self):
        print("Мое имя: ", self.first_name)

    def saySurname(self):
        print("Моя фамилия: ", self.last_name)

    def sayFullname(self):
        print("Мое полное имя", self.first_name, self.last_name)
