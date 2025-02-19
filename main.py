import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
)
from PyQt5.QtGui import QIntValidator, QIcon
from lineFlow import Ui_MainWindow
from modules.queueModel import QueueModel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("LineFlow | Calculadora de modelos de lineas de espera")

        #user input
        self.lambdaValue = self.ui.lambda_input_lineEdit
        self.muValue = self.ui.mu_input_lineEdit
        self.units = self.ui.units_input_lineEdit
        
        ## results
        self.rho = self.ui.rho_output_label
        self.po = self.ui.po_output_label
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
        self.pdfExportButton.clicked.connect(self.pdf_export)

    # Clean all the fields
    def clean_all(self):
        self.lambdaValue.clear()
        self.muValue.clear()
        self.units.clear()
        self.rho.clear()
        self.po.clear()
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
            self.po.setText(str(calculator.getPo()))
            self.ls.setText(str(calculator.getLs()))
            self.lq.setText(str(calculator.getLq()))
            self.ws.setText(str(calculator.getWs()))         
            self.wq.setText(str(calculator.getWq()))
            self.lambdaEff.setText(str(calculator.getLambdaEff()))


    def pdf_export(self):
        
        c = canvas.Canvas(f"reporte.pdf", pagesize=letter)         
        c.drawString(100, 750, "Resultados de la Calculadora de Líneas de Espera")
        c.drawString(100, 750, "")
        c.drawString(100, 750, "")
        c.drawString(100, 730, f"Lambda (λ): {self.lambdaValue.text()}")
        c.drawString(100, 710, f"Mu (μ): {self.muValue.text()}")
        c.drawString(100, 690, f"Rho (ρ): {self.rho.text()}")
        c.drawString(100, 670, f"Po: {self.po.text()}")
        c.drawString(100, 650, f"Ls: {self.ls.text()}")
        c.drawString(100, 630, f"Lq: {self.lq.text()}")
        c.drawString(100, 610, f"Ws: {self.ws.text()}")
        c.drawString(100, 590, f"Wq: {self.wq.text()}")
        c.drawString(100, 570, f"Lambda Efectiva: {self.lambdaEff.text()}")
        c.save()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())