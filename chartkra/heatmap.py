import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

class heatMap:
    def __init__(self, ax, points, accuracy, zone_width, zone_height, pic):

        # load img
        img = Image.open(pic)

        origin = np.asarray(img)
        height_px = origin.shape[0]
        width_px = origin.shape[1]

        # resize
        img = img.resize((width_px * 2, height_px * 2))
        A = np.asarray(img)

        # extent (need to redraw, axis will be reset)
        extent = (0, width_px, height_px, 0)
        ax.imshow(A, extent=extent)

        """
        codes = [Path.MOVETO] + [Path.LINETO] * 3 + [Path.CLOSEPOLY]
        vertices = [(100, 100), (100, 200), (200, 200), (200, 100), (0, 0)]
        vertices = np.array(vertices, float)
        path = Path(vertices, codes)
        area_draw = PathPatch(path, facecolor='None', edgecolor='green')
        ax.add_patch(area_draw)
        """

        # map meter to pixel
        # width_meter = width_px / ratio
        # width_px = width_meter * ratio
        ratio = width_px / zone_width

        # calculte grid size
        # use short size to calculate
        short_px = width_px
        long_px = height_px
        if width_px > height_px:
            short_px = height_px
            long_px = width_px

        # calculate block size
        part = short_px / accuracy
        grid_size_short_f = accuracy
        grid_size_long_f = long_px / part

        # generate coordinate at each axis
        ticks_x = np.linspace(0, width_px, grid_size_short_f)
        ticks_y = np.linspace(0, height_px, grid_size_long_f)
        if width_px > height_px:
            ticks_x = np.linspace(0, width_px, grid_size_long_f)
            ticks_y = np.linspace(0, height_px, grid_size_short_f)

        # record score
        score = np.zeros((round(grid_size_long_f), round(grid_size_short_f)))

        def update_score(score, points_input):
            points = np.array(points_input)

            for point in points:
                point_px = point * ratio


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

                print('index x,y=' + str(idx) + ',' + str(idy))

                score[idx][idy] = score[idx][idy] + 1

        update_score(score, points)

        ax.imshow(score, cmap=plt.cm.coolwarm, alpha=.9, interpolation='bilinear', extent=extent)