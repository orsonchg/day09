#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-22 0022 09:28 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : continent.py 
# @Software: PyCharm

from django import forms
from django.core.exceptions import ValidationError
from crms.forms.bootstrap import BootstrapForm
from crms import models


class CountryForm(BootstrapForm, forms.ModelForm):
	"""洲别ModelForm"""

	class Meta:
		model = models.Country
		fields = '__all__'

	def clean_code(self):
		code = self.cleaned_data['code']
		# 在models查找不重复
		exist = models.Continent.objects.filter(name=code).exclude(id=self.instance.pk).exists()
		if exist:
			raise ValidationError('国家代码已存在!')
		else:
			return code
