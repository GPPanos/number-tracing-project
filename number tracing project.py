import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("Enter your NO. with +963:")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
printb(phone)
print(time)
print(car)
print(reg)