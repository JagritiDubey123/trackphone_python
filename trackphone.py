import phonenumbers
from  phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+919919474871")
phone_number2 = phonenumbers.parse("+917007220804")
phone_number3 = phonenumbers.parse("+919125569843")
phone_number4 = phonenumbers.parse("+918700413467")
phone_number5 = phonenumbers.parse("+233207026823")
print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));
print(geocoder.description_for_number(phone_number4,"en"));
print(geocoder.description_for_number(phone_number5,"en"));