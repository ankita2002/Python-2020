import phonenumbers
from phonenumbers import carrier 
from phonenumbers import geocoder
from tabulate import tabulate

def scan_number(phone_no):
    number = phonenumbers.parse(phone_no)
    description = geocoder.description_for_number(number,"en")
    supply = carrier.name_for_number(number,"en")
    info = [["Country","Supplier"], [description, supply]]
    data = str(tabulate(info,headers="firstrow", tablefmt="github"))
    return data

if __name__ == "__main__":
    number = input("Enter Number: ")
    print(scan_number(number))