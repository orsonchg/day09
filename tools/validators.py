#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-23 0023 15:12 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : validators.py 
# @Software: PyCharm

from django.core.exceptions import ValidationError

import os

def validate_file_size(value):
	"""验证上传文件大小"""
	filesize = value.size
	if filesize > 2097152:
		raise ValidationError('最大上传文件大小不能超过2MB')
	else:
		return value


def validate_image_file_extension(value):
	"""验证上传图片的格式"""
	ext = os.path.splitext(value.name)[1]   # [0] 代表返回 path + filename 路径+文件名
	valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
	if not ext.lower() in valid_extensions:
		raise ValidationError('图片格式只能为 jpg, jpeg, png, gif')


def valide_document_file_extension(value):
	"""验证上传文件格式"""
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png', 'gif','xlsx','xls']
	if not ext.lower() in valid_extensions:
		raise ValidationError('文件格式只能为 pdf, doc, docx, xls, xlsx, jpg, jpeg, png, gif')