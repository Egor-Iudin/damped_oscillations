from PyQt5 import QtWidgets, QtCore
from design import design2
import numpy as np
import pyqtgraph as pg


class App(QtWidgets.QMainWindow, design2.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pg.setConfigOptions(antialias=True)
        self.graphicsView.plot()
        self.doubleSpinBox_1.setValue(1)
        self.doubleSpinBox_2.setValue(1)
        self.doubleSpinBox_3.setValue(1)
        self.doubleSpinBox_4.setValue(1)

    def update_graphics(self):
        self.graphicsView.clear()
        if self.doubleSpinBox_1.value() == 0:
            self.doubleSpinBox_1.setValue(1)
            a0 = 1
        else:
            a0 = self.doubleSpinBox_1.value()
        if self.doubleSpinBox_2.value() == 0:
            self.doubleSpinBox_2.setValue(1)
            k = 1
        else:
            k = self.doubleSpinBox_2.value()
        if self.doubleSpinBox_3.value() == 0:
            self.doubleSpinBox_3.setValue(1)
            m = 1
        else:
            m = self.doubleSpinBox_3.value()
        if self.doubleSpinBox_4.value() == 0:
            self.doubleSpinBox_4.setValue(1)
            b = 1
        else:
            b = self.doubleSpinBox_4.value()
        w0s = k/m
        al = b/(2*m)
        w = np.sqrt(w0s - np.power(al, 2))
        shift = 0.01
        x = np.arange(0, 400, shift)
        y1 = a0 * np.exp(-al * x) * np.cos(w * x)
        y2 = a0 * np.exp(-al * x)
        self.graphicsView.plot(x, y1, pen=pg.mkPen(color="r"))
        self.graphicsView.plot(x, y2, pen=pg.mkPen(color="y", style=QtCore.Qt.DashLine))
        self.graphicsView.plot(x, -y2, pen=pg.mkPen(color="y", style=QtCore.Qt.DashLine))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()