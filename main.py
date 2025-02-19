import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QVBoxLayout, 
    QWidget, 
    QPushButton, 
    QFrame, 
    QGridLayout, 
    QSizePolicy, 
    QSpacerItem, 
    QTableWidgetItem
)
from PyQt5.QtGui import QIntValidator

from lineFlow import Ui_MainWindow
from modules.queueModel import QueueModel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #user input
        self.lambdaValue = self.ui.lambda_input_lineEdit
        self.muValue = self.ui.mu_input_lineEdit
        self.units = self.ui.units_input_lineEdit
        
        ## results
        self.rho = self.ui.rho_output_label
        self.p0 = self.ui.p0_output_label
        self.ls = self.ui.ls_output_label
        self.lq = self.ui.lq_output_label
        self.ws = self.ui.ws_output_label
        self.wq = self.ui.wq_output_label
        self.lambdaEff = self.ui.lambda_eff_output_label

        #buttons
        self.cleanButton = self.ui.clean_pushButton
        self.pdfExportButton = self.ui.pdf_export_pushButton
        self.calculateButton = self.ui.calculate_pushButton
        
        self.setValidators()
        self.init_actions()

    def setValidators(self):
        self.lambdaValue.setValidator(QIntValidator())
        self.muValue.setValidator(QIntValidator())
        self.units.setValidator(QIntValidator())


    # Connect the buttons to the actions
    def init_actions(self):
        self.cleanButton.clicked.connect(self.clean_all)
        self.calculateButton.clicked.connect(self.events)

    # Clean all the fields
    def clean_all(self):
        self.lambdaValue.clear()
        self.muValue.clear()
        self.units.clear()
        self.rho.clear()
        self.p0.clear()
        self.ls.clear()
        self.lq.clear()
        self.ws.clear()
        self.wq.clear()
        self.lambdaEff.clear()

    # Calculate the values
    def events(self):
        if self.lambdaValue.text() and self.muValue.text() and self.units.text():
            calculator = QueueModel(int(self.lambdaValue.text()), int(self.muValue.text()), int(self.units.text()))
            self.rho.setText(str(calculator.getRho()))
            self.p0.setText(str(calculator.getPCero()))
            self.ls.setText(str(calculator.getLs()))
            self.ws.setText(str(calculator.getWs()))         



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())