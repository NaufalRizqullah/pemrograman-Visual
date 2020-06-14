# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
from home import Ui_home


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(575, 360)
        login.setStyleSheet("background-color: gray;\n"
                            "border-radius:20px;")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar = QtWidgets.QLabel(self.centralwidget)
        self.gambar.setGeometry(QtCore.QRect(200, 10, 171, 171))
        self.gambar.setMaximumSize(QtCore.QSize(200, 200))
        self.gambar.setText("")
        self.gambar.setPixmap(QtGui.QPixmap("img/bola.png"))
        self.gambar.setScaledContents(True)
        self.gambar.setAlignment(QtCore.Qt.AlignCenter)
        self.gambar.setWordWrap(False)
        self.gambar.setObjectName("gambar")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 190, 251, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: white;\n"
                                    "border: 2px solid gray;\n"
                                    "border-radius: 5px;")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 280, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 25px;\n"
                                      "background: #73AD21;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        # Button login kalo di klik
        self.pushButton.clicked.connect(self.login)
        # Button login kalo di klik

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 230, 251, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: white;\n"
                                      "border: 2px solid gray;\n"
                                      "border-radius: 5px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    # fungsi login
    def login(self):
        username = self.lineEdit.text()  # ambil text yang dari username yg diinputkan
        password = self.lineEdit_2.text()
        # print(username)
        # print(password)
        conn = pymysql.connect(host="localhost", user="root",
                               password="", db="futsal", port=3306, autocommit=True)
        cur = conn.cursor()  # cursor berfungsi untuk mengkatifkan databasenya
        query = "SELECT * FROM admin WHERE username=%s AND password=%s"
        data = cur.execute(query, (username, password))

        if (len(cur.fetchall()) > 0):
            # kalo login berhasil maka akan pindah ke halaman home
            self.messagebox("Berhasil Login", "Anda Telah Berhasil Login!")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_home()
            self.ui.setupUi(self.window)
            self.window.show()
            login.hide()

        else:
            # kalo login gagal maka akan memunculkan popup
            self.warning(
                "Login Gagal", "Harap Masukkan Username dan Password yang benar")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setIcon(QMessageBox.Information)
        mess.exec_()

    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setIcon(QMessageBox.Warning)
        mess.exec_()

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("login", "Username"))
        self.pushButton.setText(_translate("login", "Login"))
        self.lineEdit_2.setPlaceholderText(_translate("login", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
