# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesan.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 360)
        Dialog.setStyleSheet("background-color: #55557f;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #aaff7f;")

        # Button pesan kalo di klik
        self.pushButton.clicked.connect(self.pesan)
        # Button pesan kalo di klik

        self.pushButton.setObjectName("pushButton")
        self.pembayaran = QtWidgets.QComboBox(Dialog)
        self.pembayaran.setGeometry(QtCore.QRect(70, 260, 461, 41))
        self.pembayaran.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")
        self.pembayaran.setObjectName("pembayaran")
        self.pembayaran.addItem("")
        self.pembayaran.addItem("")
        self.waktu = QtWidgets.QComboBox(Dialog)
        self.waktu.setGeometry(QtCore.QRect(70, 180, 461, 41))
        self.waktu.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")
        self.waktu.setObjectName("waktu")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.waktu.addItem("")
        self.pemesanan = QtWidgets.QComboBox(Dialog)
        self.pemesanan.setGeometry(QtCore.QRect(70, 220, 461, 41))
        self.pemesanan.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")
        self.pemesanan.setObjectName("pemesanan")
        self.pemesanan.addItem("")
        self.pemesanan.addItem("")
        self.nama = QtWidgets.QLineEdit(Dialog)
        self.nama.setGeometry(QtCore.QRect(70, 60, 461, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.nama.setFont(font)
        self.nama.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")
        self.nama.setClearButtonEnabled(False)
        self.nama.setObjectName("nama")
        self.nohp = QtWidgets.QLineEdit(Dialog)
        self.nohp.setGeometry(QtCore.QRect(70, 100, 461, 41))
        font = QtGui.QFont()
        font.setKerning(True)
        self.nohp.setFont(font)
        self.nohp.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")
        self.nohp.setClearButtonEnabled(False)
        self.nohp.setObjectName("nohp")
        self.lapangan = QtWidgets.QComboBox(Dialog)
        self.lapangan.setGeometry(QtCore.QRect(70, 140, 461, 41))
        self.lapangan.setStyleSheet("background-color: white;\n"
"border: 2px solid gray;\n"
"border-radius: 5px;")
        self.lapangan.setObjectName("lapangan")
        self.lapangan.addItem("")
        self.lapangan.addItem("")
        self.lapangan.addItem("")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 91, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kembali = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kembali.setFont(font)
        self.kembali.setStyleSheet("background: #3dfff3;")

         # Button pesan kalo di klik
        self.kembali.clicked.connect(Dialog.reject)
        # Button pesan kalo di klik

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Mintb iOs/009-back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembali.setIcon(icon)
        self.kembali.setObjectName("kembali")
        self.verticalLayout.addWidget(self.kembali)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 10, 191, 32))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def pesan(self):
        nama = self.nama.text()
        hp = self.nohp.text()
        lapangan = str(self.lapangan.currentText())
        waktu = str(self.waktu.currentText())
        pemesanan = str(self.pemesanan.currentText())
        pembayaran = str(self.pembayaran.currentText())
        # print(nama, hp, lapangan, waktu, pemesanan, pembayaran)
        conn = pymysql.connect(host="localhost", user="root",
                               password="", db="futsal", port=3306, autocommit=True)
        cur = conn.cursor()
        query = "INSERT INTO pesanan VALUES (NULL,%s, %s, %s, %s, %s, %s,'0')"
        data = cur.execute(
            query, (nama, waktu, lapangan, hp, pemesanan, pembayaran))
        if(data):
            self.messagebox("Berhasil!", "Data Sudah Ditambahkan!")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Pesan"))
        self.pembayaran.setItemText(0, _translate("Dialog", "Full"))
        self.pembayaran.setItemText(1, _translate("Dialog", "Booking"))
        self.waktu.setItemText(0, _translate("Dialog", "09.00 - 10.00"))
        self.waktu.setItemText(1, _translate("Dialog", "10.00 - 11.00"))
        self.waktu.setItemText(2, _translate("Dialog", "11.00 - 12.00"))
        self.waktu.setItemText(3, _translate("Dialog", "12.00 - 13.00"))
        self.waktu.setItemText(4, _translate("Dialog", "13.00 - 14.00"))
        self.waktu.setItemText(5, _translate("Dialog", "14.00 - 15.00"))
        self.waktu.setItemText(6, _translate("Dialog", "15.00 - 16.00"))
        self.waktu.setItemText(7, _translate("Dialog", "16.00 - 17.00"))
        self.waktu.setItemText(8, _translate("Dialog", "17.00 - 18.00"))
        self.waktu.setItemText(9, _translate("Dialog", "18.00 - 19.00"))
        self.waktu.setItemText(10, _translate("Dialog", "19.00 - 20.00"))
        self.waktu.setItemText(11, _translate("Dialog", "20.00 - 21.00"))
        self.waktu.setItemText(12, _translate("Dialog", "21.00 - 22.00"))
        self.waktu.setItemText(13, _translate("Dialog", "22.00 - 23.00"))
        self.pemesanan.setItemText(0, _translate("Dialog", "Lunas"))
        self.pemesanan.setItemText(1, _translate("Dialog", "Sebagian"))
        self.nama.setPlaceholderText(_translate("Dialog", "Nama Lengkap"))
        self.nohp.setPlaceholderText(_translate("Dialog", "Nomor Handphone"))
        self.lapangan.setItemText(0, _translate("Dialog", "Lapangan 1"))
        self.lapangan.setItemText(1, _translate("Dialog", "Lapangan 2"))
        self.lapangan.setItemText(2, _translate("Dialog", "Lapangan 3"))
        self.kembali.setText(_translate("Dialog", "Kembali"))
        self.label.setText(_translate("Dialog", "Form Pemesanan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

