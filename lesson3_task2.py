from smartphone import Smartphone

Smartphone.catalog = []

phone1 = Smartphone('Samsung', 'A23', '+79635874213')
phone2 = Smartphone('iPhone', '13 Pro', '+79139856472')
phone3 = Smartphone('Xiaomi', '12t Pro', '+79641253985')
phone4 = Smartphone('Redmi', 'Note 12', '+79031478596')
phone5 = Smartphone('OPPO', 'Reno 10', '+79045852369')


for i in range(0, len(Smartphone.catalog)):
    print(Smartphone.catalog[i])