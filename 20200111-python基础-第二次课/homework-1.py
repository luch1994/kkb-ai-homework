#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luch'

income_str = input('请输入收入记录，用空格隔开：')
pay_str = input('请输入支出记录，用空格隔开：')
income_list = list(map(int, income_str.split(' ')))
pay_list = list(map(int, pay_str.split(' ')))
print('你的收入：', income_list)
print('你的支出：', pay_list)
balance_list = []
pay_len = len(pay_list)
for i in range(len(income_list)):
    if i < pay_len:
        balance_list.append(income_list[i] - pay_list[i])
    else:
        balance_list.append(income_list[i])
print('结余：', balance_list)

balance = 0
for n in balance_list:
    balance += n

print('总结余：', balance)
