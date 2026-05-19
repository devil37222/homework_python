from address import address
from Mailing import mailing
address_from = address("899678", "Moscow", "pervomayskaya", "15", "3")
address_to = address("678123", "Saint-Petersburg", "Nevsky", "14", "5")

mailing = mailing(to_address = address_to, from_address = address_from, track = "RU123524356", cost=550)
print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street} "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street} "
      f"{mailing.to_address.house} - {mailing.to_address.apartment} "
)