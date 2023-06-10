# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(484, 393)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rightButton = QtWidgets.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(410, 220, 51, 51))
        self.rightButton.setObjectName("rightButton")
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(350, 280, 51, 51))
        self.downButton.setObjectName("downButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(350, 220, 51, 51))
        self.stopButton.setObjectName("stopButton")
        self.forwardButton = QtWidgets.QPushButton(self.centralwidget)
        self.forwardButton.setGeometry(QtCore.QRect(350, 160, 51, 51))
        self.forwardButton.setObjectName("forwardButton")
        self.leftButton = QtWidgets.QPushButton(self.centralwidget)
        self.leftButton.setGeometry(QtCore.QRect(290, 220, 51, 51))
        self.leftButton.setObjectName("leftButton")
        self.lTurnButton = QtWidgets.QPushButton(self.centralwidget)
        self.lTurnButton.setGeometry(QtCore.QRect(290, 160, 51, 51))
        self.lTurnButton.setObjectName("lTurnButton")
        self.rTurnButton = QtWidgets.QPushButton(self.centralwidget)
        self.rTurnButton.setGeometry(QtCore.QRect(410, 160, 51, 51))
        self.rTurnButton.setObjectName("rTurnButton")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 484, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.downButton.clicked.connect(mainWindow.clickedBack) # type: ignore
        self.leftButton.clicked.connect(mainWindow.clickedLeft) # type: ignore
        self.lTurnButton.clicked.connect(mainWindow.clickedLTurn) # type: ignore
        self.rightButton.clicked.connect(mainWindow.clickedRight) # type: ignore
        self.rTurnButton.clicked.connect(mainWindow.clickedRTurn) # type: ignore
        self.stopButton.clicked.connect(mainWindow.clickedStop) # type: ignore
        self.forwardButton.clicked.connect(mainWindow.clickedForward) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "mainWindow"))
        self.rightButton.setText(_translate("mainWindow", "Right"))
        self.downButton.setText(_translate("mainWindow", "Down"))
        self.stopButton.setText(_translate("mainWindow", "Stop"))
        self.forwardButton.setText(_translate("mainWindow", "Forward"))
        self.leftButton.setText(_translate("mainWindow", "Left"))
        self.lTurnButton.setText(_translate("mainWindow", "L Turn"))
        self.rTurnButton.setText(_translate("mainWindow", "R Turn"))
