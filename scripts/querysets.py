#!/usr/bin/env python
import csv
import os
import sys


sys.path.append("..")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_states.settings')

from django.db.models import Q
from main.models import State, StateCapital, City


# def a_view(request):

# states = State.objects.filter(name__startswith="A", name__endswith="a").order_by('latitude').reverse().values('name', 'latitude')
# sqs = State.objects.filter(Q(name__startswith="A") | Q(name__endswith="a"))
# qs = sqs.exclude(name__contains="Ala").order_by('latitude')
# qs = qs.reverse().values('name', 'latitude')

# states = State.objects.all().values_list('capital', flat=True)

# states2 = State.objects.all().values_list('name')

# states = State.objects.all()

# for state in states:
#     print "---- %s ----" % state.name
#     for city in state.city_set.all():
#         print city

# states_with_htown = State.objects.filter(city__name="Houston")

# for state in states_with_htown:
#     cities = state.city_set.filter(name="Houston")
#     for city in cities:
#         print "%s | %s | %s" % (state, city.name, city.zip_code)

# states_with_atown = State.objects.filter(city__name__startswith="A")

# for state in states_with_atown:
#     cities = state.city_set.filter(name__startswith="A")
#     for city in cities:
#         print "%s | %s | %s" % (state, city.name, city.zip_code)

