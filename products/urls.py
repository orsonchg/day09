#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-17 0017 08:54 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : urls.py 
# @Software: PyCharm

from django.urls import path
from products import views

app_name = 'products'
urlpatterns = [
     path('category/', views.category_list, name='category_list'),
     path('category/add/', views.category_add, name='category_add'),
     path('category/edit/<int:pk>/', views.category_edit, name='category_edit'),
     path('category/del/<int:pk>/', views.category_del, name='category_del'),


]