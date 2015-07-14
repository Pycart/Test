from django.contrib import admin
from main.models import State, StateCapital, City

class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name', 'population')
	search_fields = ('name', )

class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'county')
	search_fields = ('name', )

class CityInline(admin.TabularInline):
    model = City

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation')
	search_fields = ('name', )
	inlines = [CityInline]



admin.site.register(City, CityAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(State, StateAdmin)