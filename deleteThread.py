#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : deleteThread.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-10
#  Last modified: 2014-04-10 13:31:32
# Description   : 
# 

import time
from skiplistThread import *

class DeleteThread(SkiplistThread):
    def __init__(self, head, index):
        SkiplistThread.__init__(self, head, index)

    def run(self):
        index = self.index
        BlockItem.clear()
        p_cur = self.head
        p_del = None
        for i in range(Node.MAX_LEVEL-1, -1, -1):
            if p_del is None:
                self.addBlock.emit('route', p_cur.index_draw, i)
                time.sleep(SkiplistThread.DT)
            # 分别处理每一级
            while p_cur.p_next[i].index <= index:
                if p_del is None:
                    self.addBlock.emit('route', p_cur.index_draw, i)
                    time.sleep(SkiplistThread.DT)
                if index == p_cur.p_next[i].index:
                    if p_del is None:
                        self.addBlock.emit(
                                'delete', p_cur.p_next[i].index_draw, i)
                        time.sleep(SkiplistThread.DT)
                        p_del = p_cur.p_next[i]
                    p_cur.p_next[i] = p_cur.p_next[i].p_next[i]
                    break
                p_cur = p_cur.p_next[i]
                if p_del is None:
                    self.addBlock.emit('route', p_cur.index_draw, i)
                    time.sleep(SkiplistThread.DT)
        if p_del is not None:
            p_del.hide()
        else:
            self.opFailed.emit()
        self.opFinished.emit()

