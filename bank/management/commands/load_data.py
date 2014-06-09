from django.core.management.base import NoArgsCommand
from bank.models import Location,Bank,Branch
import csv

class Command(NoArgsCommand):
    help="""
            Used to load data from
            .csv file into databse
            """
    def handle_noargs(self,**options):
        #fill_database()
        load_database()

def load_database():
    file1='/home/ashik/venvs/bankcenter/bankcenter/data/bank-info.csv'
    file2='/home/ashik/venvs/bankcenter/bankcenter/data/bank-info-2.csv'

    # file1='/home/agiliq/recipehq/bank_center/data/bank-info.csv'
    # file2='/home/agiliq/recipehq/bank_center/bank-info-2.csv'
    fill_database(file1)
    fill_database(file2)

def fill_database(file_name):
    try:
        #bank_reader=open('/home/akshar/bank_center/data/bank-info-2.csv')
        bank_reader=open(file_name)
        line_reader=csv.reader(bank_reader)
        line_reader.next() #We don't want to read the first row, since entries in first row contains description about the corresponding column.
        for row in line_reader:
            branch_bank_name=encode_decode(row[0]).title()
            if branch_bank_name=='':
                break
            branch_ifsc_code=encode_decode(row[1])
            branch_micr_code=encode_decode(row[2])
            branch_micr_code=branch_micr_code.replace(' ','')
            if not len(branch_micr_code)==11:
                branch_micr_code=None
            try:
                int(branch_micr_code)
            except (ValueError,TypeError):
                branch_micr_code=None
            branch_branch_name=encode_decode(row[3]).title()
            branch_address=encode_decode(row[4]).title()
            branch_contact=encode_decode(row[5]).title()
            branch_city=encode_decode(row[6]).title()
            branch_district=encode_decode(row[7]).title()
            branch_state=encode_decode(row[8]).title()
            branch_location,location_created=Location.objects.get_or_create(city=branch_city,district=branch_district,state=branch_state)
            branch_bank,bank_created=Bank.objects.get_or_create(bank_name=branch_bank_name)
            branch,branch_created=Branch.objects.get_or_create(branch_name=branch_branch_name,ifsc=branch_ifsc_code,micr=branch_micr_code,address=branch_address,contact=branch_contact,bank=branch_bank,location=branch_location)

    except IOError:
        print "IO Error occured"
    finally:
        if bank_reader in locals():
            bank_reader.close()

def encode_decode(value):
    value=value.strip()
    value=value.decode('utf-8')
    value=value.encode('ascii','ignore')
    return value

