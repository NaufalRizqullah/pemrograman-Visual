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
        login.setStyleSheet("background-color: #55557f;\n"
"border-radius:20px;")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.gambar = QtWidgets.QLabel(self.centralwidget)
        self.gambar.setGeometry(QtCore.QRect(50, 60, 101, 101))
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
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-radius: 25px;\n"
"background: #73AD21;\n"
"")
        self.pushButton.setObjectName("pushButton")
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 100, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 120, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)
        # Button login kalo di klik
        self.pushButton.clicked.connect(self.login)
        # Button login kalo di klik

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
        self.pushButton.setText(_translate("login", "LOGIN"))
        self.lineEdit_2.setPlaceholderText(_translate("login", "Password"))
        self.label.setText(_translate("login", "APLIKASI"))
        self.label_2.setText(_translate("login", "PEMESANAN LAPANGAN FUTSAL"))
        self.label_3.setText(_translate("login", "[APLF]"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())

