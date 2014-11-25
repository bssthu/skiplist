#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : blockItem.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-09
#  Last modified: 2014-04-10 13:27:00
# Description   : 
# 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsWidget
from nodeItem import *

class BlockItem(QGraphicsWidget):
    addToScene = pyqtSignal()

    def __init__(self, blockType, drawIndex, level):
        QGraphicsWidget.__init__(self)
        self.blockType = BlockItem.Types.index(blockType)
        self.index_draw = drawIndex
        self.level = level
        self.setZValue(-1.0)
        BlockItem.items.append(self)

    def boundingRect(self):
        return QRectF(NodeItem.ITEM_DX * self.index_draw,
                -NodeItem.ITEM_Y * (self.level + 1),
                NodeItem.ITEM_X, NodeItem.ITEM_Y)

    def paint(self, painter, option, widget):
        rect = self.boundingRect().adjusted(
                BlockItem.ITEM_DX, BlockItem.ITEM_DY,
                -BlockItem.ITEM_DX, -BlockItem.ITEM_DY)
        painter.fillRect(rect, BlockItem.Color[self.blockType])

    def clear():
        for item in BlockItem.items:
            item.hide()
        BlockItem.items = []


BlockItem.items = []
BlockItem.Types = ('route', 'search', 'delete', 'insert')
BlockItem.Color = (QColor(0, 200, 0), QColor(255, 200, 0),
        QColor(200, 0, 0), QColor(0, 150, 250))

BlockItem.ITEM_DX = 5.0
BlockItem.ITEM_DY = 5.0

