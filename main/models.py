from django.db import models
from django.db.models import signals
from django.core.mail import send_mail


def send_confirm_email(sender, instance, created, **kwargs):
    send_mail('New Created', 'The new city is %s' % instance.name, 'django.stuff@gmail.com', ['django.stuff@gmail.com'], fail_silently=False)



class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=2, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_city_starts_with(self, letter):
        results = self.city_set.filter(name__startswith="%s" % letter)
        return results

class StateCapital(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    state = models.OneToOneField('main.State', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'State Capital'
        verbose_name_plural = 'State Capitals'

class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey('main.State', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'State Capital'
        verbose_name_plural = 'State Capitals'

signals.post_save.connect(send_confirm_email, sender=City)