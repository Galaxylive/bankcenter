BANKCENTER
------------------

A django powered site to find the details about banks in India.


How to Get Started
~~~~~~~~~~~~~~~~~~~

1. Clone this repo.
2. pip install -r requirements/local.txt
3. Correct settings in bank_center/settings/local.py
4. Create databse, sync db
5. Set enviornment variable 'SECRET_KEY' with django secret key.
6. Run management command "load_data". (It will load data from csv files in data directory to database)
        -
