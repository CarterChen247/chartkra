
from PyQt5.QtWidgets import QWidget

from chartkra.Chartkra import Chartkra
from widget import Ui_Widget


class ChartWidget(QWidget, Ui_Widget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi(self)
        self.showMaximized()

        plot = Chartkra()
        self.gridLayout_2.addWidget(plot.get_widget())
        plot.draw_plot(listx=['1201','1202','1203'], listy=[1,2,3])

        bar = Chartkra()
        self.gridLayout_2.addWidget(bar.get_widget())
        bar.draw_bar(listx=['zone1', 'zone2', 'zone3'], listy=[1, 2, 3])

        pie = Chartkra()
        self.gridLayout_2.addWidget(pie.get_widget())
        pie.draw_pie(sizes=[1, 2, 3], labels=['zone1', 'zone2', 'zone3'])

        heatmap = Chartkra()
        points = [[2, 2], [3, 3], [4, 4], [8, 8], [4, 4], [4.1, 4.1]]
        self.gridLayout_2.addWidget(heatmap.get_widget(), 0, 1, 2, 1)
        heatmap.draw_heatmap(points=points,accuracy=10, zone_width=8.2, zone_height=10.836, zone_pic='office_inte.jpg', canvas_width=8, canvas_height=6, canvas_dpi=100)



        # [plot] people count / period
        # list1 : people count
        # list2 : timestamp

        # [bar] people count / each zone
        # list1: zone name
        # list2: value

        # [bar] stay time / zone
        # list1: zone name
        # list2: value

        # [pie] zone ratio
        # list1: zone name
        # list2: ratio
