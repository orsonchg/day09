#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-23 0023 15:45 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : forms.py 
# @Software: PyCharm

from django import forms
from django.core.exceptions import ValidationError
from products import models
from tools.bootstrap import BootstrapForm


class CategoryForm(BootstrapForm, forms.ModelForm):
	class Meta:
		model = models.Category
		fields = '__all__'

	def clean_category(self):
		category = self.cleaned_data['category']
		# 在models查找不重复
		exist = models.Category.objects.filter(category=category).exclude(id=self.instance.pk).exists()
		if exist:
			raise ValidationError('产品分类已存在!')
		else:
			return category


class ProductForm(BootstrapForm, forms.ModelForm):
	class Meta:
		model = models.Products
		fields = '__all__'
