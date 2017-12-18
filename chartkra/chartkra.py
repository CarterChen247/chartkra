import pprint

from chartkra.heatmap import HeatMap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class chartkra:
    def __init__(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)



    def get_widget(self):
        return self.canvas

    def draw_plot(self, listx, listy):
        ax = self.figure.add_subplot(111)
        ax.plot(listx, listy)

    def draw_bar(self, listx, listy):
        ax = self.figure.add_subplot(111)
        ax.bar(listx, listy)
    #
    def draw_pie(self, sizes, labels):
        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')

