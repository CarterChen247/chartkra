# chartkra

Chartkra stands for `chart` and `charkra`. It facilitates the displaying from `matplotlib` to be embed in `PyQt` Widgets.

## version 0.0.6

Only provides simple visualization features, such as plots, bars, pies and heatmaps.

## usage

By using `chartkra`, it is very easy to draw `matplotlib`'s figure to `PyQt` Widget, the implementation codes will take no longer than 3 lines.

### import

````python
from chartkra.chartkra import chartkra
````

### draw plots
````python
plot = chartkra()
self.gridLayout.addWidget(plot.get_widget())
plot.draw_plot(listx=['12/01','12/02','12/03'], listy=[1,2,3])
````

### draw bars
````python
bar = chartkra()
self.gridLayout.addWidget(bar.get_widget())
bar.draw_bar(listx=['zone1', 'zone2', 'zone3'], listy=[1, 2, 3])
````

### draw pies
````python
pie = chartkra()
self.gridLayout.addWidget(pie.get_widget())
pie.draw_pie(sizes=[1, 2, 3], labels=['zone1', 'zone2', 'zone3'])
````

### draw heatmap
````python
heatmap = chartkra()
points = [[2, 2], [4, 3], [4, 4], [4, 4], [4, 4], [4.1, 4.1]]
self.gridLayout.addWidget(heatmap.get_widget(), 0, 1, 2, 1)
heatmap.draw_heatmap(
    points=points,
    accuracy=10, 
    zone_width=8.2, 
    zone_height=10.836, 
    zone_pic='office_inte.jpg', 
    canvas_width=8, 
    canvas_height=6, 
    canvas_dpi=100
)
````

### demo
![](https://github.com/KazafChen/chartkra/blob/master/demo.png)