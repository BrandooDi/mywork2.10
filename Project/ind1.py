# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Произведение первого и последнего элемента
"""


def proizv(*args):
    if args:
        return args[0] * args[-1]
    else:
        return None


if __name__ == "__main__":
    print(proizv())
    print(proizv(0.5, -3, 0, 2.5, 3.2))
