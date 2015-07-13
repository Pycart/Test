#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_states.settings')

from main.models import State, City

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'zip_codes_states.csv')

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    try:
        the_state = State.objects.get(abbreviation=row['state'])
    except Exception, e:
        print e
        print row['state']

    new_city, created = City.objects.get_or_create(name=row['city'], zip_code=row['zip_code'])

    new_city.state = the_state

    try:
        new_city.latitude = float(row['latitude'])
    except ValueError, e:
        print e
        print row['latitude']

    try:
        new_city.longitude = float(row['longitude'])
    except ValueError, e:
        print e
        print row['latitude']
    
    new_city.county = row['county']

    new_city.save()
