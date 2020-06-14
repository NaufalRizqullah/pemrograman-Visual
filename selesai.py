# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selesai.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import QMessageBox


class Ui_selesaiFutsal(object):
    def setupUi(self, selesaiFutsal):
        selesaiFutsal.setObjectName("selesaiFutsal")
        selesaiFutsal.resize(350, 200)
        selesaiFutsal.setStyleSheet("background-color: #55557f;")
        self.splitter = QtWidgets.QSplitter(selesaiFutsal)
        self.splitter.setGeometry(QtCore.QRect(30, 40, 291, 71))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.idInput = QtWidgets.QLineEdit(self.splitter)
        self.idInput.setStyleSheet("background:white;\n"
                                   "border-radius:5px;")
        self.idInput.setObjectName("idInput")
        self.splitter_2 = QtWidgets.QSplitter(selesaiFutsal)
        self.splitter_2.setGeometry(QtCore.QRect(100, 140, 150, 23))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.btnOk = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btnOk.setFont(font)
        self.btnOk.setStyleSheet("background:white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Mintb iOs/036-check.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOk.setIcon(icon)
        self.btnOk.setObjectName("btnOk")

        # Button Ok kalo di klik
        self.btnOk.clicked.connect(self.selesai)
        # Button Ok kalo di klik

        self.btnBatal = QtWidgets.QPushButton(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.btnBatal.setFont(font)
        self.btnBatal.setStyleSheet("background:white;")

        # Button batal kalo di klik
        self.btnBatal.clicked.connect(selesaiFutsal.reject)
        # Button batal kalo di klik

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Mintb iOs/038-cancel.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBatal.setIcon(icon1)
        self.btnBatal.setObjectName("btnBatal")

        self.retranslateUi(selesaiFutsal)
        QtCore.QMetaObject.connectSlotsByName(selesaiFutsal)

    def selesai(self):
        idInput = self.idInput.text()

        conn = pymysql.connect(host="localhost", user="root",
                               password="", db="futsal", port=3306, autocommit=True)
        cur = conn.cursor()
        query = "UPDATE `pesanan` SET `status` = '1' WHERE `pesanan`.`id` = %s"
        data = cur.execute(query, (idInput))

        if (data):
            self.messagebox('Berhasil', 'Pertandingan Telah Selesai!')
        else:
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

    def retranslateUi(self, selesaiFutsal):
        _translate = QtCore.QCoreApplication.translate
        selesaiFutsal.setWindowTitle(_translate("selesaiFutsal", "Dialog"))
        self.label.setText(_translate("selesaiFutsal", "Pertandingan Selesai"))
        self.idInput.setPlaceholderText(_translate(
            "selesaiFutsal", "Masukan ID dari Pertandingan yang telah Selesai"))
        self.btnOk.setText(_translate("selesaiFutsal", "Ok"))
        self.btnBatal.setText(_translate("selesaiFutsal", "Batal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selesaiFutsal = QtWidgets.QDialog()
    ui = Ui_selesaiFutsal()
    ui.setupUi(selesaiFutsal)
    selesaiFutsal.show()
    sys.exit(app.exec_())
