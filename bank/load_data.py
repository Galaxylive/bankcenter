# import csv
from models import Location


def load_location():
    try:
        location_reader = open('../data/bank-info.csv')
        for row in location_reader:
            print row[6:]
    except IOError:
        print "IO Error occurred"
    finally:
        if 'location' in locals():
            Location.close()

load_location()
