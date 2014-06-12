import os
import csv

from django.conf import settings
from django.core.management.base import NoArgsCommand

from atm.models import Atm


class Command(NoArgsCommand):
    help = """
            Used to load atm data from
            .csv file into databse
            """

    def handle_noargs(self, **options):
        load_database()


def load_database():
    base_path = settings.PROJECT_DIR
    file_name = os.path.join(base_path, 'data/atm-list-india.csv')
    try:
        reader = open(file_name, "rb")
        line_reader = csv.reader(reader, delimiter=",")
        line_reader.next()
        for line in line_reader:
            atm_city = get_digit_or_chars(line[1])
            atm_bank = get_bank_name(get_digit_or_chars(line[2]))
            atm_address = get_digit_or_chars(line[3])

            atm, atm_created = Atm.objects.get_or_create(
                name_of_city=atm_city,
                name_of_bank=atm_bank,
                address=atm_address
            )

    except IOError:
        print "IO Error occured"
    finally:
        if reader in locals():
            reader.close()


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
