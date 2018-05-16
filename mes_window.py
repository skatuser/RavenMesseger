# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mes_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ContactsList = QtWidgets.QListWidget(self.centralwidget)
        self.ContactsList.setGeometry(QtCore.QRect(10, 30, 201, 551))
        self.ContactsList.setObjectName("ContactsList")
        self.ChatWindow = QtWidgets.QTextBrowser(self.centralwidget)
        self.ChatWindow.setGeometry(QtCore.QRect(240, 60, 541, 321))
        self.ChatWindow.setObjectName("ChatWindow")
        self.MessageInput = QtWidgets.QTextEdit(self.centralwidget)
        self.MessageInput.setGeometry(QtCore.QRect(240, 390, 541, 121))
        self.MessageInput.setObjectName("MessageInput")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(240, 520, 541, 61))
        self.SendButton.setObjectName("SendButton")
        self.LoginInput = QtWidgets.QTextEdit(self.centralwidget)
        self.LoginInput.setGeometry(QtCore.QRect(240, 10, 361, 41))
        self.LoginInput.setObjectName("LoginInput")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(610, 10, 171, 41))
        self.LoginButton.setObjectName("LoginButton")
        self.ContactsLabel = QtWidgets.QLabel(self.centralwidget)
        self.ContactsLabel.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.ContactsLabel.setObjectName("ContactsLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SendButton.setText(_translate("MainWindow", "Send"))
        self.LoginButton.setText(_translate("MainWindow", "Log in"))
        self.ContactsLabel.setText(_translate("MainWindow", "Список контактов"))

