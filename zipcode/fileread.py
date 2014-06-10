from zipcode.models import Zip_code
file = open("pincodes_of_India_Database.csv", "r")
text = file.read().split("\n")


def get_digits(var):
    strn = ""
    for char in var:
        if char.isdigit():
            strn += var
    return strn

for line in text:
    words = line.splilt(",")
    p = Zip_code(
        post_office_name=words[1],
        pin_code=get_digits(words[2]),
        district_name=words[3],
        city_name=words[4],
        state=words[5]
    )
    p.save()
