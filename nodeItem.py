#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : nodeItem.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-04
#  Last modified: 2014-04-10 13:58:37
# Description   : 
# 

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QPolygonF
from node import *

class NodeItem(Node, QGraphicsItem):
    def __init__(self, index):
        Node.__init__(self, index)
        QGraphicsItem.__init__(self)
        # 绘制时的位置
        self.index_draw = 0

    def center(self):
        return QPointF(NodeItem.ITEM_DX * self.index_draw
                + NodeItem.ITEM_X / 2,
                -NodeItem.ITEM_Y * self.level / 2)

    def boxRect(self):
        return QRectF(NodeItem.ITEM_DX * self.index_draw,
                -NodeItem.ITEM_Y * self.level,
                NodeItem.ITEM_X, NodeItem.ITEM_Y * self.level)

    def boundingRect(self):
        p_right = self
        for i in range(0, self.level):
            if (self.p_next[i] != None):
                if (self.p_next[i].center().x() > p_right.center().x()):
                    p_right = self.p_next[i]
        return QRectF(NodeItem.ITEM_DX * self.index_draw,
                -NodeItem.ITEM_Y * self.level,
                NodeItem.ITEM_DX + p_right.center().x()-self.center().x(),
                NodeItem.ITEM_Y * self.level)

    def paint(self, painter, option, widget):
        boxRect = self.boxRect()
        painter.drawRect(boxRect)
        painter.drawText(boxRect, QtCore.Qt.AlignCenter,
                str(self.index))
        for i in range(0, self.level):
            if (self.p_next[i] != None):
                l = QPointF(self.center().x() + NodeItem.ITEM_X / 2,
                        -NodeItem.ITEM_Y * (i + 0.5))
                r = QPointF(self.p_next[i].center().x()
                        - NodeItem.ITEM_X / 2,
                        -NodeItem.ITEM_Y * (i + 0.5))
                painter.drawLine(l, r)
                painter.drawPolygon(QPolygonF(
                        [r, r + QPointF(-5, 5), r + QPointF(-5, -5), r]), 4)


NodeItem.ITEM_X = 30.0
NodeItem.ITEM_Y = 30.0
NodeItem.ITEM_DX = 40.0

