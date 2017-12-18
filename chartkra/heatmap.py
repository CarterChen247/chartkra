import pprint

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.colors import ListedColormap
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import make_axes_locatable

import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import imread
from scipy.ndimage import rotate, filters


class HeatMap:
    def __init__(self):
        # pyqt objects
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # matplotlib objects
        self.pic = None
        self.zone_width = None
        self.zone_height = None
        self.points = None
        self.accuracy = 25
        self.style = plt.cm.jet
        self.rotate_angle = 0
        self.title = None
        self.title_padding = 1
        self.colorbar_enabled = False
        self.colorbar_position = 'right'
        self.colorbar_width = '5%'
        self.colorbar_padding = 0.1

        # for calculation
        self.ratio = None

        # for displaying
        self.hide_img_layer = False
        self.hide_heatmap_layer = False

    def get_widget(self):
        return self.canvas

    def set_zone(self, pic, width, height, points):
        self.pic = pic
        self.zone_width = width
        self.zone_height = height
        self.points = points

    def set_display(self, accuracy, style, rotation, title, title_padding=1):
        self.accuracy = accuracy
        self.style = style
        self.rotate_angle = rotation
        self.title = title
        self.title_padding = title_padding

    def set_colorbar(self, position, width, padding):
        self.colorbar_enabled = True
        self.colorbar_position = position
        self.colorbar_width = width
        self.colorbar_padding = padding

    def disable_img_layer(self):
        self.hide_img_layer = True

    def disable_heatmap_layer(self):
        self.hide_heatmap_layer = True

    def show(self):

        if self.pic is None or self.zone_width is None or self.zone_height is None or self.points is None:
            raise RuntimeError('generating heatmap requires real-world values')

        # load picture
        origin_pic = imread(self.pic)

        # get width and height
        pic_height_px = origin_pic.shape[0]
        pic_width_px = origin_pic.shape[1]

        # store rotated picture
        rotated_pic = rotate(origin_pic, self.rotate_angle)

        # values for calculate extent (avoid distortion)
        size = np.zeros((pic_height_px, pic_width_px))
        size_rotated = rotate(size, self.rotate_angle)
        extent_args = np.zeros((2, 2))
        extent_args[0, 0] = 0
        extent_args[0, 1] = size_rotated.shape[1]
        extent_args[1, 0] = size_rotated.shape[0]
        extent_args[1, 1] = 0

        # define extent
        extent = (extent_args[0, 0], extent_args[0, 1], extent_args[1, 0], extent_args[1, 1])

        # map meter to pixel
        # width_meter = width_px / ratio
        # width_px = width_meter * ratio
        self.ratio = pic_width_px / self.zone_width

        # calculate grid size
        # use short size to calculate
        short_px = pic_width_px
        long_px = pic_height_px
        if pic_width_px > pic_height_px:
            short_px = pic_height_px
            long_px = pic_width_px

        # calculate block size
        part = short_px / self.accuracy
        grid_size_short_f = self.accuracy
        grid_size_long_f = long_px / part

        # generate coordinate at each axis
        ticks_x = np.linspace(0, pic_width_px, grid_size_short_f)
        ticks_y = np.linspace(0, pic_height_px, grid_size_long_f)
        if pic_width_px > pic_height_px:
            ticks_x = np.linspace(0, pic_width_px, grid_size_long_f)
            ticks_y = np.linspace(0, pic_height_px, grid_size_short_f)

        # record score
        score_row = round(grid_size_long_f)
        score_col = round(grid_size_short_f)
        if pic_width_px > pic_height_px:
            score_row = round(grid_size_short_f)
            score_col = round(grid_size_long_f)

        # create score table
        scores = np.zeros((score_row, score_col))

        # update score
        self.update_score(scores, self.points, ticks_x, ticks_y)

        # mapping heatmap and zone picture
        scores = rotate(scores, self.rotate_angle)

        # enlarge heat zones by gaussian blur
        heat = filters.gaussian_filter(scores, 1)

        colormap = self.style
        custom_colormap = colormap(np.arange(colormap.N))
        custom_colormap[:, -1] = np.linspace(0, 1, colormap.N)
        custom_colormap = ListedColormap(custom_colormap)

        max_score = np.amax(scores)
        max_heat = np.amax(heat)
        compensate = max_score / max_heat
        heat_show = heat * compensate

        # the axis is difficult to handle with rotations, so hide it temporarily
        self.ax.axis('off')

        if self.title is not None:
            self.ax.set_title(self.title, y=self.title_padding)

        # show zone picture
        if self.hide_img_layer is False:
            self.ax.imshow(rotated_pic, extent=extent)

        if self.hide_heatmap_layer is False:

            if self.hide_img_layer is False:
                heatmap = self.ax.imshow(heat_show, extent=extent, interpolation='lanczos', cmap=custom_colormap)
            else:
                heatmap = self.ax.imshow(heat_show, extent=extent, interpolation='lanczos', cmap=self.style)

            if self.colorbar_enabled is True:
                self.show_colorbar(heatmap)

    def update_score(self, score, points_input, ticks_x, ticks_y):
        points = np.array(points_input)

        for point in points:
            point_px = point * self.ratio

            # find index
            idx = 0
            dist = abs(point_px[0] - ticks_x[0])
            for i in range(0, len(ticks_x)):
                value = abs(point_px[0] - ticks_x[i])
                if value < dist:
                    dist = value
                    idx = i

            idy = 0
            dist = abs(point_px[1] - ticks_y[0])
            for i in range(0, len(ticks_y)):
                value = abs(point_px[1] - ticks_y[i])
                if value < dist:
                    dist = value
                    idy = i

            # update score
            score[idy][idx] = score[idy][idx] + 1

    def show_colorbar(self, heatmap):

        # locate
        divider = make_axes_locatable(self.ax)
        cax = divider.append_axes(self.colorbar_position, size=self.colorbar_width, pad=self.colorbar_padding)

        # determine orientation
        orientation = 'vertical'
        if self.colorbar_position is 'right' or self.colorbar_position is 'left':
            orientation = 'vertical'
        elif self.colorbar_position is 'top' or self.colorbar_position is 'bottom':
            orientation = 'horizontal'
        # show colorbar
        self.figure.colorbar(heatmap, orientation=orientation, cax=cax)

    def show_and_save_fig(self, filename='chartkra_heatmap.png', dpi=150):
        self.show()
        self.figure.savefig(fname=filename, dpi=dpi)
