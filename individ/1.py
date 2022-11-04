#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите номер месяца: "))

    if n == 1:
        print("январь")
    elif n == 2:
        print("ферваль")
    elif n == 3:
        print("март")
    elif n == 4:
        print("апрель")
    elif n == 5:
        print("май")
    elif n == 6:
        print("июнь")
    elif n == 7:
        print("июль")
    elif n == 8:
        print("август")
    elif n == 9:
        print("сертябрь")
    elif n == 10:
        print("октябрь")
    elif n == 11:
        print("ноябрь")
    elif n == 12:
        print("декабрь")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)