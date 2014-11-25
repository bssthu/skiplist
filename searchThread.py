#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : searchThread.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-10
#  Last modified: 2014-04-10 13:43:42
# Description   : 
# 

import time
from skiplistThread import *

class SearchThread(SkiplistThread):
    def __init__(self, head, index):
        SkiplistThread.__init__(self, head, index)

    def run(self):
        index = self.index
        BlockItem.clear()
        p_cur = self.head
        for i in range(Node.MAX_LEVEL-1, -1, -1):
            self.addBlock.emit('route', p_cur.index_draw, i)
            time.sleep(SkiplistThread.DT)
            while p_cur.p_next[i].index <= index:
                self.addBlock.emit('route', p_cur.index_draw, i)
                time.sleep(SkiplistThread.DT)
                p_cur = p_cur.p_next[i]
                if index == p_cur.index:
                    self.addBlock.emit('search', p_cur.index_draw, i)
                    time.sleep(SkiplistThread.DT)
                    self.opFinished.emit()
                    return
                self.addBlock.emit('route', p_cur.index_draw, i)
                time.sleep(SkiplistThread.DT)
        self.opFailed.emit()
        self.opFinished.emit()

