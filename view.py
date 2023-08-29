from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

class CalculatorView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora MVC")
        self.layout = QVBoxLayout()

        self.result_label = QLabel("Resultado:")
        self.input_x = QLineEdit()
        self.input_y = QLineEdit()
        self.add_button = QPushButton("Sumar")
        self.subtract_button = QPushButton("Restar")

        self.layout.addWidget(self.input_x)
        self.layout.addWidget(self.input_y)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.subtract_button)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
