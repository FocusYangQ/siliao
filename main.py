# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import loginUI #ui的名字
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = loginUI.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
