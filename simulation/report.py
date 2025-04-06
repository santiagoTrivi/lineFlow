from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
import datetime
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
import os


def handle_directory( path):
        if not os.path.exists(path):
            os.makedirs(path)


def generate_report(logs):
        subdir = "reportes"
        
        saved_path = os.path.join(os.getcwd(), subdir)
        handle_directory(saved_path)

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(saved_path, f"reporte_{timestamp}.pdf")
        document = SimpleDocTemplate(filename, pagesize=letter)

        # Create styles
        estilos = getSampleStyleSheet()
        estilo_titulo = ParagraphStyle('TitleStyle', parent=estilos['Title'], fontSize=18, fontName='Helvetica-Bold')
    
        # Title
        titulo_texto = "Resultados Simulación"

        titulo = Paragraph(titulo_texto, estilo_titulo)
        # Basic results
        

        # Probability distribution
       

        logs_table = Table(logs)
        ##table2 = Table(data2)

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

        logs_table.setStyle(style1)
        ##table2.setStyle(style2)

        spacer = Spacer(1, 20)

        elements = [titulo, Spacer(1, 12), logs_table]
        document.build(elements)
        