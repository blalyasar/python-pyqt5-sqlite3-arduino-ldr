# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hakkinda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_hakkinda(object):
    def setupUi(self, hakkinda):
        hakkinda.setObjectName("hakkinda")
        hakkinda.resize(634, 297)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dht11_700p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hakkinda.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(hakkinda)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-330, 530, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 10, 591, 171))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 205, 591, 28))
        self.pushButton.setObjectName("pushButton")
        hakkinda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hakkinda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 21))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        hakkinda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hakkinda)
        self.statusbar.setObjectName("statusbar")
        hakkinda.setStatusBar(self.statusbar)
        self.actionGiri = QtWidgets.QAction(hakkinda)
        self.actionGiri.setObjectName("actionGiri")
        self.actionKay_t_Ol = QtWidgets.QAction(hakkinda)
        self.actionKay_t_Ol.setObjectName("actionKay_t_Ol")
        self.action_k = QtWidgets.QAction(hakkinda)
        self.action_k.setObjectName("action_k")
        self.menuProgram.addAction(self.actionGiri)
        self.menuProgram.addAction(self.actionKay_t_Ol)
        self.menuProgram.addAction(self.action_k)
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(hakkinda)
        QtCore.QMetaObject.connectSlotsByName(hakkinda)

    def retranslateUi(self, hakkinda):
        _translate = QtCore.QCoreApplication.translate
        hakkinda.setWindowTitle(_translate("hakkinda", "Hakkında"))
        self.textBrowser_2.setHtml(_translate("hakkinda", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">BİLAL YAŞAR 1612710001 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">1.ÖĞRETİM </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> GÖRSEL PROGRAMLAMA DERSİ</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\"> DÖNEM ÖDEVİ</span><span style=\" font-size:8pt;\"><br /><br /><br /></span></p></body></html>"))
        self.pushButton.setText(_translate("hakkinda", "Giriş Sayfası İçin Tıklayın"))
        self.menuProgram.setTitle(_translate("hakkinda", "Program"))
        self.actionGiri.setText(_translate("hakkinda", "Giriş"))
        self.actionKay_t_Ol.setText(_translate("hakkinda", "Kayıt Ol"))
        self.action_k.setText(_translate("hakkinda", "Çıkış"))

