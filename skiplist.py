#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : skiplist.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-04
#  Last modified: 2014-04-10 15:57:39
# Description   : 
# 

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
import sys
import os
import math
import time
import random
from nodeItem import *
from blockItem import *

class Skiplist(QObject):
    addNode = pyqtSignal(tuple)

    def __init__(self, scene):
        QObject.__init__(self)
        self.scene = scene
        self.head = None
        self.clear()

    def clear(self):
        Skiplist.MAX_RND = 500
        self.head = NodeItem(-float("Inf"))
        self.addNode.emit((self.head,))
        self.head.level = Node.MAX_LEVEL
        self.head.p_next = [None for i in range(0, Node.MAX_LEVEL)]
        p_end = NodeItem(float("Inf"))
        self.addNode.emit((p_end,))
        p_end.level = Node.MAX_LEVEL
        p_end.p_next = [None for i in range(0, Node.MAX_LEVEL)]
        for i in range(0, Node.MAX_LEVEL):
            self.head.p_next[i] = p_end
        # update ui
        self.updateDrawInfo()

    @pyqtSlot()
    def updateDrawInfo(self):
        p_cur = self.head
        index_draw = 0
        while p_cur is not None:
            p_cur.index_draw = index_draw
            p_cur = p_cur.p_next[0]
            index_draw += 1
        self.scene.update()

    def randomIndex(self):
        BlockItem.clear()
        while True:
            index = random.randint(1, Skiplist.MAX_RND)
            p_cur = self.head.p_next[0]
            isFull = True
            isNew = True
            last_index = 1
            while p_cur.p_next[0] is not None:
                if p_cur.index - last_index > 1:
                    isFull = False
                last_index = p_cur.index
                if p_cur.index == index:
                    isNew = False
                p_cur = p_cur.p_next[0]
            if Skiplist.MAX_RND - last_index > 0:
                isFull = False
            if isNew:
                return index
            if isFull:
                Skiplist.MAX_RND *= 2
                return self.randomIndex()

    def save(self, path):
        fp = open(path, 'w')
        fp.write('SkipList\n')
        p_cur = self.head.p_next[0]
        while p_cur.p_next[0] is not None:
            fp.write(str(p_cur.index))
            fp.write(' ')
            fp.write(str(p_cur.level))
            fp.write('\n')
            p_cur = p_cur.p_next[0]
        fp.close()

    def load(self, path):
        self.clear()
        fp = open(path, 'r')
        if fp.readline() == 'SkipList\n':
            for line in fp.readlines():
                args = line.strip().split(' ')
                self.__insert(int(args[0]), int(args[1]))
                Skiplist.MAX_RND += 1
        fp.close()
        self.updateDrawInfo()

    def __insert(self, index, level):
        p_cur = self.head
        # 查重
        while p_cur is not None:
            if p_cur.index == index:
                return
            p_cur = p_cur.p_next[0]
        # insert
        p_new = NodeItem(index)
        p_new.level = level
        p_new.p_next = [None for i in range(0, level)]
        p_cur = self.head
        for i in range(Node.MAX_LEVEL-1, -1, -1):
            while p_cur.p_next[i].index < index:
                p_cur = p_cur.p_next[i]
            if p_new.level > i:
                p_new.p_next[i] = p_cur.p_next[i]
                p_cur.p_next[i] = p_new
        self.addNode.emit((p_new,))

Skiplist.MAX_RND = 500

