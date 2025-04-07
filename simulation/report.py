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

def generate_report(logs, data_exponential, data_poisson, static):
    subdir = "reportes"
    saved_path = os.path.join(os.getcwd(), subdir)
    handle_directory(saved_path)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(saved_path, f"reporte_{timestamp}.pdf")
    document = SimpleDocTemplate(filename, pagesize=letter)

    estilos = getSampleStyleSheet()
    estilo_titulo = ParagraphStyle('TitleStyle', parent=estilos['Title'], fontSize=18, fontName='Helvetica-Bold')

    titulo_texto = "Resultados Simulación"
    titulo = Paragraph(titulo_texto, estilo_titulo)

    # **Cuadro principal: logs de eventos (sin cambios)**
    logs_table = Table(logs)
    logs_table.setStyle(TableStyle([
        ('SPAN', (0, 0), (-1, 0)),
        ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, -1), (0, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # **Nuevo cuadro: resultados exponenciales**
    exp_data = [["Servidor", "Tiempo de Servicio"]]  # Encabezados para la tabla

    # Iterar correctamente sobre todos los datos en `data_exponential`
    for key, values in data_exponential.items():
        for value in values:
            exp_data.append([key, value])  # Agregar cada tiempo de servicio sin saltar ninguno

    exp_table = Table(exp_data)
    exp_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # **Nuevo cuadro: tiempos de llegada Poisson**
    poisson_data = [["Cliente", "Tiempo de Llegada"]]  # Encabezados para la tabla
    for idx, time in enumerate(data_poisson):
        poisson_data.append([f"Cliente {idx + 1}", time])
    poisson_table = Table(poisson_data)
    poisson_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    static_result = [["Resultados Básicos", ""],
                 ["Parámetro", "Valor"]]

    static_result += [
        ["Lambda (λ)", f"{static['Lambda']:.4f}"],
        ["Mu (μ)", f"{static['Mu']:.4f}"],
        ["Rho (ρ)", f"{static['Rho']:.4f}"],
        ["Po", f"{static['Po']:.4f}"],
        ["Ls", f"{static['Ls']:.4f}"],
        ["Lq", f"{static['Lq']:.4f}"],
        ["Ws", f"{static['Ws']:.4f}"],
        ["Wq", f"{static['Wq']:.4f}"]]
    
    stying_table = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    static_table = Table(static_result)
    static_table.setStyle(stying_table)

    dist = [["Distribución de Probabilidad", ""],
    ["n", "Pn", "Fn"]]
    for item in static['Prob_dist']:
        dist.append([str(item['n']), f"{item['Pn']:.4f}", f"{item['Fn']:.4f}"])
    
    dist_table = Table(dist)
    dist_table.setStyle(stying_table)

    spacer = Spacer(1, 20)
    elements = [titulo, spacer, exp_table, spacer, poisson_table, spacer, static_table, spacer, dist_table, spacer, logs_table]
    document.build(elements)
