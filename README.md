BANKCENTER
----------

A django powered site to find the details about banks in India.


#### How to Get Started

1. Clone this repo.
2. pip install -r requirements/local.txt
3. Correct settings in bank_center/settings/local.py
4. Create databse, sync db
5. Set enviornment variable 'SECRET_KEY' with django secret key.
6. Run management commands to load data to database.
  `python manage.py load_data`
  `python manage.py load_atm`
  `python manage.py load_zipcode`
