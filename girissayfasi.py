# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'girissayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_girispenceresi(object):
    def setupUi(self, girispenceresi):
        girispenceresi.setObjectName("girispenceresi")
        girispenceresi.resize(447, 239)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dht11_700p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        girispenceresi.setWindowIcon(icon)
        girispenceresi.setStyleSheet("QMainWindow{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 162, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QLineEdit{\n"
"background-color:rgb(170, 0, 255)\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(209, 190, 255);\n"
"border:none;\n"
"color:rgb(0, 170, 0)\n"
"}")
        self.centralwidget = QtWidgets.QWidget(girispenceresi)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 55, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 35, 31, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 90, 51, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 30, 151, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 103, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 160, 147, 20))
        self.checkBox.setObjectName("checkBox")
        girispenceresi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(girispenceresi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 21))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        girispenceresi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(girispenceresi)
        self.statusbar.setObjectName("statusbar")
        girispenceresi.setStatusBar(self.statusbar)
        self.actionGiri = QtWidgets.QAction(girispenceresi)
        self.actionGiri.setObjectName("actionGiri")
        self.actionKay_t_Ol = QtWidgets.QAction(girispenceresi)
        self.actionKay_t_Ol.setObjectName("actionKay_t_Ol")
        self.actionHakk_nda = QtWidgets.QAction(girispenceresi)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.action_k = QtWidgets.QAction(girispenceresi)
        self.action_k.setObjectName("action_k")
        self.menuProgram.addAction(self.actionKay_t_Ol)
        self.menuProgram.addAction(self.actionHakk_nda)
        self.menuProgram.addAction(self.action_k)
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(girispenceresi)
        QtCore.QMetaObject.connectSlotsByName(girispenceresi)

    def retranslateUi(self, girispenceresi):
        _translate = QtCore.QCoreApplication.translate
        girispenceresi.setWindowTitle(_translate("girispenceresi", "Giriş"))
        self.pushButton.setText(_translate("girispenceresi", "Giriş"))
        self.label_3.setText(_translate("girispenceresi", "ID:"))
        self.label_4.setText(_translate("girispenceresi", "Şifre:"))
        self.pushButton_2.setText(_translate("girispenceresi", "Kayıt Ol"))
        self.checkBox.setText(_translate("girispenceresi", "Şifreyi Göster"))
        self.menuProgram.setTitle(_translate("girispenceresi", "Program"))
        self.actionGiri.setText(_translate("girispenceresi", "Giriş"))
        self.actionKay_t_Ol.setText(_translate("girispenceresi", "Kayıt Ol"))
        self.actionHakk_nda.setText(_translate("girispenceresi", "Hakkında"))
        self.action_k.setText(_translate("girispenceresi", "Çıkış"))

