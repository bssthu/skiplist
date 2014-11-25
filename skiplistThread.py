#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : skiplistThread.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-09
#  Last modified: 2014-04-10 13:27:57
# Description   : 
# 

from PyQt5.QtCore import pyqtSignal, QThread
from nodeItem import *
from blockItem import *

class SkiplistThread(QThread):
    opFinished = pyqtSignal()
    opFailed = pyqtSignal()
    addBlock = pyqtSignal(str, int, int)
    addNode = pyqtSignal(tuple)
    
    def __init__(self, head, index):
        QThread.__init__(self)
        self.head = head
        self.index = index

SkiplistThread.DT = 0.1

