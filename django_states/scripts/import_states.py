#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_states.settings")

from main.models import State, StateCapital

states = State.objects.all()


csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	
    new_state, created = State.objects.get_or_create(name = row['state'])
    new_state.abbreviation = row['abbrev']
    new_state.save()

    new_capital, created = StateCapital.objects.get_or_create(name = row['capital'])
    new_capital.state = new_state
    new_capital.latitude = row['latitude']
    new_capital.longitude = row['longitude']
    new_capital.population = row['population']

    new_capital.save()

# csv_file.close()
