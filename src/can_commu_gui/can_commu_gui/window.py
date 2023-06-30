# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(340, 108)
        MainWindow.setMinimumSize(QtCore.QSize(340, 108))
        MainWindow.setMaximumSize(QtCore.QSize(340, 108))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 321, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setToolTip("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setToolTip("")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setToolTip("")
        self.spinBox.setMaximum(2047)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_2.setToolTip("")
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setToolTip("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_Us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.spinBox.valueChanged['int'].connect(MainWindow.ADD) # type: ignore
        self.comboBox_2.activated['int'].connect(MainWindow.frameType) # type: ignore
        self.comboBox.activated['int'].connect(MainWindow.chSelect) # type: ignore
        self.spinBox_2.valueChanged['int'].connect(MainWindow.DLC) # type: ignore
        self.pushButton.released.connect(MainWindow.Sent) # type: ignore
        self.pushButton.released.connect(self.lineEdit.clear) # type: ignore
        self.lineEdit.textChanged['QString'].connect(MainWindow.DATA) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CAN communication"))
        self.comboBox.setStatusTip(_translate("MainWindow", "Channel select"))
        self.comboBox.setItemText(0, _translate("MainWindow", "0ch"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1ch"))
        self.comboBox_2.setStatusTip(_translate("MainWindow", "FrameType select"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "0:data"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1:rtr"))
        self.label.setText(_translate("MainWindow", "Address"))
        self.spinBox.setStatusTip(_translate("MainWindow", "Address"))
        self.label_2.setText(_translate("MainWindow", "DLC"))
        self.spinBox_2.setStatusTip(_translate("MainWindow", "Data Length Code"))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Message"))
        self.pushButton.setStatusTip(_translate("MainWindow", "Sent"))
        self.pushButton.setText(_translate("MainWindow", "Sent"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Application close"))
        self.actionAbout_Us.setText(_translate("MainWindow", "info"))
        self.actionAbout_Us.setStatusTip(_translate("MainWindow", "Infomation"))
