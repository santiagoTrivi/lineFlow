import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QMessageBox,
    QTableWidgetItem
)
from PyQt5.QtGui import QIntValidator, QIcon
from lineFlow import Ui_MainWindow
from modules.queueModel import (
    calculate_limited,
    calculate_unlimited
)
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
        self.isLimited = self.ui.limited_radioButton
        self.isUnlimited = self.ui.unlimited_radioButton
        
        ## results
        self.results = None
        self.rho = self.ui.rho_output_label
        self.po = self.ui.po_output_label
        self.ls = self.ui.ls_output_label
        self.lq = self.ui.lq_output_label
        self.ws = self.ui.ws_output_label
        self.wq = self.ui.wq_output_label
        self.lambdaEff = self.ui.lambda_eff_output_label
        self.prod_dist = self.ui.prodDist_tableWidget

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

        self.isUnlimited.clicked.connect(self.setUnlimitedModel)
        self.isLimited.clicked.connect(self.setLimitedModel)


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
        self.prod_dist.clear()
        self.isLimited.setChecked(False)
        self.isUnlimited.setChecked(False)
        self.results = None

    # Calculate the values
    def events(self):

        if self.isLimited.isChecked() == False and self.isUnlimited.isChecked() == False:
            QMessageBox.warning(self, "Error", "Por favor, seleccione un tipo de modelo")

        if self.lambdaValue.text() is None or self.muValue.text() is None:
            QMessageBox.warning(self, "Error", "Por favor, llene los campos Lambda (λ), Mu (μ)")
    
        if self.isLimited.isChecked():

            if self.units.text() is None:
                QMessageBox.warning(self, "Error", "Por favor, llene el campo de unidades para el modelo con limite")
                
            self.results = calculate_limited(int(self.lambdaValue.text()), int(self.muValue.text()), int(self.units.text()))
            self.lambdaEff.setText(str(self.results["Lambda_eff"]))
        elif self.isUnlimited.isChecked():
            try:
                self.results = calculate_unlimited(int(self.lambdaValue.text()), int(self.muValue.text()))
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))
                return
        else:
            QMessageBox.warning(self, "Error", "Por favor, seleccione un tipo de modelo")
            return
        
        self.rho.setText(str(self.results["Rho"]))
        self.po.setText(str(self.results["Po"]))
        self.ls.setText(str(self.results["Ls"]))
        self.lq.setText(str(self.results["Lq"]))
        self.ws.setText(str(self.results["Ws"]))         
        self.wq.setText(str(self.results["Wq"]))
        
        
        self.populate_table()

    def populate_table(self):
        if self.results:
            self.prod_dist.setColumnCount(3)
            self.prod_dist.setRowCount(len(self.results['Prob_dist']))
            self.prod_dist.verticalHeader().setVisible(False)
            
            for row, item in enumerate(self.results['Prob_dist']):
                self.prod_dist.setItem(row, 0, QTableWidgetItem(str(item['n'])))
                self.prod_dist.setItem(row, 1, QTableWidgetItem(str(item['Pn'])))
                self.prod_dist.setItem(row, 2, QTableWidgetItem(str(item['Fn'])))


    def setUnlimitedModel(self):
        self.ui.lambda_eff_label.hide()
        self.ui.lambda_eff_output_label.hide()
        self.ui.units_label.hide()
        self.ui.units_input_lineEdit.hide()

    def setLimitedModel(self):
        self.ui.lambda_eff_label.show()
        self.ui.lambda_eff_output_label.show()
        self.ui.units_label.show()
        self.ui.units_input_lineEdit.show()
       

    def pdf_export(self):

        if self.results is None:
            QMessageBox.warning(self, "Error", "Por favor, calcule los valores antes de exportar el reporte")
            return
        
        c = canvas.Canvas(f"reporte.pdf", pagesize=letter)         
        c.drawString(100, 750, "Resultados de la Calculadora de Líneas de Espera")
        c.line(100, 745, 500, 745)
 

        c.drawString(100, 710, f"Lambda (λ): {self.results['Lambda']}")
        c.drawString(100, 690, f"Mu (μ): {self.results['Mu']}")
        c.drawString(100, 670, f"Rho (ρ): {self.results['Rho']}")
        c.drawString(100, 650, f"Po: {self.results['Po']}")
        c.drawString(100, 630, f"Ls: {self.results['Ls']}")
        c.drawString(100, 610, f"Lq: {self.results['Lq']}")
        c.drawString(100, 590, f"Ws: {self.results['Ws']}")
        c.drawString(100, 570, f"Wq: {self.results['Wq']}")
        c.drawString(100, 550, f"Lambda Efectiva: {self.results['Lambda_eff']}")
        
        c.drawString(100,510, f"Distribucion de probabilidad")

        space = 510
        for row, item in enumerate(self.results['Prob_dist']):
            space -= 20
            c.drawString(100, space,f"{item}")
        c.save()

    


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())