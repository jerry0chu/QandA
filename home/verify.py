# -*- coding: utf-8 -*-
from home.models import User
import re


def verify_username(name):
    name_dic = {}
    string = ''
    query = User.objects.filter(username=name).values('username')
    if len(name) < 5:
        string = string + '密码长度不能低于5位'
    elif query:
        string = string + '用户名已存在'
    name_dic['name'] = string
    return name_dic


def verify_phone(phone):
    string = ''
    phone_dic = {}
    p2 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    phonematch = p2.match(phone)
    query = User.objects.filter(mobile=phone).values('mobile')
    if phonematch is None:
        string = string + '手机格式不对'
    elif query:
        string = string + '手机号已存在'
    phone_dic['phone'] = string
    return phone_dic


def verify_pwd(pwd, pwd2):
    pwd_dic = {}
    string = ''
    if len(str(pwd)) < 6:
        string = string + '密码长度小于6位'
    elif pwd != pwd2:
        string = string + '两个密码不一致'
    pwd_dic['pwd'] = string
    return pwd_dic
