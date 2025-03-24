# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lineFlow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 594)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"selection-color: rgb(255, 255, 255);\n"
"font-family: Arial, sans-serif;\n"
"color: rgb(0, 0, 127);\n"
"alternate-background-color: rgb(85, 170, 255);\n"
"selection-background-color: #007bff")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(330, 90, 601, 451))
        self.frame_4.setStyleSheet("background-color: #ffffff;\n"
"border: 1px solid #007bff;\n"
"border-radius: 8px;\n"
"padding: 2px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.prodDist_tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.prodDist_tableWidget.setGeometry(QtCore.QRect(20, 260, 561, 171))
        self.prodDist_tableWidget.setMaximumSize(QtCore.QSize(561, 171))
        self.prodDist_tableWidget.setStyleSheet("background-color: #ffffff;\n"
"border: 1px solid #007bff;\n"
"border-radius: 4px;\n"
"alternate-background-color: #f9f9f9;\n"
"color: rgb(0, 0, 0);")
        self.prodDist_tableWidget.setObjectName("prodDist_tableWidget")
        self.prodDist_tableWidget.setColumnCount(3)
        self.prodDist_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.prodDist_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.prodDist_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.prodDist_tableWidget.setHorizontalHeaderItem(2, item)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"border: none;")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"border:none;")
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setGeometry(QtCore.QRect(20, 50, 561, 161))
        self.frame_3.setStyleSheet("border: 1px solid #007bff;\n"
"color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(10, 10, 191, 141))
        self.frame.setStyleSheet("border:none;")
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lq_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.lq_label.setFont(font)
        self.lq_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.lq_label.setObjectName("lq_label")
        self.gridLayout_2.addWidget(self.lq_label, 3, 0, 1, 1)
        self.lq_output_label = QtWidgets.QLabel(self.frame)
        self.lq_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.lq_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.lq_output_label.setText("")
        self.lq_output_label.setObjectName("lq_output_label")
        self.gridLayout_2.addWidget(self.lq_output_label, 3, 1, 1, 2)
        self.rho_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.rho_label.setFont(font)
        self.rho_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.rho_label.setObjectName("rho_label")
        self.gridLayout_2.addWidget(self.rho_label, 0, 0, 1, 1)
        self.rho_output_label = QtWidgets.QLabel(self.frame)
        self.rho_output_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #cccccc;")
        self.rho_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.rho_output_label.setText("")
        self.rho_output_label.setObjectName("rho_output_label")
        self.gridLayout_2.addWidget(self.rho_output_label, 0, 1, 1, 2)
        self.po_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.po_label.setFont(font)
        self.po_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.po_label.setObjectName("po_label")
        self.gridLayout_2.addWidget(self.po_label, 1, 0, 1, 1)
        self.ls_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.ls_label.setFont(font)
        self.ls_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.ls_label.setObjectName("ls_label")
        self.gridLayout_2.addWidget(self.ls_label, 2, 0, 1, 1)
        self.po_output_label = QtWidgets.QLabel(self.frame)
        self.po_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.po_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.po_output_label.setText("")
        self.po_output_label.setObjectName("po_output_label")
        self.gridLayout_2.addWidget(self.po_output_label, 1, 1, 1, 2)
        self.ls_output_label = QtWidgets.QLabel(self.frame)
        self.ls_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.ls_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ls_output_label.setText("")
        self.ls_output_label.setObjectName("ls_output_label")
        self.gridLayout_2.addWidget(self.ls_output_label, 2, 1, 1, 2)
        self.frame1 = QtWidgets.QFrame(self.frame_3)
        self.frame1.setGeometry(QtCore.QRect(200, 10, 191, 111))
        self.frame1.setStyleSheet("border:none;")
        self.frame1.setObjectName("frame1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lambda_eff_output_label = QtWidgets.QLabel(self.frame1)
        self.lambda_eff_output_label.setStyleSheet("border: 1px solid #cccccc;\n"
"")
        self.lambda_eff_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.lambda_eff_output_label.setText("")
        self.lambda_eff_output_label.setObjectName("lambda_eff_output_label")
        self.gridLayout_3.addWidget(self.lambda_eff_output_label, 2, 1, 1, 2)
        self.ws_output_label = QtWidgets.QLabel(self.frame1)
        self.ws_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.ws_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.ws_output_label.setText("")
        self.ws_output_label.setObjectName("ws_output_label")
        self.gridLayout_3.addWidget(self.ws_output_label, 0, 1, 1, 2)
        self.wq_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.wq_label.setFont(font)
        self.wq_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.wq_label.setObjectName("wq_label")
        self.gridLayout_3.addWidget(self.wq_label, 1, 0, 1, 1)
        self.ws_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.ws_label.setFont(font)
        self.ws_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.ws_label.setObjectName("ws_label")
        self.gridLayout_3.addWidget(self.ws_label, 0, 0, 1, 1)
        self.lambda_eff_label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.lambda_eff_label.setFont(font)
        self.lambda_eff_label.setStyleSheet("border: 1px solid #007bff;\n"
"")
        self.lambda_eff_label.setObjectName("lambda_eff_label")
        self.gridLayout_3.addWidget(self.lambda_eff_label, 2, 0, 1, 1)
        self.wq_output_label = QtWidgets.QLabel(self.frame1)
        self.wq_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.wq_output_label.setFrameShape(QtWidgets.QFrame.Box)
        self.wq_output_label.setText("")
        self.wq_output_label.setObjectName("wq_output_label")
        self.gridLayout_3.addWidget(self.wq_output_label, 1, 1, 1, 2)
        self.inactive_servers_label = QtWidgets.QLabel(self.frame_3)
        self.inactive_servers_label.setGeometry(QtCore.QRect(400, 60, 51, 25))
        self.inactive_servers_label.setObjectName("inactive_servers_label")
        self.inactive_servers_output_label = QtWidgets.QLabel(self.frame_3)
        self.inactive_servers_output_label.setGeometry(QtCore.QRect(460, 60, 81, 25))
        self.inactive_servers_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.inactive_servers_output_label.setText("")
        self.inactive_servers_output_label.setObjectName("inactive_servers_output_label")
        self.server_rate_label = QtWidgets.QLabel(self.frame_3)
        self.server_rate_label.setGeometry(QtCore.QRect(400, 20, 51, 25))
        self.server_rate_label.setObjectName("server_rate_label")
        self.server_rate_output_label = QtWidgets.QLabel(self.frame_3)
        self.server_rate_output_label.setGeometry(QtCore.QRect(460, 20, 81, 25))
        self.server_rate_output_label.setStyleSheet("border: 1px solid #cccccc;")
        self.server_rate_output_label.setText("")
        self.server_rate_output_label.setObjectName("server_rate_output_label")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 921, 71))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #007bff;\n"
"border-radius:5px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(70, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border:none;\n"
"color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.label_4.setStyleSheet("border:none;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/prefijoNuevo/wind.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.open_reports_pushButton = QtWidgets.QPushButton(self.frame_5)
        self.open_reports_pushButton.setGeometry(QtCore.QRect(800, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setBold(True)
        font.setWeight(75)
        self.open_reports_pushButton.setFont(font)
        self.open_reports_pushButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;\n"
"\n"
"border: none;")
        self.open_reports_pushButton.setObjectName("open_reports_pushButton")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(10, 90, 321, 451))
        self.frame2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid #007bff;\n"
"\n"
"border-radius: 8px;\n"
"padding: 2px;")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.clean_pushButton = QtWidgets.QPushButton(self.frame2)
        self.clean_pushButton.setGeometry(QtCore.QRect(200, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setBold(True)
        font.setWeight(75)
        self.clean_pushButton.setFont(font)
        self.clean_pushButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;\n"
"\n"
"border: none;  \n"
"    ")
        self.clean_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.clean_pushButton.setObjectName("clean_pushButton")
        self.pdf_export_pushButton = QtWidgets.QPushButton(self.frame2)
        self.pdf_export_pushButton.setGeometry(QtCore.QRect(100, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setBold(True)
        font.setWeight(75)
        self.pdf_export_pushButton.setFont(font)
        self.pdf_export_pushButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;\n"
"\n"
"border: none;")
        self.pdf_export_pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pdf_export_pushButton.setObjectName("pdf_export_pushButton")
        self.label_7 = QtWidgets.QLabel(self.frame2)
        self.label_7.setGeometry(QtCore.QRect(30, 190, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"border: none;")
        self.label_7.setObjectName("label_7")
        self.calculate_pushButton = QtWidgets.QPushButton(self.frame2)
        self.calculate_pushButton.setGeometry(QtCore.QRect(20, 400, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setBold(True)
        font.setWeight(75)
        self.calculate_pushButton.setFont(font)
        self.calculate_pushButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;\n"
"\n"
"border: none;")
        self.calculate_pushButton.setObjectName("calculate_pushButton")
        self.frame_6 = QtWidgets.QFrame(self.frame2)
        self.frame_6.setGeometry(QtCore.QRect(30, 130, 251, 51))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.limited_radioButton = QtWidgets.QRadioButton(self.frame_6)
        self.limited_radioButton.setGeometry(QtCore.QRect(140, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.limited_radioButton.setFont(font)
        self.limited_radioButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;\n"
"\n"
"")
        self.limited_radioButton.setObjectName("limited_radioButton")
        self.unlimited_radioButton = QtWidgets.QRadioButton(self.frame_6)
        self.unlimited_radioButton.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.unlimited_radioButton.setFont(font)
        self.unlimited_radioButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;")
        self.unlimited_radioButton.setObjectName("unlimited_radioButton")
        self.widget = QtWidgets.QWidget(self.frame2)
        self.widget.setGeometry(QtCore.QRect(30, 210, 251, 171))
        self.widget.setStyleSheet("border:none;\n"
"color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.units_label = QtWidgets.QLabel(self.widget)
        self.units_label.setStyleSheet("border: 1px solid #007bff;\n"
"color: rgb(0, 0, 0);\n"
"")
        self.units_label.setObjectName("units_label")
        self.gridLayout.addWidget(self.units_label, 2, 0, 1, 1)
        self.lambda_label = QtWidgets.QLabel(self.widget)
        self.lambda_label.setStyleSheet("border: 1px solid #007bff;\n"
"color: rgb(0, 0, 0);")
        self.lambda_label.setObjectName("lambda_label")
        self.gridLayout.addWidget(self.lambda_label, 0, 0, 1, 1)
        self.mu_label = QtWidgets.QLabel(self.widget)
        self.mu_label.setStyleSheet("border: 1px solid #007bff;\n"
"color: rgb(0, 0, 0);")
        self.mu_label.setObjectName("mu_label")
        self.gridLayout.addWidget(self.mu_label, 1, 0, 1, 1)
        self.lambda_input_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lambda_input_lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border: 1px solid #cccccc;")
        self.lambda_input_lineEdit.setObjectName("lambda_input_lineEdit")
        self.gridLayout.addWidget(self.lambda_input_lineEdit, 0, 1, 1, 1)
        self.units_input_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.units_input_lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border: 1px solid #cccccc;")
        self.units_input_lineEdit.setObjectName("units_input_lineEdit")
        self.gridLayout.addWidget(self.units_input_lineEdit, 2, 1, 1, 1)
        self.mu_input_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.mu_input_lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border: 1px solid #cccccc;")
        self.mu_input_lineEdit.setObjectName("mu_input_lineEdit")
        self.gridLayout.addWidget(self.mu_input_lineEdit, 1, 1, 1, 1)
        self.servers_input_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.servers_input_lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"border: 1px solid #cccccc;")
        self.servers_input_lineEdit.setObjectName("servers_input_lineEdit")
        self.gridLayout.addWidget(self.servers_input_lineEdit, 3, 1, 1, 1)
        self.servers_label = QtWidgets.QLabel(self.widget)
        self.servers_label.setStyleSheet("border: 1px solid #007bff;\n"
"color: rgb(0, 0, 0);")
        self.servers_label.setObjectName("servers_label")
        self.gridLayout.addWidget(self.servers_label, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame2)
        self.label.setGeometry(QtCore.QRect(30, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size: 16px;\n"
"border: none;")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame2)
        self.frame_2.setGeometry(QtCore.QRect(30, 40, 251, 81))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.singleServer_radioButton = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.singleServer_radioButton.setFont(font)
        self.singleServer_radioButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;")
        self.singleServer_radioButton.setObjectName("singleServer_radioButton")
        self.gridLayout_4.addWidget(self.singleServer_radioButton, 0, 0, 1, 1)
        self.multiServer_radioButton = QtWidgets.QRadioButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial,sans-serif")
        self.multiServer_radioButton.setFont(font)
        self.multiServer_radioButton.setStyleSheet("background-color: #007bff;\n"
"color: #ffffff;\n"
"border-radius: 4px;")
        self.multiServer_radioButton.setObjectName("multiServer_radioButton")
        self.gridLayout_4.addWidget(self.multiServer_radioButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 23))
        self.menubar.setObjectName("menubar")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openGeneratorWindow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.openGeneratorWindow.setFont(font)
        self.openGeneratorWindow.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.openGeneratorWindow.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.openGeneratorWindow.setObjectName("openGeneratorWindow")
        self.menuHerramientas.addAction(self.openGeneratorWindow)
        self.menubar.addAction(self.menuHerramientas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.prodDist_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "n"))
        item = self.prodDist_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pn"))
        item = self.prodDist_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fn"))
        self.label_6.setText(_translate("MainWindow", "Resultados"))
        self.label_8.setText(_translate("MainWindow", "Tabla de distribucion de probabilidades :"))
        self.lq_label.setText(_translate("MainWindow", "Lq"))
        self.rho_label.setText(_translate("MainWindow", "Rho (ρ)"))
        self.po_label.setText(_translate("MainWindow", "P0"))
        self.ls_label.setText(_translate("MainWindow", "Ls"))
        self.wq_label.setText(_translate("MainWindow", "Wq"))
        self.ws_label.setText(_translate("MainWindow", "Ws"))
        self.lambda_eff_label.setText(_translate("MainWindow", "Lambda eff"))
        self.inactive_servers_label.setText(_translate("MainWindow", "    c̅"))
        self.server_rate_label.setText(_translate("MainWindow", "Rho/c"))
        self.label_5.setText(_translate("MainWindow", "LineFlow"))
        self.open_reports_pushButton.setText(_translate("MainWindow", "Abrir reportes"))
        self.clean_pushButton.setText(_translate("MainWindow", "Limpiar"))
        self.pdf_export_pushButton.setText(_translate("MainWindow", "Exportar"))
        self.label_7.setText(_translate("MainWindow", "Entrada"))
        self.calculate_pushButton.setText(_translate("MainWindow", "Calcular"))
        self.limited_radioButton.setText(_translate("MainWindow", "Con limite"))
        self.unlimited_radioButton.setText(_translate("MainWindow", "Sin limite"))
        self.units_label.setText(_translate("MainWindow", "Unidades (n)"))
        self.lambda_label.setText(_translate("MainWindow", "Lambda (λ)"))
        self.mu_label.setText(_translate("MainWindow", "Mu (μ)"))
        self.servers_label.setText(_translate("MainWindow", "Servidores (c)"))
        self.label.setText(_translate("MainWindow", "Modelo"))
        self.singleServer_radioButton.setText(_translate("MainWindow", "un servidor"))
        self.multiServer_radioButton.setText(_translate("MainWindow", "varios servidores"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Metodo"))
        self.openGeneratorWindow.setText(_translate("MainWindow", "Montecarlo"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
