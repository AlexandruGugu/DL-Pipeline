# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ClassEditor(object):
    def setupUi(self, ClassEditor):
        ClassEditor.setObjectName("ClassEditor")
        ClassEditor.setWindowModality(QtCore.Qt.WindowModal)
        ClassEditor.resize(800, 599)
        self.centralwidget = QtWidgets.QWidget(ClassEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 1, 1, 1)
        self.txtLog = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.txtLog.setFont(font)
        self.txtLog.setReadOnly(True)
        self.txtLog.setObjectName("txtLog")
        self.gridLayout.addWidget(self.txtLog, 0, 2, 1, 1)
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setObjectName("button")
        self.gridLayout.addWidget(self.button, 1, 0, 1, 3)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 2, 0, 1, 3)
        ClassEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ClassEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ClassEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ClassEditor)
        self.statusbar.setObjectName("statusbar")
        ClassEditor.setStatusBar(self.statusbar)

        self.retranslateUi(ClassEditor)
        QtCore.QMetaObject.connectSlotsByName(ClassEditor)

    def retranslateUi(self, ClassEditor):
        _translate = QtCore.QCoreApplication.translate
        ClassEditor.setWindowTitle(_translate("ClassEditor", "Class Editor"))
        self.txtLog.setToolTip(_translate("ClassEditor", "<html><head/><body><p align=\"justify\">Log</p></body></html>"))
        self.button.setText(_translate("ClassEditor", "Rename"))
        self.button_2.setText(_translate("ClassEditor", "Remove"))

