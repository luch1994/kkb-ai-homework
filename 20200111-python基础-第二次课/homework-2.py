#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luch'

balance = 0

while True:
    s = input('''
    查询余额请按：1
    存款请按：2
    取款请按：3
    退出请按其他任意键
    请输入您需要的操作
    ''')
    print('--------------------')
    if s == '1':
        print('您的余额为：%s' % balance)
        print('--------------------')
    elif s == '2':
        money = input('请输入你要存入的金额：')
        if money.isdigit():
            money = float(money)
            balance += money
            print('您成功存入：%s，当前余额：%s' % (money, balance))
        else:
            print('输入的不是数字！')
        print('--------------------')
    elif s == '3':
        money = input('请输入你要取款的金额：')
        if money.isdigit():
            money = float(money)
            if money > balance:
                print('您的余额不足')
            else:
                balance -= money
                print('您成功取走：%s，当前余额：%s' % (money, balance))
        else:
            print('输入的不是数字！')
        print('--------------------')
    else:
        print('欢迎您下次光临，再见~')
        break