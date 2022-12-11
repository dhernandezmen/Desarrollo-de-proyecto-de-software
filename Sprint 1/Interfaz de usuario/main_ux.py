

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    #Diseño de la interfaz

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QWidget#centralwidget{background-color: rgb(50, 50, 50);}\n"
    "\n"
    "\n"
    "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(300, 40, 201, 101))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap("WeCollect.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.Bienvenida = QtWidgets.QLabel(self.centralwidget)
        self.Bienvenida.setGeometry(QtCore.QRect(110, 160, 571, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Bienvenida.setFont(font)
        self.Bienvenida.setObjectName("Bienvenida")
        self.Ev = QtWidgets.QLabel(self.centralwidget)
        self.Ev.setGeometry(QtCore.QRect(110, 360, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.Ev.setFont(font)
        self.Ev.setObjectName("Ev")
        self.EV1 = QtWidgets.QPushButton(self.centralwidget)
        self.EV1.setGeometry(QtCore.QRect(160, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.EV1.setFont(font)
        self.EV1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EV1.setObjectName("EV1")
        self.EV2 = QtWidgets.QPushButton(self.centralwidget)
        self.EV2.setGeometry(QtCore.QRect(290, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.EV2.setFont(font)
        self.EV2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EV2.setObjectName("EV2")
        self.torta = QtWidgets.QPushButton(self.centralwidget)
        self.torta.setGeometry(QtCore.QRect(420, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.torta.setFont(font)
        self.torta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.torta.setObjectName("torta")
        self.kpi = QtWidgets.QPushButton(self.centralwidget)
        self.kpi.setGeometry(QtCore.QRect(550, 440, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.kpi.setFont(font)
        self.kpi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kpi.setObjectName("kpi")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(714, 532, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#Estilos y Funcionalidades

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Bienvenida.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#ffffff;\">Bienvenido<br/>Al sistema de evaluacion de desempeño de<br/>We Collect</span></p></body></html>"))
        self.Ev.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Seleccione que quiere evaluar:</span></p></body></html>"))
        self.EV1.setText(_translate("MainWindow", "Desempeño anual"))
        self.EV2.setText(_translate("MainWindow", "Desempeño diario"))
        self.torta.setText(_translate("MainWindow", "Contactados"))
        self.kpi.setText(_translate("MainWindow", "KPIs"))
        self.pushButton.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())