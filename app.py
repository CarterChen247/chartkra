import sys

from PyQt5.QtWidgets import QApplication


from ChartWidget import ChartWidget

if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = ChartWidget()
    widget.show()
    sys.exit(app.exec_())

