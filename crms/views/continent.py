#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-22 0022 10:50 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : continent.py 
# @Software: PyCharm

from django.shortcuts import render, redirect, HttpResponse, reverse
from crms.forms.continent import ContinentForm
from crms import models


# Create your views here.
def continent_list(request):
	"""洲别列表"""
	continent_obj = models.Continent.objects.all()
	return render(request, 'crms/continent_list.html', {'continent_obj': continent_obj})


def continent_add(request):
	"""洲别新增"""
	if request.method == 'POST':
		form = ContinentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crms:continent_list')
		else:
			return render(request, 'crms/change.html', {'form': form})
	form = ContinentForm()
	return render(request, 'crms/change.html', {'form': form})


def continent_edit(request, pk):
	"""洲别修改"""
	continent_obj = models.Continent.objects.filter(id=pk).first()
	if not continent_obj:
		return HttpResponse('数据不存在')
	if request.method == 'GET':
		form = ContinentForm(instance=continent_obj)
		return render(request, 'crms/change.html', {'form': form})
	form = ContinentForm(instance=continent_obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect('crms:continent_list')
	return render(request, 'crms/change.html', {'form': form})

def continent_del(request, pk):
	"""洲别删除"""
	origin_url = reverse('crms:continent_list')
	if request.method == 'GET':
		return render(request, 'alarm.html', {'cancel': origin_url})
	models.Continent.objects.filter(id = pk).delete()
	return redirect('crms:continent_list')
