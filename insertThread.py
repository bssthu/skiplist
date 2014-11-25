#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : insertThread.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-09
#  Last modified: 2014-04-10 13:26:34
# Description   : 
# 

import time
from skiplistThread import *

class InsertThread(SkiplistThread):
    def __init__(self, head, index):
        SkiplistThread.__init__(self, head, index)

    def run(self):
        index = self.index
        BlockItem.clear()
        p_new = NodeItem(index)
        p_cur = self.head
        for i in range(Node.MAX_LEVEL-1, -1, -1):
            if i >= p_new.level-1:
                self.addBlock.emit('route', p_cur.index_draw, i)
                time.sleep(SkiplistThread.DT)
            while p_cur.p_next[i].index < index:
                p_cur = p_cur.p_next[i]
                if i >= p_new.level-1:
                    self.addBlock.emit('route', p_cur.index_draw, i)
                    time.sleep(SkiplistThread.DT)
            if p_new.level > i:
                p_new.p_next[i] = p_cur.p_next[i]
                p_cur.p_next[i] = p_new
        # 不允许重复 index
        if p_new.index == p_new.p_next[0].index:
            p_cur = self.head
            for i in range(Node.MAX_LEVEL-1, -1, -1):
                while p_cur.p_next[i].index < index:
                    p_cur = p_cur.p_next[i]
                if p_new.level > i:
                    # cur.next is new
                    p_cur.p_next[i] = p_new.p_next[i]
            p_new.hide()
            self.opFailed.emit()
        self.addNode.emit((p_new,))
        self.opFinished.emit()
        time.sleep(SkiplistThread.DT)
        self.addBlock.emit('insert', p_new.index_draw, p_new.level - 1)

