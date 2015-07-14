#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_states.settings")

from main.models import State, City

states = State.objects.all()


csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	
    try:
        state_obj = State.objects.get(abbreviation=row['state'])
    except:
        print row['state']

    new_city, created = City.objects.get_or_create(name=row['city'], state=state_obj)
    new_city.county = row['county']
    new_city.latitude = row['latitude']
    new_city.longitude = row['longitude']

    try:
        new_city.save()
    except Exception, e:
        print e
        print new_city.county
        print new_city.latitude
        print new_city.longitude

# csv_file.close()
