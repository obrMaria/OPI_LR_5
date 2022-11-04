#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == '__main__':
    r = int(input("введите радиус окружности: "))
    x = int(input("введите первую координату точки А:\nx="))
    y = int(input("введите вторую координату точки А:\ny="))

    if (math.sqrt(x*x+y*y)) <= r:
        print("точка А входит в окружность")
        print(f"d={math.sqrt(x*x+y*y)}")
    else:
        print("точка А не входит в окружность")
        print(f"d={math.sqrt(x*x+y*y)}")
