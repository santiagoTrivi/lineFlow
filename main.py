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



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setValidators()

    def setValidators(self):
        self.lambdaValue = self.ui.lambda_input_lineEdit
        self.lambdaValue.setValidator(QIntValidator())

        self.muValue = self.ui.mu_input_lineEdit
        self.muValue.setValidator(QIntValidator())

        self.units = self.ui.units_input_lineEdit
        self.units.setValidator(QIntValidator())





if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())