from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from main.models import State
import json

def first_view(request, starts_with):

	states = State.objects.all()

	text_string = ''

	for state in states:
		cities = state.city_set.filter(name__startswith="%s" % starts_with)
		for city in cities:
			 text_string += "State: %s , City: %s <br>" % (state, city.name)

	return HttpResponse(text_string)


class GetPost(View):

    def get(self, request, *args, **kwargs):
		city_state_string = """
			<form action="/get_post/" method="POST">

			State:
			<br>
			<input type="text" name="state" >

			<br>

			City:
			<br>
			<input type="text" name="city" >

			<br>
			<br>

			<input type="submit" value="Submit">

			</form>
		"""

		response = city_state_string

		return HttpResponse(response)

    def post(self, request, *args, **kwargs):
		get_state= request.POST.get('state', None)
		get_city= request.POST.get('city', None)

		city_state_string = ""

		states = State.objects.filter(name__startswith="%s" % get_state)

		for state in states:
			cities = state.city_set.filter(name__startswith="%s" % get_city)
			for city in cities:
				city_state_string+= "<b>%s</b> %s <br>" % (state, city.name)

		city_state_string+= """
			<form action="/get_post/" method="POST">

			State:
			<br>
			<input type="text" name="state" >

			<br>

			City:
			<br>
			<input type="text" name="city" >

			<br>
			<br>

			<input type="submit" value="Submit">

			</form>
		"""

		response = city_state_string

		return HttpResponse(response)


@csrf_exempt
def get_post(request):

	if request.method == 'GET':

		city_state_string = """
			<form action="/get_post/" method="POST">

			State:
			<br>
			<input type="text" name="state" >

			<br>

			City:
			<br>
			<input type="text" name="city" >

			<br>
			<br>

			<input type="submit" value="Submit">

			</form>
		"""

		response = city_state_string

		return HttpResponse(response)


	elif request.method == 'POST':

		get_state= request.POST.get('state', None)
		get_city= request.POST.get('city', None)

		city_state_string = ""

		states = State.objects.filter(name__startswith="%s" % get_state)

		for state in states:
			cities = state.city_set.filter(name__startswith="%s" % get_city)
			for city in cities:
				city_state_string+= "<b>%s</b> %s <br>" % (state, city.name)

		city_state_string+= """
			<form action="/get_post/" method="POST">

			State:
			<br>
			<input type="text" name="state" >

			<br>

			City:
			<br>
			<input type="text" name="city" >

			<br>
			<br>

			<input type="submit" value="Submit">

			</form>
		"""

		response = city_state_string

		return HttpResponse(response)
