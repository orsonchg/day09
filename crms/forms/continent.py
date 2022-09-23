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


class ContinentForm(BootstrapForm, forms.ModelForm):
	"""洲别ModelForm"""

	class Meta:
		model = models.Continent
		fields = '__all__'
		error_messages = {
			'name': {'required': '洲别名称不能为空！'}
		}

	def clean_name(self):
		name = self.cleaned_data['name']
		# 在models查找不重复
		exist = models.Continent.objects.filter(name=name).exclude(id=self.instance.pk).exists()
		if exist:
			raise ValidationError('洲别名称已存在')
		else:
			return name
