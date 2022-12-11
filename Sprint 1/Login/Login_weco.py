
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

        # Formateo de ventana

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(400, 600)
                MainWindow.setMinimumSize(QtCore.QSize(400, 600))
                MainWindow.setMaximumSize(QtCore.QSize(400, 600))
                MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.389831 rgba(0, 170, 255, 255), stop:1 rgba(0, 0, 131, 255));\n"
                "}")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.US_CT = QtWidgets.QLabel(self.centralwidget)
                self.US_CT.setGeometry(QtCore.QRect(30, 110, 351, 41))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Semibold")
                font.setPointSize(18)
                font.setBold(True)
                font.setWeight(75)
                self.US_CT.setFont(font)
                self.US_CT.setObjectName("US_CT")
                self.Us_label = QtWidgets.QLabel(self.centralwidget)
                self.Us_label.setGeometry(QtCore.QRect(165, 180, 71, 41))
                self.Us_label.setObjectName("Us_label")
                self.Ct_label = QtWidgets.QLabel(self.centralwidget)
                self.Ct_label.setGeometry(QtCore.QRect(130, 270, 141, 51))
                self.Ct_label.setObjectName("Ct_label")
                self.User = QtWidgets.QLineEdit(self.centralwidget)
                self.User.setGeometry(QtCore.QRect(80, 230, 241, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.User.setFont(font)
                self.User.setStyleSheet("QLineEdit {\n"
                " border: 2px solid gray;\n"
                " border-radius: 10px;\n"
                "}")
                self.User.setObjectName("User")
                self.Pass = QtWidgets.QLineEdit(self.centralwidget)
                self.Pass.setGeometry(QtCore.QRect(80, 320, 241, 21))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.Pass.setFont(font)
                self.Pass.setStyleSheet("QLineEdit {\n"
                " border: 2px solid gray;\n"
                " border-radius: 10px;\n"
                "}")
                self.Pass.setEchoMode(QtWidgets.QLineEdit.Password)
                self.Pass.setObjectName("Pass")
                self.salir = QtWidgets.QPushButton(self.centralwidget)
                self.salir.setGeometry(QtCore.QRect(320, 540, 71, 31))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Semibold")
                font.setBold(True)
                font.setWeight(75)
                self.salir.setFont(font)
                self.salir.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.salir.setObjectName("salir")
                self.salir_2 = QtWidgets.QPushButton(self.centralwidget)
                self.salir_2.setGeometry(QtCore.QRect(150, 370, 101, 51))
                font = QtGui.QFont()
                font.setFamily("Segoe UI Semibold")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.salir_2.setFont(font)
                self.salir_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.salir_2.setObjectName("salir_2")
                self.errorlbl = QtWidgets.QLabel(self.centralwidget)
                self.errorlbl.setGeometry(QtCore.QRect(90, 350, 201, 16))
                self.errorlbl.setStyleSheet("color:red;")
                self.errorlbl.setText("")
                self.errorlbl.setObjectName("errorlbl")
                self.Logo = QtWidgets.QLabel(self.centralwidget)
                self.Logo.setGeometry(QtCore.QRect(100, 20, 211, 101))
                self.Logo.setText("")
                self.Logo.setPixmap(QtGui.QPixmap("WeCollect.png"))
                self.Logo.setScaledContents(True)
                self.Logo.setObjectName("Logo")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Funciones y estilos
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.US_CT.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#060606;\">Ingrese su usuario y contraseña:</span></p></body></html>"))
                self.Us_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Usuario:</span></p></body></html>"))
                self.Ct_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Contraseña:</span></p></body></html>"))
                self.salir.setText(_translate("MainWindow", "Salir"))
                self.salir_2.setText(_translate("MainWindow", "Ingresar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())