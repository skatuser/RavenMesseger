import sys
# Импортируем наш интерфейс из файла
from mes_window import *
from PyQt5 import QtCore, QtGui, QtWidgets
from mes_lib import Client

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, contacts, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Наполняем список контактов
        for contact in contacts:
            self.ui.ContactsList.addItem(contact)
        #Связываем кнопку Login с подключением к серверу
        self.ui.LoginButton.clicked.connect(self.login)
        #Связываем двойной щелчок по элементу списка с открытием чата
        self.ui.ContactsList.itemDoubleClicked.connect(self.open_chat)
        #Связы        
        self.ui.SendButton.clicked.connect(self.send_message)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку                  
    def login(self):
        name = self.ui.LoginInput.toPlainText()
        self.client = Client(name = name)
        self.client.confirm_connection()
    def open_chat(self):
        pass
    def send_message(self):
        pass

contact_list = ['John', 'Steve', 'Richard']

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin(contacts =  contact_list)
    myapp.show()
    sys.exit(app.exec_())