# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pemesanan.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql


class Ui_Dialog2(object):
    def LoadData(self):
        conn = pymysql.connect(host="localhost", user="root",
                               password="", db="futsal", port=3306, autocommit=True)
        cur = conn.cursor()
        query = "SELECT nama, waktu, lapangan, no_hp, pemesanan, pembayaran FROM pesanan"
        cur.execute(query)
        result = cur.fetchall()
        # print(result)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(600, 360)
        Dialog2.setStyleSheet("background-color: #55557f;")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 571, 211))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kembali = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.kembali.setFont(font)
        self.kembali.setStyleSheet("background: #3dfff3;\n"
                                   "")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "img/Mintb iOs/009-back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembali.setIcon(icon)
        self.kembali.setObjectName("kembali")
        self.verticalLayout.addWidget(self.kembali)
        self.export_2 = QtWidgets.QPushButton(Dialog2)
        self.export_2.setGeometry(QtCore.QRect(500, 290, 89, 24))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.export_2.setFont(font)
        self.export_2.setStyleSheet("background: #ffaa00;\n"
                                    "")
        self.export_2.setIcon(icon)
        self.export_2.setObjectName("export_2")
        self.btnRefresh = QtWidgets.QPushButton(Dialog2)
        self.btnRefresh.setGeometry(QtCore.QRect(560, 30, 31, 31))
        self.btnRefresh.setStyleSheet("background:white;")
        self.btnRefresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Mintb iOs/012-reload.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon1)
        self.btnRefresh.setObjectName("btnRefresh")
        # test load data pake btnRefresh
        self.btnRefresh.clicked.connect(self.LoadData)
        # test load data pake btnRefresh
        # Button pesan kalo di klik
        self.kembali.clicked.connect(Dialog2.reject)
        # Button pesan kalo di klik

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.label_2.setText(_translate("Dialog2", "Data Pemesanan Futsal"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog2", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog2", "Waktu"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog2", "Lapangan"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog2", "No Handphone"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog2", "Jenis Pemesanan"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog2", "Pembayaran"))
        self.kembali.setText(_translate("Dialog2", "Kembali"))
        self.export_2.setText(_translate("Dialog2", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())
