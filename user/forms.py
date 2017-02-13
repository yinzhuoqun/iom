#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

# 日志级别等级 ERROR > WARNING > INFO > DEBUG 等几个级别
import logging

logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.WARNING)

from django import forms


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=32, label='用户名称',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_password = forms.CharField(max_length=32, label='设置密码',
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    # user_password_r = forms.CharField(max_length=32, label='确认密码',
    #                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_email = forms.EmailField(max_length=254, label='用户邮箱', widget=forms.TextInput(attrs={'class': 'form-control'}))

    user_phone = forms.CharField(max_length=18, label='用户手机', required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_avatar = forms.ImageField(label='用户头像', required=False)  # ImageField字段需要调用Pillow 库.

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name", "")
        user_name_min = 4
        if user_name and len(user_name) < user_name_min:
            raise forms.ValidationError("用户名长度至少为 %s " % user_name_min)
        if user_name and not user_name.isalnum():
            raise forms.ValidationError("用户名当中不可以有特殊符号")
        return user_name

    def clean_user_password(self):
        user_password = self.cleaned_data.get("user_password", "")

        # user_password_r = self.cleaned_data.get("user_password_r", "")
        # if user_password != user_password_r:
        #     raise forms.ValidationError("确认密码与设置密码不一致")
        user_password_min = 6
        if user_password and len(user_password) < user_password_min:
            raise forms.ValidationError("密码用户名长度至少为 %s" % user_password_min)

        # if user_password_r and len(user_password_r) < 6:
        #     raise forms.ValidationError("确认密码至少要有六位")

        return user_password
