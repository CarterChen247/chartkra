# Introduction

    pip3 install chartkra
    
chartkra facilitates the chart displaying on PyQt widgets by the use of matplotlib. It can easily to display the following figures:

1. plots
2. bars
3. pies
4. heatmaps

# Usage

It's very easy to getting started with chartkra. What you need to do is to instantiate a `chartkra` object, and pass its `get_widget` function to PyQt Widget's `addWidget` function:

```python
# initialize
chart = chartkra()
self.gridLayout.addWidget(chart.get_widget())
# draw charts
# ...
```

It's the same way to showing a heatmap, just need to instantiate  a `HeatMap` object instead.

```python
# initialize
heatmap = HeatMap()
self.gridLayout.addWidget(heatmap.get_widget())
# draw heatmap
# ...
```


# Drawing Figures
## Drawing Plots

Use function `draw_plot` to draw. Pass what you're going to show on x axis to `listx`, and what you're going to show on y axis to `listy`.

```python
chart.draw_plot(listx=['12/01', '12/02', '12/03'], listy=[1, 2, 3])
```

<img src="https://i.imgur.com/HkG5Bho.png" height="300">


## Drawing Bars

Use function `draw_bar` to draw. Pass what you're going to show on x axis to `listx`, and what you're going to show on y axis to `listy`.

```python
chart.draw_bar(listx=['zone1', 'zone2', 'zone3'], listy=[1, 2, 3])
```

<img src="https://i.imgur.com/6NYNVm7.png" height="300">

## Drawing Pies

Use function `draw_pie` to draw. The sizes and the labels reference the partition in the pie figure respectively.

```python
chart.draw_pie(sizes=[1, 2, 3], labels=['zone1', 'zone2', 'zone3'])
```

<img src="https://i.imgur.com/FgZXCBa.png" height="300">

## Drawing Heatmaps

### Example: Pedestrian Trajectory Heatmap


<img src="https://i.imgur.com/4FrExRg.png" height="300">


### codes:

```python
heatmap.set_zone(pic='office_inte.jpg', width=8.2, height=10.836, points=points)
heatmap.set_display(accuracy=25, style=plt.cm.jet, rotation=0, title='Pedestrian Trajectory Heatmap')
heatmap.set_colorbar(position='right', width='5%', padding=0.1)
heatmap.show()
```

When creating a heatmap, it is needed to declare the function `set_zone` and its arguments: 

- pic: the path of picture which you want to show in heatmap.
- width: width of the picture(zone).
- height: height of the picture(zone).
- points: the points scattered in the zone, the units of each point need to be the same as the width and the height of picture(zone).

By setting up argument `title` and `title_padding` in function `set_display`, you can customized the title of figure and the padding between title and figure.

### Accuracy

|<img src="https://i.imgur.com/rHyM0Ew.png" height="300">   |  <img src="https://i.imgur.com/6zCeZYV.png" height="300"> |
|---|---|
| <img src="https://i.imgur.com/gU1Rsqx.png" height="300">  | <img src="https://i.imgur.com/8p1tv2p.png" height="300">  |

It is customized by argument `accuracy` in function `set_display`

### Styles


| <img src="https://i.imgur.com/owL0Ryo.png" height="300">  | <img src="https://i.imgur.com/4JHRMj2.png" height="300">  |
|---|---|
| <img src="https://i.imgur.com/ZbFmR9x.png" height="300">  | <img src="https://i.imgur.com/iT4Ome7.png" height="300">  |


It is customized by argument `style` in function `set_display`. The accepted styles can be found on https://matplotlib.org/examples/color/colormaps_reference.html

### Orientations

| <img src="https://i.imgur.com/YwuwDIK.png" height="300">  | <img src="https://i.imgur.com/i6iR7Ag.png" height="300">  |
|---|---|
| <img src="https://i.imgur.com/09BGNuJ.png" height="300">  | <img src="https://i.imgur.com/VdnVpt9.png" height="300">  |

It is customized by argument `rotation` in function `set_display`. The accepted values includes 0, 90, 180 and 270.

### Colorbars

| <img src="https://i.imgur.com/gZakZ8T.png" height="300">  | <img src="https://i.imgur.com/4FrExRg.png" height="300">  |
|---|---|
| <img src="https://i.imgur.com/AIqwjiS.png" height="300">  | <img src="https://i.imgur.com/FTZS3St.png" height="300">  |

It is customized by assign arguments in function `set_colorbar`

- position: accepted values includes top, right, left, bottom.
- width: the width of the colorbar.
- padding: distance between colorbar and figure.

### Others

| <img src="https://i.imgur.com/JVXKPLl.png" >  | <img src="https://i.imgur.com/EaVGAyn.png" >  | <img src="https://i.imgur.com/nnrBAXj.png">  |
|---|---|---|

- The showing of colorbars is not requires. The colorbars will not be showed by default if you don't declare function `set_colorbar`.
- By using function `disable_heatmap_layer`, the figure will only display picture.
- By using function `disable_img_layer`, the figure will only display heatmap layer.

### Save Figure to File
In general situations, using function `show` would be enough for showing a figure. If you want to save the figure to file as well, just declare function `show_and_save_fig` instead and assign arguments `filename` and display resolution like: 

```python
heatmap.show_and_save_fig(filename='sample.png', dpi=150)
```

