import sys
import os
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
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
import datetime
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from calcFacade import CalcFacade

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        width = 940
        height = 570
        # setting  the fixed size of window
        self.setFixedSize(width, height)

        self.setWindowTitle("LineFlow | Calculadora de modelos de líneas de espera")

        self.reports_path = "reportes"

        #user input
        self.singleServer = self.ui.singleServer_radioButton
        self.multiServer = self.ui.multiServer_radioButton
        self.servers = self.ui.servers_input_lineEdit
        self.lambdaValue = self.ui.lambda_input_lineEdit
        self.muValue = self.ui.mu_input_lineEdit
        self.units = self.ui.units_input_lineEdit
        self.isLimited = self.ui.limited_radioButton
        self.isUnlimited = self.ui.unlimited_radioButton

        self.ui.servers_input_lineEdit.hide()
        self.ui.servers_label.hide()

        self.ui.inactive_servers_label.hide()
        self.ui.inactive_servers_output_label.hide()

        self.ui.server_rate_output_label.hide()
        self.ui.server_rate_label.hide()

        # Resultados
        self.results = None
        self.rho = self.ui.rho_output_label
        self.po = self.ui.po_output_label
        self.ls = self.ui.ls_output_label
        self.lq = self.ui.lq_output_label
        self.ws = self.ui.ws_output_label
        self.wq = self.ui.wq_output_label
        self.lambdaEff = self.ui.lambda_eff_output_label
        self.inactiveServers = self.ui.inactive_servers_output_label
        self.server_rate = self.ui.server_rate_output_label
        self.prod_dist = self.ui.prodDist_tableWidget
        self.prod_dist.setColumnWidth(0, 80)
        self.prod_dist.setColumnWidth(1, 220)
        self.prod_dist.setColumnWidth(2, 225)
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
        self.servers.setValidator(QDoubleValidator(0.0, 9999.0, 0))  # Units must be integers

    def init_actions(self):
        # Connect buttons to actions
        self.cleanButton.clicked.connect(self.clean_all)
        self.calculateButton.clicked.connect(self.events)
        self.pdfExportButton.clicked.connect(self.pdf_export)

        self.isUnlimited.clicked.connect(self.setUnlimitedModel)
        self.isLimited.clicked.connect(self.setLimitedModel)

        self.singleServer.clicked.connect(self.setSingleServerMode)
        self.multiServer.clicked.connect(self.setMultiServerMode)

        self.ui.open_reports_pushButton.clicked.connect(self.open_reports)

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
        self.singleServer.setChecked(False)
        self.multiServer.setChecked(False)
        self.servers.clear()
        self.server_rate.clear()
        self.inactiveServers.clear()
        self.results = None

    def events(self):
        self.facade = CalcFacade(self)

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
        self.limitedMultiserversMode()

    def setLimitedModel(self):
        # Show fields for limited model
        self.ui.lambda_eff_label.show()
        self.ui.lambda_eff_output_label.show()
        self.ui.units_label.show()
        self.ui.units_input_lineEdit.show()
        self.limitedMultiserversMode()

    def setMultiServerMode(self):
        self.ui.servers_label.show()
        self.ui.servers_input_lineEdit.show()

    def setSingleServerMode(self):
        self.ui.servers_label.hide()
        self.ui.servers_input_lineEdit.hide()
        

    def open_reports(self):
        path = os.path.join(os.getcwd(), self.reports_path)
        self.handle_directory(path)
        os.startfile(path)
        
    def handle_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def limitedMultiserversMode(self):
        if self.multiServer.isChecked() and self.isLimited.isChecked():
            self.inactiveServers.show()
            self.ui.inactive_servers_label.show()
            self.server_rate.show()
            self.ui.server_rate_label.show()
        elif self.multiServer.isChecked() and self.isUnlimited.isChecked():
            self.inactiveServers.hide()
            self.ui.inactive_servers_label.hide()
            self.server_rate.hide()
            self.ui.server_rate_label.hide()

    def pdf_export(self):
        # Export results to PDF
        if self.results is None:
            QMessageBox.warning(self, "Error", "Por favor, calcule los valores antes de exportar el reporte")
            return
        
        subdir = ""
        if self.singleServer.isChecked():
            subdir = self.reports_path + "/un_servidor"
        else:
            subdir = self.reports_path + "/varios_servidores"
        
        saved_path = os.path.join(os.getcwd(), subdir)
        self.handle_directory(saved_path)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(saved_path, f"reporte_{timestamp}.pdf")
        document = SimpleDocTemplate(filename, pagesize=letter)

        # Create styles
        estilos = getSampleStyleSheet()
        estilo_titulo = ParagraphStyle('TitleStyle', parent=estilos['Title'], fontSize=18, fontName='Helvetica-Bold')
    
        # Title
        titulo_texto = "Resultados de la Calculadora de Líneas de Espera"
        if self.multiServer.isChecked() == True:
            titulo_texto = titulo_texto + " con Vario Servidores"


        titulo = Paragraph(titulo_texto, estilo_titulo)
        # Basic results
        data1 = [["Resultados Básicos", ""],
                 ["Parámetro", "Valor"]]

        data1 += [
        ["Lambda (λ)", f"{self.results['Lambda']:.4f}"],
        ["Mu (μ)", f"{self.results['Mu']:.4f}"],
        ["Rho (ρ)", f"{self.results['Rho']:.4f}"],
        ["Po", f"{self.results['Po']:.4f}"],
        ["Ls", f"{self.results['Ls']:.4f}"],
        ["Lq", f"{self.results['Lq']:.4f}"],
        ["Ws", f"{self.results['Ws']:.4f}"],
        ["Wq", f"{self.results['Wq']:.4f}"]]

        if self.isLimited.isChecked() and 'Lambda_eff' in self.results:
            data1.append(["Lambda Efectiva", f"{self.results['Lambda_eff']:.4f}"])
        
        if self.multiServer.isChecked() and self.isLimited.isChecked():
            data1.append(["Servidores inactivos", f"{self.results['inactive']:.4f}"])

        # Probability distribution
        data2 = [["Distribución de Probabilidad", ""],
        ["n", "Pn", "Fn"]]
        for item in self.results['Prob_dist']:
            data2.append([str(item['n']), f"{item['Pn']:.4f}", f"{item['Fn']:.4f}"])

        table1 = Table(data1)
        table2 = Table(data2)

        style1 = TableStyle([
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, -1), (0, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        style2 = TableStyle([
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, -1), (0, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        table1.setStyle(style1)
        table2.setStyle(style2)

        spacer = Spacer(1, 20)

        elements = [titulo, Spacer(1, 12), table1, spacer, table2]
        document.build(elements)
        QMessageBox.information(self, "Éxito", f"Reporte exportado como {filename}")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
