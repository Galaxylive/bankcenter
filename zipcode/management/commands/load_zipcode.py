import os
import csv

from django.conf import settings
from django.core.management.base import NoArgsCommand

from zipcode.models import Zip_code


class Command(NoArgsCommand):
    help = """
            Used to load zipcodes from
            .csv file into databse
            """

    def handle_noargs(self, **options):
        load_database()


def load_database():
    base_path = settings.PROJECT_DIR
    file_name = os.path.join(base_path, 'data/pincodes_of_India_Database.csv')
    try:
        reader = open(file_name)
        line_reader = csv.reader(reader, delimiter=",")
        line_reader.next()

        for row in line_reader:
            post_office_name = row[0]
            pin_code = get_digits(row[1])
            district_name = row[2]
            city_name = row[3]
            state = row[4]
            latitude = 0
            longitude = 0

            if not post_office_name or not pin_code or not city_name:
                continue

            pin, pin_created = Zip_code.objects.get_or_create(
                post_office_name=post_office_name,
                pin_code=pin_code,
                district_name=district_name,
                city_name=city_name,
                state=state,
                latitude=latitude,
                longitude=longitude
            )

    except IOError:
        print "IO Error occured"
    finally:
        if reader in locals():
            reader.close()


def get_digits(var):
    strn = ""
    for char in var:
        if char.isdigit():
            strn += char
    return strn
