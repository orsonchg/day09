#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-17 0017 08:54 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from persons import views

app_name = 'persons'
urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('add/', views.person_add, name='person_add'),
    path('edit/<int:pk>/', views.person_edit, name='person_edit'),
    path('del/<int:pk>/', views.person_del, name='person_del'),


]