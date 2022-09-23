#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-22 0022 10:50 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : continent.py 
# @Software: PyCharm

from django.shortcuts import render, redirect, HttpResponse, reverse
from crms.forms.country import CountryForm
from crms import models


# Create your views here.
def country_list(request):
	"""国家列表"""
	country_obj = models.Country.objects.all()
	return render(request, 'crms/country_list.html', {'country_obj': country_obj})


def country_add(request):
	"""国家新增"""
	if request.method == 'POST':
		form = CountryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crms:country_list')
		else:
			return render(request, 'crms/change.html', {'form': form})
	form = CountryForm()
	return render(request, 'crms/change.html', {'form': form})


def country_edit(request, pk):
	"""洲别修改"""
	country_obj = models.Country.objects.filter(id=pk).first()
	if not country_obj:
		return HttpResponse('数据不存在')
	if request.method == 'GET':
		form = CountryForm(instance=country_obj)
		return render(request, 'crms/change.html', {'form': form})
	form = CountryForm(instance=country_obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect('crms:country_list')
	return render(request, 'crms/change.html', {'form': form})

def country_del(request, pk):
	"""洲别删除"""
	origin_url = reverse('crms:country_list')
	if request.method == 'GET':
		return render(request, 'alarm.html', {'cancel': origin_url})
	models.CountryForm.objects.filter(id = pk).delete()
	return redirect('crms:country_list')
