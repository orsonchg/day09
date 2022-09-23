#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-23 0023 12:34 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : person.py 
# @Software: PyCharm
from django import forms
from persons import models

from tools.bootstrap import BootstrapForm

class PersonForm(BootstrapForm, forms.ModelForm):

	class Meta:
		model = models.Person
		fields = '__all__'
