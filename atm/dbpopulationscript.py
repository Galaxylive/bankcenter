import csv

from .models import Atm


def get_digit_or_chars(address):
    strn = ""
    for i in address:
        if i.isalpha() or i.isdigit():
            strn += i
    return strn


def get_bank_name(name):
    if name == "HDFC":
        return "HDFC Bank Ltd"
    elif name == "ICICI":
        return "Icici Bank Ltd"
    elif name == "IDBI":
        return "Idbi Bank Ltd"
    elif name == "UCO Bank":
        return "Uco Bank"
    else:
        return name

reader = csv.reader(open("../data/atm-list-india.csv", "rb"), delimiter=",")

for line in reader:
    p = Atm(name_of_city=get_digit_or_chars(line[1]))
    p.save()
    p = Atm(name_of_bank=get_bank_name(get_digit_or_chars(line[2])))
    p.save()
    p = Atm(address=get_digit_or_chars(line[3]))
    p.save()


# today modified the previous xls file and used csv.DictReader, the database in
# its initial form was not customised for dictreading.
