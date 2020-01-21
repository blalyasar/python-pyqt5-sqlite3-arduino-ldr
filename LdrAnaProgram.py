# -*- coding: utf-8 -*-
import sys
from time import *
import serial   
import sqlite3    

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore 

from girissayfasi import * 
from kayitol import * 
from LdrAnaPencere import *  
from hakkinda import *


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_anapencere()
ui.setupUi(MainWindow)


app1=QtWidgets.QApplication(sys.argv)
MainWindow1=QtWidgets.QMainWindow()
ui1= Ui_girispenceresi()
ui1.setupUi(MainWindow1)


app2=QtWidgets.QApplication(sys.argv)
MainWindow2=QtWidgets.QMainWindow()
ui2= Ui_kayitoll()
ui2.setupUi(MainWindow2)


app3=QtWidgets.QApplication(sys.argv)
MainWindow3=QtWidgets.QMainWindow()
ui3= Ui_hakkinda()
ui3.setupUi(MainWindow3)
MainWindow3.show() 


conn3=sqlite3.connect('LdrAnaPencere.db') 
curs3=conn3.cursor() 
curs3.execute("CREATE TABLE IF NOT EXISTS LdrTablo (id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	saat	TEXT NOT NULL,	Led1	TEXT)")
conn3.commit()


conn2=sqlite3.connect('giris.db') 
curs2=conn2.cursor() 
curs2.execute("CREATE TABLE IF NOT EXISTS giris (id2 INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,	username	TEXT NOT NULL UNIQUE,	passwoord	TEXT NOT NULL, email TEXT, adsoyad TEXT)")
conn2.commit()


def girisiac():

    MainWindow2.close()
    MainWindow3.close()
    MainWindow1.show()    
def kayitiac():
    MainWindow.close()
    MainWindow1.close()

    MainWindow3.close()
    MainWindow2.show()
    
def hakkindaac():
    MainWindow.show()
    MainWindow1.close()
    MainWindow2.close()
    MainWindow3.show()


def kayitol():
    
    ad=ui2.adsoyad.text()
    kullanici=ui2.kullaniciadi.text()
    sifre1=ui2.sifre.text()
    sifre2=ui2.sifretekrar.text()
    mail=ui2.email.text()

    
    if sifre1==sifre2:
        curs2.execute('INSERT INTO giris (username, passwoord, email, adsoyad) VALUES ( ?, ?, ?, ?)', (kullanici,sifre1,mail,ad) )
        conn2.commit()
        ui2.statusbar.showMessage(" "*5 + " Kayıt gerçekleştirildi.", 1500)
        ui2.adsoyad.clear()
        ui2.kullaniciadi.clear()
        ui2.sifre.clear()
        ui2.sifretekrar.clear()
        ui2.email.clear()
    else:
        ui2.statusbar.showMessage(" "*5 + " Kayıt gerçekleştirilemedi. Şifre alanları aynı değil. ", 1500)

        
def giris():

    global username
    username=ui1.lineEdit_2.text()
    passwoord=ui1.lineEdit.text()
 
    curs2.execute("SELECT * FROM giris WHERE username='%s' and passwoord='%s'" %(username,passwoord))
    conn2.commit()
    
    if(len(curs2.fetchall())>0): 
        ui.statusbar.showMessage(" "*3 + " Giriş yapıldı", 1500) 
        MainWindow1.close()
        MainWindow.show()

    else:
        ui1.statusbar.showMessage(" "*3 + " Giriş yapılamadı.  Hatalı kullanıcı adı veya şifre", 1500)  
        
        
def sifre_goster():

    if ui1.checkBox.isChecked():
        ui1.lineEdit.setEchoMode(QLineEdit.Normal)    
    else:
        ui1.lineEdit.setEchoMode(QLineEdit.Password)

def zaman_yaz():
    
    global zaman
    zaman = ctime()
    ui.label_8.setText(zaman[10:19])
    global saat
    saat=zaman[10:19]


timer0 = QtCore.QTimer()
timer0.start(1000)
timer0.timeout.connect(zaman_yaz)

def port_ac():
    
    port = str(ui.port.currentText())
    baud = str(ui.baudrate.currentText())
    global ser
    ser = serial.Serial(port, baudrate=baud, timeout=0)

    if ser.is_open:
        ui.statusbar.showMessage(" "*1 + " Port açıldı...", 1500)
    
        global timer1    
        timer1 = QtCore.QTimer()
        timer1.start(1000)
        timer1.timeout.connect(sensoroku)
    
    else:
        ui.statusbar.showMessage(" "*1 + " Port açılamadı !!!", 1500)
          
def port_kapat():
    
    if ser.is_open:
        
        ser.close()
        timer1.stop()
        print("Port kapatıldı...")       
        ui.label_15.setText("")
        ui.label_16.setText("")
        ui.label_17.setText("")
        ui.label_18.setText("")


        ui.progressBar_2.setValue(1)
        ui.progressBar_3.setValue(1)
        ui.progressBar_4.setValue(1)
        ui.progressBar_5.setValue(1)

        ui.statusbar.showMessage(" "*1 + " Port kapatıldı...", 1500)
def sensoroku():    

    data = ser.read(5)
    print(data)
    
    veri = str(data)
    print(" Ortamın Işık Değeri: ", veri[2:5])
    deger = float(veri[2:5])
    
    ui.label_15.setText(veri[2:5])

    if deger>0 and deger<150:
        ui.progressBar_2.setValue(0)
        ui.progressBar_3.setValue(0)
        ui.progressBar_4.setValue(0)
        ui.progressBar_5.setValue(0)    
    
    if deger>150 and deger<255:
        ui.progressBar_2.setValue(100)
        ui.progressBar_3.setValue(0)
        ui.progressBar_4.setValue(0)
        ui.progressBar_5.setValue(0)
        
    elif deger > 256 and deger<512:
        ui.progressBar_2.setValue(100)
        ui.progressBar_3.setValue(100)
        ui.progressBar_4.setValue(0)
        ui.progressBar_5.setValue(0)

    elif deger>513 and deger<767:
        ui.progressBar_2.setValue(100)
        ui.progressBar_3.setValue(100)
        ui.progressBar_4.setValue(100)
        ui.progressBar_5.setValue(0)

    elif deger>767 and deger<1023:
        ui.progressBar_2.setValue(100)
        ui.progressBar_3.setValue(100)
        ui.progressBar_4.setValue(100)
        ui.progressBar_5.setValue(100)

    curs3.execute('INSERT INTO LdrTablo (Led1, saat ) VALUES (?,?)', (deger, saat))
    conn3.commit()
    listele()
    
def listele():

    sorgu = "SELECT * FROM LdrTablo"
    curs3.execute(sorgu)
    
   
    for row, columnvalues in enumerate(curs3):

        for column, value in enumerate(columnvalues):

            ui.tablWdht11_2.setItem(row, column, QTableWidgetItem(str(value))) #bu satıra dikkat!
        
def cikis():

    try:
        port_kapat()
    except (NameError):  
        sys.exit(app.exec_())
    finally:
        sys.exit(app.exec_())
    
def kapat():
    MainWindow.close()
    MainWindow1.close()
    MainWindow2.close()
    MainWindow3.close()



ui.portac.clicked.connect(port_ac)
ui.portkapat.clicked.connect(port_kapat)
ui.pb_cikis.clicked.connect(cikis)
ui1.pushButton.clicked.connect(giris)
ui1.checkBox.clicked.connect(sifre_goster)
ui1.pushButton_2.clicked.connect(kayitiac)
ui2.giris.clicked.connect(girisiac)
ui2.kayitol.clicked.connect(kayitol)
ui.actionHakk_nda.triggered.connect(hakkindaac)
ui1.actionGiri.triggered.connect(girisiac)
ui1.actionHakk_nda.triggered.connect(hakkindaac)
ui1.actionKay_t_Ol.triggered.connect(kayitiac)
ui2.actionGiri_2.triggered.connect(girisiac)
ui2.actionHakk_nda_2.triggered.connect(hakkindaac)
ui3.actionGiri.triggered.connect(girisiac)
ui3.actionKay_t_Ol.triggered.connect(kayitiac)
ui.action_k.triggered.connect(kapat)
ui1.action_k.triggered.connect(kapat)
ui2.action_cikisk.triggered.connect(kapat)
ui3.action_k.triggered.connect(kapat)
ui3.pushButton.clicked.connect(girisiac)

sys.exit(app.exec_())
