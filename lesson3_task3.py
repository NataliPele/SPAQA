from address import Address
from mail import Mailing

new_to_address = Address('698574', 'Moscow', 'Pushkina', '158', '89')
new_from_address = Address('895327', 'Irkutsk', 'Lenina', '63', '14')
new_mail = Mailing(new_to_address, new_from_address, '850', '65896321477')

print(f'Отправление  {new_mail.track} из {new_mail.from_address.index}, {new_mail.from_address.city}, {new_mail.from_address.street}, {new_mail.from_address.house} - {new_mail.from_address.apartment} '
      f'в {new_mail.to_address.index}, {new_mail.to_address.city}, {new_mail.to_address.street}, {new_mail.to_address.house} - {new_mail.to_address.apartment}. Cтоимость: {new_mail.cost} рублей')

