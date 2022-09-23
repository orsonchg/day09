from django.db import models

from django_countries.fields import CountryField

# Create your models here.

class Person(models.Model):
	name = models.CharField(verbose_name='姓名', max_length=30)
	country = CountryField(verbose_name='国家', null=True, blank=True)

	def __str__(self):
		return self.name