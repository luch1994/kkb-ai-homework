#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 同时打乱 x,y，保证数据和标签的对应关系

import random

def shuffle(x, y):
    # your code here
    l = [i for i in range(len(x))]
    random.shuffle(l)
    x = [x[i] for i in l]
    y = [y[i] for i in l]
    return x, y


def main():
    x = ['快递太慢了！', '不好吃', '特别难吃', '要齁死我了', '很划算', '下次还来', '味道很不错！', '香']
    y = ['差评', '差评', '差评', '差评', '好评', '好评', '好评', '好评']
    x, y = shuffle(x, y)

    # print result for certify
    for i, j in zip(x, y):
        print(i, ':', j)


if __name__ == '__main__':
    main()
