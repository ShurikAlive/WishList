#!/usr/bin/python3
# -*- coding:utf-8 -*-

import DBManager

class ProductsManager(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProductsManager, cls).__new__(cls)
        return cls.instance

    def GetProducts(self):
        res = DBManager.DBManager().ExecuteSQLScript('SELECT * FROM wishlistDB.PRODUCTS')
        return res

    def GetProductById(self, productId):
        res = DBManager.DBManager().ExecuteSQLScript('SELECT * FROM wishlistDB.PRODUCTS WHERE ID = ' + str(productId) + ';')
        return res

    def AddProduct(self, name, prace, url, note):
        DBManager.DBManager().ExecuteSQL('INSERT wishlistDB.PRODUCTS(NAME, PRACE, URL, NOTE) VALUES '+
                                               ' (\'' + name + '\', ' + str(prace) + ', \'' + url + '\', \'' + note + '\' );')
        return True

    def EditProduct(self, productId, name, prace, url, note):
        DBManager.DBManager().ExecuteSQL('UPDATE wishlistDB.PRODUCTS SET ' + 
            ' NAME = \'' + name + '\', ' +
            ' PRACE = ' + str(prace) + ', ' +
            ' URL = \'' + url + '\', ' +
            ' NOTE = \'' + note + '\' ' +
            ' WHERE ID = ' + str(productId) + ';')
        return True

    def DeleteProduct(self, productId):
        DBManager.DBManager().ExecuteSQL('DELETE FROM wishlistDB.PRODUCTS WHERE ID = ' + str(productId) + ';')
        return True

