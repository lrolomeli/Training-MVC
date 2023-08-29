from PySide6.QtCore import QObject, Signal

class CalculatorModel(QObject):
    resultChanged = Signal(int)

    def __init__(self):
        super().__init__()
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        self.resultChanged.emit(self.result)

    def subtract(self, x, y):
        self.result = x - y
        self.resultChanged.emit(self.result)
