#! D:/Python33/ python
# -*- coding: utf-8 -*-
# Module        : mainWindow.py
# Author        : bss
# Project       : SkipList
# Creation date : 2014-04-03
#  Last modified: 2014-04-10 15:43:52
# Description   :
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QFileDialog, QInputDialog
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from ui_Form import Ui_MainWindow
from skiplist import *
from blockItem import *
from insertThread import *
from deleteThread import *
from searchThread import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.setScene(QGraphicsScene())
        self.skiplist = Skiplist(self.ui.graphicsView.scene())
        self.skiplist.addNode.connect(self.addNode)
        self.skiplist.clear()

# slots
    @pyqtSlot()
    def on_newAction_triggered(self):
        BlockItem.clear()
        self.ui.graphicsView.scene().clear()
        self.skiplist.clear()

    @pyqtSlot()
    def on_openAction_triggered(self):
        BlockItem.clear()
        path = QFileDialog.getOpenFileName(self, '载入数据', '.',
                '文本文档(*.txt)')[0];
        if path:
            self.ui.graphicsView.scene().clear()
            self.skiplist.load(path)

    @pyqtSlot()
    def on_saveAction_triggered(self):
        BlockItem.clear()
        path = QFileDialog.getSaveFileName(self, '保存数据', '.',
                '文本文档(*.txt)')[0];
        if path:
            self.skiplist.save(path)

    @pyqtSlot()
    def on_insertAction_triggered(self):
        BlockItem.clear()
        self.skiplist.updateDrawInfo()
        input_ret = QInputDialog.getInt(self, '插入', '请输入ID',
                self.skiplist.randomIndex())
        if input_ret[1]:
            index = input_ret[0]
            self.lockUI()
            self.thr = InsertThread(self.skiplist.head, index)
            self.thr.opFinished.connect(self.unlockUI)
            self.thr.opFinished.connect(self.skiplist.updateDrawInfo)
            self.thr.addNode.connect(self.addNode)
            self.thr.addBlock.connect(self.addBlock)
            self.thr.opFailed.connect(lambda: QMessageBox.warning(
                    self, '警告', '不允许重复index'))
            self.thr.start()

    @pyqtSlot()
    def on_deleteAction_triggered(self):
        BlockItem.clear()
        self.skiplist.updateDrawInfo()
        input_ret = QInputDialog.getInt(self, '删除', '请输入ID')
        if input_ret[1]:
            index = input_ret[0]
            self.lockUI()
            self.thr = DeleteThread(self.skiplist.head, index)
            self.thr.opFinished.connect(self.unlockUI)
            self.thr.addBlock.connect(self.addBlock)
            self.thr.opFailed.connect(lambda: QMessageBox.warning(
                    self, '警告', '找不到指定index'))
            self.thr.start()


    @pyqtSlot()
    def on_searchAction_triggered(self):
        BlockItem.clear()
        self.skiplist.updateDrawInfo()
        input_ret = QInputDialog.getInt(self, '检索', '请输入ID')
        if input_ret[1]:
            index = input_ret[0]
            self.lockUI()
            self.thr = SearchThread(self.skiplist.head, index)
            self.thr.opFinished.connect(self.unlockUI)
            self.thr.opFinished.connect(self.skiplist.updateDrawInfo)
            self.thr.addBlock.connect(self.addBlock)
            self.thr.opFailed.connect(lambda: QMessageBox.warning(
                    self, '警告', '找不到指定index'))
            self.thr.start()

    @pyqtSlot()
    def on_randomAction_triggered(self):
        BlockItem.clear()
        self.skiplist.updateDrawInfo()
        self.lockUI()
        index = self.skiplist.randomIndex()
        self.thr = InsertThread(self.skiplist.head, index)
        self.thr.opFinished.connect(self.unlockUI)
        self.thr.opFinished.connect(self.skiplist.updateDrawInfo)
        self.thr.addNode.connect(self.addNode)
        self.thr.addBlock.connect(self.addBlock)
        self.thr.opFailed.connect(lambda: QMessageBox.warning(
                self, '警告', 'index生成错误'))
        self.thr.start()

    @pyqtSlot()
    def on_aboutAction_triggered(self):
        info = '跳跃表\n版本 1.0.0\n作者 蚌绍诗 '   \
                'bss10@mails.tsinghua.edu.cn\n\n'   \
                '2014年 数据结构'
        QMessageBox.about(self, '关于', info);

    @pyqtSlot()
    def on_optionAction_triggered(self):
        print('hell')

    @pyqtSlot()
    def on_exitAction_triggered(self):
        exit()

    def lockUI(self):
        self.ui.toolBar.setEnabled(False)

    @pyqtSlot()
    def unlockUI(self):
        self.ui.toolBar.setEnabled(True)
        self.ui.graphicsView.scene().update()

    @pyqtSlot(tuple)
    def addNode(self, nodes):
        self.ui.graphicsView.scene().addItem(nodes[0])

    @pyqtSlot(str, int, int)
    def addBlock(self, blockType, drawIndex, level):
        self.ui.graphicsView.scene().addItem(
                BlockItem(blockType, drawIndex, level))


if __name__ == '__main__':
    import sys
    #QApplication.addLibraryPath('./plugins')
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

