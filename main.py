import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QMessageBox,
    QTableWidgetItem
)
from PyQt5.QtGui import QDoubleValidator, QIcon
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

        self.setWindowTitle("LineFlow | Calculadora de modelos de líneas de espera")

        #user input
        self.lambdaValue = self.ui.lambda_input_lineEdit
        self.muValue = self.ui.mu_input_lineEdit
        self.units = self.ui.units_input_lineEdit
        self.isLimited = self.ui.limited_radioButton
        self.isUnlimited = self.ui.unlimited_radioButton

        # Resultados
        self.results = None
        self.rho = self.ui.rho_output_label
        self.po = self.ui.po_output_label
        self.ls = self.ui.ls_output_label
        self.lq = self.ui.lq_output_label
        self.ws = self.ui.ws_output_label
        self.wq = self.ui.wq_output_label
        self.lambdaEff = self.ui.lambda_eff_output_label
        self.prod_dist = self.ui.prodDist_tableWidget

        # Botones
        self.cleanButton = self.ui.clean_pushButton
        self.pdfExportButton = self.ui.pdf_export_pushButton
        self.calculateButton = self.ui.calculate_pushButton

        # validadores
        self.setValidators()
        self.init_actions()



    def setValidators(self):

        self.lambdaValue.setValidator(QDoubleValidator(0.0, 9999.0, 2))
        self.muValue.setValidator(QDoubleValidator(0.0, 9999.0, 2))
        self.units.setValidator(QDoubleValidator(0.0, 9999.0, 0))  # Units must be integers

    def init_actions(self):
        # Connect buttons to actions
        self.cleanButton.clicked.connect(self.clean_all)
        self.calculateButton.clicked.connect(self.events)
        self.pdfExportButton.clicked.connect(self.pdf_export)

        self.isUnlimited.clicked.connect(self.setUnlimitedModel)
        self.isLimited.clicked.connect(self.setLimitedModel)

    def clean_all(self):
        # Clear all fields and reset the UI
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
        self.prod_dist.clearContents()
        self.prod_dist.setRowCount(0)
        self.isLimited.setChecked(False)
        self.isUnlimited.setChecked(False)
        self.results = None

    def events(self):
        # Validate input
        if not self.lambdaValue.text() or not self.muValue.text():
            QMessageBox.warning(self, "Error", "Por favor, llene los campos Lambda (λ) y Mu (μ)")
            return

        if not self.isLimited.isChecked() and not self.isUnlimited.isChecked():
            QMessageBox.warning(self, "Error", "Por favor, seleccione un tipo de modelo")
            return

        try:
            lambda_val = float(self.lambdaValue.text())
            mu_val = float(self.muValue.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Lambda (λ) y Mu (μ) deben ser números válidos")
            return

        if lambda_val <= 0 or mu_val <= 0:
            QMessageBox.warning(self, "Error", "Lambda (λ) y Mu (μ) deben ser mayores que cero")
            return

        if self.isUnlimited.isChecked() and lambda_val >= mu_val:
            QMessageBox.warning(self, "Error", "Para el modelo ilimitado, Lambda (λ) debe ser menor que Mu (μ)")
            return

        # Perform calculation
        if self.isLimited.isChecked():
            if not self.units.text():
                QMessageBox.warning(self, "Error", "Por favor, llene el campo de unidades para el modelo con límite")
                return
            units = int(self.units.text())
            self.results = calculate_limited(lambda_val, mu_val, units)
            self.lambdaEff.setText(f"{self.results['Lambda_eff']:.4f}")
        else:
            self.results = calculate_unlimited(lambda_val, mu_val)

        # Display results
        self.rho.setText(f"{self.results['Rho']:.4f}")
        self.po.setText(f"{self.results['Po']:.4f}")
        self.ls.setText(f"{self.results['Ls']:.4f}")
        self.lq.setText(f"{self.results['Lq']:.4f}")
        self.ws.setText(f"{self.results['Ws']:.4f}")
        self.wq.setText(f"{self.results['Wq']:.4f}")
        self.populate_table()

    def populate_table(self):
        # Populate the probability distribution table
        if self.results and 'Prob_dist' in self.results:
            self.prod_dist.setColumnCount(3)
            self.prod_dist.setRowCount(len(self.results['Prob_dist']))
            self.prod_dist.setHorizontalHeaderLabels(["n", "Pn", "Fn"])
            self.prod_dist.verticalHeader().setVisible(False)

            for row, item in enumerate(self.results['Prob_dist']):
                self.prod_dist.setItem(row, 0, QTableWidgetItem(str(item['n'])))
                self.prod_dist.setItem(row, 1, QTableWidgetItem(f"{item['Pn']:.4f}"))
                self.prod_dist.setItem(row, 2, QTableWidgetItem(f"{item['Fn']:.4f}"))

    def setUnlimitedModel(self):
        # Hide unnecessary fields for unlimited model
        self.ui.lambda_eff_label.hide()
        self.ui.lambda_eff_output_label.hide()
        self.ui.units_label.hide()
        self.ui.units_input_lineEdit.hide()

    def setLimitedModel(self):
        # Show fields for limited model
        self.ui.lambda_eff_label.show()
        self.ui.lambda_eff_output_label.show()
        self.ui.units_label.show()
        self.ui.units_input_lineEdit.show()

    def pdf_export(self):
        # Export results to PDF
        if self.results is None:
            QMessageBox.warning(self, "Error", "Por favor, calcule los valores antes de exportar el reporte")
            return

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"reporte_{timestamp}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)

        # Title
        c.drawString(100, 750, "Resultados de la Calculadora de Líneas de Espera")
        c.line(100, 745, 500, 745)

        # Basic results
        c.drawString(100, 710, f"Lambda (λ): {self.results['Lambda']:.4f}")
        c.drawString(100, 690, f"Mu (μ): {self.results['Mu']:.4f}")
        c.drawString(100, 670, f"Rho (ρ): {self.results['Rho']:.4f}")
        c.drawString(100, 650, f"Po: {self.results['Po']:.4f}")
        c.drawString(100, 630, f"Ls: {self.results['Ls']:.4f}")
        c.drawString(100, 610, f"Lq: {self.results['Lq']:.4f}")
        c.drawString(100, 590, f"Ws: {self.results['Ws']:.4f}")
        c.drawString(100, 570, f"Wq: {self.results['Wq']:.4f}")
        if 'Lambda_eff' in self.results:
            c.drawString(100, 550, f"Lambda Efectiva: {self.results['Lambda_eff']:.4f}")

        # Probability distribution
        c.drawString(100, 510, "Distribución de Probabilidad")
        
        c.drawString(100,490,"n")
        c.drawString(150,490,"Pn")
        c.drawString(220,490,"Fn")
        
        c.line(100,485,270,485)

        y = 470
        for item in self.results['Prob_dist']:
            c.drawString(100,y,str(item['n']))
            c.drawString(150,y,f"{item['Pn']:.4f}")
            c.drawString(220,y,f"{item['Fn']:.4f}")
            y -= 20

        c.save()
        QMessageBox.information(self, "Éxito", f"Reporte exportado como {filename}")


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())