import phonenumbers
number="+919934256412" #Enter the number here,within double inverted comma.

from phonenumbers import carrier
service_number=phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(service_number, 'en'))

from phonenumbers import geocoder
ch_number=phonenumbers.parse(number, 'CH')
print(geocoder.description_for_number(ch_number, "en"))
