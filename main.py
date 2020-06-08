#!/usr/bin/python3
# -*- coding:utf-8 -*-


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mainWin
import EditWin
import ProductManager

class Signals(QObject):
    CloseEditFormSignal = pyqtSignal()

class EditForm(QtWidgets.QMainWindow):
    def __init__(self, rec_id=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = EditWin.Ui_MainWindow()
        self.ui.setupUi(self)

        self.signals = Signals()
        self.rec_id = rec_id
        
        if rec_id != None:
            product = ProductManager.ProductsManager().GetProductById(rec_id)[0]
            
            self.ui.lineEdit.setText(product[1])
            self.ui.doubleSpinBox.setValue(product[2])
            self.ui.lineEdit_2.setText(product[3])
            self.ui.lineEdit_3.setText(product[4])

        self.ui.btnOk.clicked.connect(self.pressBtnOk)
        self.ui.btnCancel.clicked.connect(self.pressBtnCancel)
        
    def pressBtnOk(self):
        res = False

        name = self.ui.lineEdit.text()
        prace = self.ui.doubleSpinBox.text().replace(',','.')
        url = self.ui.lineEdit_2.text()
        note = self.ui.lineEdit_3.text()

        if self.rec_id == None:
            res = ProductManager.ProductsManager().AddProduct(name,prace,url,note)
        else:
            res = ProductManager.ProductsManager().EditProduct(self.rec_id,name,prace,url,note)
        
        if res:
            self.signals.CloseEditFormSignal.emit()
            self.close()
        else:
            print('Ошибка ввода!')    

    def pressBtnCancel(self):
        self.signals.CloseEditFormSignal.emit()
        self.close()
        
class MainForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = mainWin.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.pressBtnAdd)
        self.ui.btnEdit.clicked.connect(self.pressBtnEdit)
        self.ui.btnDelete.clicked.connect(self.pressBtnDelete)

        self.RefreshTable();

    def AddRowInGrid(self, data):
        grid = self.ui.GridProduct
        rowPosition = grid.rowCount()
        grid.insertRow(rowPosition)
        for i in range(len(data)):
            grid.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(data[i])))

    def RefreshTable(self):
        #Обновляем таблицу с данными
        grid = self.ui.GridProduct
        #grid.clear()
        grid.setRowCount(0)
        grid.setColumnHidden(0,True)

        products = ProductManager.ProductsManager().GetProducts()

        for product in products:
            self.AddRowInGrid(product)
        
    def CloseEditForm(self):
        self.RefreshTable()

    def pressBtnAdd(self):
        self.EditFrm = EditForm()
        self.EditFrm.signals.CloseEditFormSignal.connect(self.CloseEditForm)#Реагируем на закрытие формы редактирования
        self.EditFrm.show()

    def pressBtnEdit(self):
        rowNum = self.ui.GridProduct.currentIndex().row()
        rowId = self.ui.GridProduct.item(rowNum, 0).text()
        self.EditFrm = EditForm(rowId)
        self.EditFrm.signals.CloseEditFormSignal.connect(self.CloseEditForm)#Реагируем на закрытие формы редактирования
        self.EditFrm.show()

    def pressBtnDelete(self):
        rowNum = self.ui.GridProduct.currentIndex().row()
        rowId = self.ui.GridProduct.item(rowNum, 0).text()
        if not ProductManager.ProductsManager().DeleteProduct(rowId):
            print('Ошибка ввода')    
        self.RefreshTable();

if __name__ == '__main__':
    main_app = QApplication(sys.argv)
    mainWindow = MainForm()
    mainWindow.show()
    sys.exit(main_app.exec_())
