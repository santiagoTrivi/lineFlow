import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QWidget
)
from PyQt5.QtGui import QDoubleValidator, QIcon
from modules.queueModel import (
    calculate_limited,
    calculate_unlimited
)
from modules.multipleServerQueue import (
    multiple_calculate_unlimited,
    multiple_calculate_limited
)

class CalcFacade(QWidget):
    def __init__(self, mainWindow: QMainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow
        if not mainWindow.singleServer.isChecked() and not mainWindow.multiServer.isChecked():
            QMessageBox.warning(self, "Error", "Por favor, seleccione un tipo de servidor")
            return
        if not mainWindow.isLimited.isChecked() and not mainWindow.isUnlimited.isChecked():
            QMessageBox.warning(self, "Error", "Por favor, seleccione un tipo de modelo")
            return
        
        if not self.mainWindow.lambdaValue.text() or not self.mainWindow.muValue.text():
            QMessageBox.warning(self, "Error", "Por favor, llene los campos Lambda (λ) y Mu (μ)")
            return
        
        self.calculate()


    def calculate(self):
        if self.mainWindow.singleServer.isChecked():
            self.singleServer()

        if self.mainWindow.multiServer.isChecked():
            self.multipleServers()


    def singleServer(self):
        try:
            lambda_val = float(self.mainWindow.lambdaValue.text())
            mu_val = float(self.mainWindow.muValue.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Lambda (λ) y Mu (μ) deben ser números válidos")
            return

        if lambda_val <= 0 or mu_val <= 0:
            QMessageBox.warning(self, "Error", "Lambda (λ) y Mu (μ) deben ser mayores que cero")
            return

        if self.mainWindow.isUnlimited.isChecked() and lambda_val >= mu_val:
            QMessageBox.warning(self, "Error", "Para el modelo ilimitado, Lambda (λ) debe ser menor que Mu (μ)")
            return

        # Perform calculation
        if self.mainWindow.isLimited.isChecked():
            if not self.mainWindow.units.text():
                QMessageBox.warning(self, "Error", "Por favor, llene el campo de unidades para el modelo con límite")
                return
            units = int(self.mainWindow.units.text())
            self.mainWindow.results = calculate_limited(lambda_val, mu_val, units)
            self.mainWindow.lambdaEff.setText(f"{self.mainWindow.results['Lambda_eff']:.4f}")
        else:
            self.mainWindow.results = calculate_unlimited(lambda_val, mu_val)

        # Display results
        self.mainWindow.rho.setText(f"{self.mainWindow.results['Rho']:.4f}")
        self.mainWindow.po.setText(f"{self.mainWindow.results['Po']:.4f}")
        self.mainWindow.ls.setText(f"{self.mainWindow.results['Ls']:.4f}")
        self.mainWindow.lq.setText(f"{self.mainWindow.results['Lq']:.4f}")
        self.mainWindow.ws.setText(f"{self.mainWindow.results['Ws']:.4f}")
        self.mainWindow.wq.setText(f"{self.mainWindow.results['Wq']:.4f}")
        self.mainWindow.populate_table()

    def multipleServers(self):

        if not self.mainWindow.servers.text():
            QMessageBox.warning(self, "Error", "Por favor, llene el campo de cantidad de servidores")
            return

        servers = int(self.mainWindow.servers.text())

        if servers <= 1:
            QMessageBox.warning(self, "Error", "La cantidad de servidores debe ser mayor a 1")
            return

        try:
            lambda_val = float(self.mainWindow.lambdaValue.text())
            mu_val = float(self.mainWindow.muValue.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Lambda (λ) y Mu (μ) deben ser números válidos")
            return
        
        if lambda_val <= 0 or mu_val <= 0:
            QMessageBox.warning(self, "Error", "Lambda (λ) y Mu (μ) deben ser mayores que cero")
            return
        
        if self.mainWindow.isLimited.isChecked():
            if not self.mainWindow.units.text():
                QMessageBox.warning(self, "Error", "Por favor, llene el campo de unidades para el modelo con límite")
                return
            units = int(self.mainWindow.units.text())
            self.mainWindow.results = multiple_calculate_limited(lambda_val, mu_val, servers,units)
            self.mainWindow.lambdaEff.setText(f"{self.mainWindow.results['Lambda_eff']:.4f}")
            self.mainWindow.inactiveServers.setText(f"{self.mainWindow.results['inactive']:.4f}")
        else:
            
            try:
                self.mainWindow.results = multiple_calculate_unlimited(lambda_val, mu_val, servers)
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))
                return

        # Display results
        self.mainWindow.rho.setText(f"{self.mainWindow.results['Rho']:.4f}")
        self.mainWindow.po.setText(f"{self.mainWindow.results['Po']:.4f}")
        self.mainWindow.ls.setText(f"{self.mainWindow.results['Ls']:.4f}")
        self.mainWindow.lq.setText(f"{self.mainWindow.results['Lq']:.4f}")
        self.mainWindow.ws.setText(f"{self.mainWindow.results['Ws']:.4f}")
        self.mainWindow.wq.setText(f"{self.mainWindow.results['Wq']:.4f}")
        self.mainWindow.populate_table()