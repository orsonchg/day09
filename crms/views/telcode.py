#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-22 0022 10:50 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : continent.py 
# @Software: PyCharm

from django.shortcuts import render, redirect, HttpResponse, reverse
from crms.forms.telcode import TelCodeForm
from crms import models


# Create your views here.
def telcode_list(request):
	"""国际电话区号列表"""
	telcode_obj = models.TelAreaCode.objects.all()
	return render(request, 'crms/telcode_list.html', {'telcode_obj': telcode_obj})


def telcode_add(request):
	"""国际电话区号新增"""
	if request.method == 'POST':
		form = TelCodeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('crms:telcode_list')
		else:
			return render(request, 'crms/change.html', {'form': form})
	form = TelCodeForm()
	return render(request, 'crms/change.html', {'form': form})


def telcode_edit(request, pk):
	"""国际电话区号修改"""
	continent_obj = models.TelAreaCode.objects.filter(id=pk).first()
	if not continent_obj:
		return HttpResponse('数据不存在')
	if request.method == 'GET':
		form = TelCodeForm(instance=continent_obj)
		return render(request, 'crms/change.html', {'form': form})
	form = TelCodeForm(instance=continent_obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect('crms:telcode_list')
	return render(request, 'crms/change.html', {'form': form})

def telcode_del(request, pk):
	"""国际电话区号删除"""
	origin_url = reverse('crms:telcode_list')
	if request.method == 'GET':
		return render(request, 'alarm.html', {'cancel': origin_url})
	models.TelAreaCode.objects.filter(id = pk).delete()
	return redirect('crms:telcode_list')
