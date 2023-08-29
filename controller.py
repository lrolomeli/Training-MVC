from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Slot
from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Conectar señales y ranuras
        self.view.add_button.clicked.connect(self.add)
        self.view.subtract_button.clicked.connect(self.subtract)
        self.model.resultChanged.connect(self.update_result_label)

    @Slot()
    def add(self):
        x = int(self.view.input_x.text())
        y = int(self.view.input_y.text())
        self.model.add(x, y)

    @Slot()
    def subtract(self):
        x = int(self.view.input_x.text())
        y = int(self.view.input_y.text())
        self.model.subtract(x, y)

    @Slot(int)
    def update_result_label(self, result):
        self.view.result_label.setText(f"Resultado: {result}")

if __name__ == "__main__":
    app = QApplication([])

    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)

    view.show()
    app.exec()
