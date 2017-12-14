from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from chartkra.heatmap import heatMap


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

    def draw_pie(self, sizes, labels):
        ax = self.figure.add_subplot(111)
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')

    def draw_heatmap(self, points, accuracy, zone_width, zone_height, zone_pic, canvas_width, canvas_height, canvas_dpi):
        ax = self.figure.add_subplot(111)
        heatmap = heatMap(ax, points, accuracy, zone_width, zone_height, zone_pic)