from mailing import Mailing
from address import Address

from_address = Address("768546", "Краснодар", "Ставропольская", "18", "45")

to_address = Address("908765", "Новороссийск", "Ленина", "23", "56")

mail = Mailing(from_address, to_address, 1000, "TRK4567330")

print(
    f"Отправление {mail.track} из "
    f"{mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - "
    f"{mail.from_address.apartment} в "
    f"{mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
