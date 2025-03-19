import sys
import os
from PyQt5.QtWidgets import (
QApplication, 
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
)
import datetime
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QIcon
from Generator import Ui_GeneratorWindow
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
import datetime
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from modules.randomNumberGenerator import (
    randomPoissonNumbers,
    randomExponentialNumbers
)

class MainGenerator(QMainWindow):
    def __init__(self):
        super(MainGenerator, self).__init__()

        self.ui = Ui_GeneratorWindow()
        self.ui.setupUi(self)


        #user input
        self.lambda_input = self.ui.lambda_input_lineEdit
        self.random_numbers_amount_input = self.ui.random_numbers_amount_input_lineEdit
        self.variables_amount_input = self.ui.variables_amount_input_lineEdit

        self.results = None

        self.database = self.ui.database_tableView

        self.setValidators()
        self.init_actions()


    def init_actions(self):
        self.ui.calculate_pushButton.clicked.connect(self.events)
        self.ui.clean_pushButton.clicked.connect(self.clean_all)
        self.ui.pdf_export_pushButton.clicked.connect(self.pdf_export)
        self.ui.open_reports_pushButton.clicked.connect(self.open_reports)

    def setValidators(self):
        self.lambda_input.setValidator(QDoubleValidator(0.0, 9999.0, 2))
        self.random_numbers_amount_input.setValidator(QIntValidator())
        self.variables_amount_input.setValidator(QIntValidator())


    def events(self):
        try: 
            lambda_ = float(self.lambda_input.text())
            random_numbers_amount = int(self.random_numbers_amount_input.text())
            variables_amount = int(self.variables_amount_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Lambda (λ) y el resto de valores deben ser números válidos.")
            return
        
        if random_numbers_amount <= 0 or variables_amount <= 0:
            QMessageBox.warning(self, "Error", "Las cantidades de variables y de números aleatorios deben ser mayores que cero.")
            return

        if self.ui.poisson_radioButton.isChecked():
            self.results = randomPoissonNumbers(lambda_, variables_amount, random_numbers_amount)
    
        if self.ui.exponencial_radioButton.isChecked():
            self.results = randomExponentialNumbers(lambda_, variables_amount, random_numbers_amount)
        

        self.populate_table()


    def populate_table(self):

        if self.results:
            self.database.setColumnCount(len(self.results[0]))
            self.database.setRowCount(len(self.results))
            self.database.setHorizontalHeaderLabels([f"X{i}" for i in range(1, len(self.results[0]) + 1)])

            for row, item in enumerate(self.results):
                for col, value in enumerate(item):
                    if self.ui.poisson_radioButton.isChecked():
                        self.database.setItem(row, col, QTableWidgetItem(str(value)))
                    else:
                        self.database.setItem(row, col, QTableWidgetItem(f"{value:.4f}"))


    def clean_all(self):
        # Clear all fields and reset the UI
        self.lambda_input.clear()
        self.random_numbers_amount_input.clear()
        self.variables_amount_input.clear()
        self.database.clearContents()
        self.database.setRowCount(0)
        self.results = None

    def open_reports(self):
        path = os.path.join(os.getcwd(), "reportes")
        self.handle_directory(path)
        os.startfile(path)
        
    def handle_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)


    def pdf_export(self):
        # Export results to PDF
        if self.results is None:
            QMessageBox.warning(self, "Error", "Por favor, calcule los valores antes de exportar el reporte")
            return
        
        saved_path = os.path.join(os.getcwd(), "reportes/numeros_aleatorios")
        self.handle_directory(saved_path)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(saved_path, f"reporte_{timestamp}.pdf")
        document = SimpleDocTemplate(filename, pagesize=letter)

        # Create styles
        estilos = getSampleStyleSheet()
        estilo_titulo = ParagraphStyle('TitleStyle', parent=estilos['Title'], fontSize=18, fontName='Helvetica-Bold')
    
        # Title
        titulo = Paragraph("Resultados", estilo_titulo)

        data = [["Resultados", ""],
        [f"X{i}" for i in range(1, len(self.results[0]) + 1)]]


        for row, item in enumerate(self.results):
            if self.ui.poisson_radioButton.isChecked():
                data.append([str(value) for value in item])
            else:
                data.append([f"{value:.4f}" for value in item])

        table = Table(data)

        style = TableStyle([
            ('SPAN', (0, 0), (-1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, -1), (0, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ])

        table.setStyle(style)

        elements = [titulo, Spacer(1, 12), table]
        document.build(elements)

        QMessageBox.information(self, "Éxito", f"Reporte exportado como {filename}")