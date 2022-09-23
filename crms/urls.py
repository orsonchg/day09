#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-17 0017 08:54 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from crms.views import continent, country, telcode

app_name = 'crms'
urlpatterns = [
    path('continent/list/', continent.continent_list, name='continent_list'),
    path('continent/add/', continent.continent_add, name='continent_add'),
    path('continent/edit/<int:pk>/', continent.continent_edit, name='continent_edit'),
    path('continent/del/<int:pk>/', continent.continent_del, name='continent_del'),

    path('country/list/', country.country_list, name='country_list'),
    path('country/add/', country.country_add, name='country_add'),
    path('country/edit/<int:pk>/', country.country_edit, name='country_edit'),
    path('country/del/<int:pk>/', country.country_del, name='country_del'),

    path('telcode/list/', telcode.telcode_list, name='telcode_list'),
    path('telcode/add/', telcode.telcode_add, name='telcode_add'),
    path('telcode/edit/<int:pk>/', telcode.telcode_edit, name='telcode_edit'),
    path('telcode/del/<int:pk>/', telcode.telcode_del, name='telcode_del'),

]