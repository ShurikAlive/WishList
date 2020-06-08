# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python_proj\hello_world_pyqt\mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GridProduct = QtWidgets.QTableWidget(self.centralwidget)
        self.GridProduct.setGeometry(QtCore.QRect(0, 40, 801, 511))
        self.GridProduct.setAutoFillBackground(False)
        self.GridProduct.setObjectName("GridProduct")
        self.GridProduct.setColumnCount(5)
        self.GridProduct.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.GridProduct.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.GridProduct.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.GridProduct.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.GridProduct.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.GridProduct.setHorizontalHeaderItem(4, item)
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(10, 0, 93, 28))
        self.btnAdd.setObjectName("btnAdd")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(120, 0, 93, 28))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setGeometry(QtCore.QRect(230, 0, 93, 28))
        self.btnDelete.setObjectName("btnDelete")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.GridProduct.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.GridProduct.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Наименование"))
        item = self.GridProduct.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.GridProduct.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Ссылка"))
        item = self.GridProduct.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Примечание"))
        self.btnAdd.setText(_translate("MainWindow", "Добавить"))
        self.btnEdit.setText(_translate("MainWindow", "Изменить"))
        self.btnDelete.setText(_translate("MainWindow", "Удалить"))
