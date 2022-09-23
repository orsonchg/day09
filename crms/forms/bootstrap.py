#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time : 2022-9-22 0022 09:27 
# @Author: Orsonz
# @Email: orsonz@163.com
# @File : bootstrap.py 
# @Software: PyCharm

class BootstrapForm(object):
    bootstrap_class_exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.bootstrap_class_exclude:
                continue
            old_class = field.widget.attrs.get('class', "")
            field.widget.attrs['class'] = '{} form-control'.format(old_class)
            field.widget.attrs['placeholder'] = '请输入%s' % (field.label,)