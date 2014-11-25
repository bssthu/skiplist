#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : node.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-04
#  Last modified: 2014-04-10 11:32:01
# Description   : 
# 

import random

class Node:
    def __init__(self, index):
        self.index = index
        r = random.randint(1, pow(2, Node.MAX_LEVEL-1))
        # 层数
        self.level = 1
        while r % 2 == 0:
            r = r / 2
            self.level += 1
        self.p_next = [None for i in range(0, self.level)]

Node.MAX_LEVEL = 6

