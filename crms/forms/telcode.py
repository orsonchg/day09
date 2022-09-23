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


class TelCodeForm(BootstrapForm, forms.ModelForm):
	"""国际电话区号ModelForm"""

	class Meta:
		model = models.TelAreaCode
		fields = '__all__'


	def clean_code(self):
		code = self.cleaned_data['code']
		# 在models查找不重复
		exist = models.TelAreaCode.objects.filter(code=code).exclude(id=self.instance.pk).exists()
		if exist:
			raise ValidationError('国际电话区号已存在')
		else:
			return code
