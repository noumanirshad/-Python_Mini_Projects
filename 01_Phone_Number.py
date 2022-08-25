import phonenumbers
from phonenumbers import timezone, geocoder, carrier,country_mobile_token
class PhoneNumber():
    number = input("Enter the numbe with +92: ")
    def phonedetail(self):
        phone = phonenumbers.parse(self.number)
        time = timezone.time_zones_for_number(phone)
        car = carrier.name_for_number(phone, "en")
        geo = geocoder.description_for_number(phone, "en")
        print(time)
        print(phone)
        print(f"\nNetwork Name of this Number is:\n\t '{car}'")
        print(f"Country Name of phone number is:\n\t '{geo}'")

cls = PhoneNumber()
cls.phonedetail()  