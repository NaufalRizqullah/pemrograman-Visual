# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pesan import Ui_Dialog
from pemesanan import Ui_Dialog2
from selesai import Ui_selesaiFutsal
import pymysql

class Ui_home(object):
    def LoadData(self):
        conn = pymysql.connect(host="localhost", user="root",
                               password="", db="futsal", port=3306, autocommit=True)
        cur = conn.cursor()
        query = "SELECT id, nama, lapangan, waktu FROM pesanan WHERE status=0"
        cur.execute(query)
        result = cur.fetchall()
        # print(result)
        self.tableWidget.setRowCount(0)
        # self.tableWidget.setColumnCount(4)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(600, 360)
        home.setStyleSheet("background-color: #55557f;")
        self.centralwidget = QtWidgets.QWidget(home)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnPelaporan_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btnPelaporan_2.setFont(font)
        self.btnPelaporan_2.setStyleSheet("color:white;\n"
"background: #453a7f;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Mintb iOs/021-cursor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPelaporan_2.setIcon(icon)
        self.btnPelaporan_2.setObjectName("btnPelaporan_2")
         # Button pesan kalo di klik
        self.btnPelaporan_2.clicked.connect(self.windowPesan)
        # Button pesan kalo di klik
        self.horizontalLayout_2.addWidget(self.btnPelaporan_2)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setStyleSheet("background-color:white;")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.btnPelaporan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(16)
        self.btnPelaporan.setFont(font)
        self.btnPelaporan.setStyleSheet("color:white;\n"
"background: #453a7f;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Mintb iOs/020-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPelaporan.setIcon(icon1)
        self.btnPelaporan.setObjectName("btnPelaporan")
        self.horizontalLayout_2.addWidget(self.btnPelaporan)
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setStyleSheet("background-color:white;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.btnDPemesanan = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.btnDPemesanan.setFont(font)
        self.btnDPemesanan.setStyleSheet("color:white;\n"
"background: #453a7f;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/Mintb iOs/022-list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDPemesanan.setIcon(icon2)
        self.btnDPemesanan.setObjectName("btnDPemesanan")
        # Button pesan kalo di klik
        self.btnDPemesanan.clicked.connect(self.windowPemesanan)
        # Button pesan kalo di klik
        self.horizontalLayout_2.addWidget(self.btnDPemesanan)
        self.line_3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_3.setStyleSheet("background-color:white;")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.logOut = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.logOut.setFont(font)
        self.logOut.setStyleSheet("background: #fcff21;")
        self.logOut.setObjectName("logOut")
        self.horizontalLayout_2.addWidget(self.logOut)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 59, 581, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(190, 290, 251, 29))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnRefresh = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnRefresh.setFont(font)
        self.btnRefresh.setStyleSheet("background: #aaffff;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/Mintb iOs/014-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon3)
        self.btnRefresh.setObjectName("btnRefresh")
        # test load data pake btnRefresh
        self.btnRefresh.clicked.connect(self.LoadData)
        # test load data pake btnRefresh
        self.horizontalLayout_3.addWidget(self.btnRefresh)
        self.btnSelesai = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.btnSelesai.setFont(font)
        self.btnSelesai.setStyleSheet("background: #55ff00;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/Mintb iOs/036-check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSelesai.setIcon(icon4)
        self.btnSelesai.setObjectName("btnSelesai")
        # btn selesai
        self.btnSelesai.clicked.connect(self.windowSelesai)
        # btn selsai
        self.horizontalLayout_3.addWidget(self.btnSelesai)
        home.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(home)
        self.statusbar.setObjectName("statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)
        # fungsi tombol pindah ke halaman form pemesanan (pesan)
    def windowPesan(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def windowSelesai(self):
        self.selesaiFutsal = QtWidgets.QDialog()
        self.ui = Ui_selesaiFutsal()
        self.ui.setupUi(self.selesaiFutsal)
        self.selesaiFutsal.show()

    def windowPemesanan(self):
        self.Dialog2 = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.Dialog2)
        self.Dialog2.show()

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "MainWindow"))
        self.btnPelaporan_2.setText(_translate("home", "Pesan"))
        self.btnPelaporan.setText(_translate("home", "Laporan"))
        self.btnDPemesanan.setText(_translate("home", "Data Pesanan"))
        self.logOut.setText(_translate("home", "Keluar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("home", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("home", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("home", "Lapangan"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("home", "Waktu"))
        self.btnRefresh.setText(_translate("home", "Refresh"))
        self.btnSelesai.setText(_translate("home", "Selesai"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = QtWidgets.QMainWindow()
    ui = Ui_home()
    ui.setupUi(home)
    home.show()
    sys.exit(app.exec_())

