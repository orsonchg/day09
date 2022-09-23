#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-17 0017 08:54 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'app01'
urlpatterns = [
    path('', views.index, name='index'),
    path('alarm/', views.alarm, name='alarm'),

]