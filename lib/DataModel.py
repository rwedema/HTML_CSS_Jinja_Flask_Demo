import matplotlib.pyplot as plt

import numpy as np
from io import BytesIO
import base64


class DataModel:
    def bar_plot(self, filename):
        """
        Create a barplot from a csv file, use numpy to read a bytes stream
        :param filename: from form file upload
        :return: image stream to be placed in <img> tag
        """

        data = np.genfromtxt(filename, delimiter=',', skip_header=1, usecols=range(1, 5))
        data = data.transpose()

        width = 0.45
        ind = np.arange(11) + 0.75

        fig, ax = plt.subplots(1, 1)

        p0 = ax.bar(ind, data[0], width, color='cyan')
        p1 = ax.bar(ind, data[1], width, bottom=data[0], color='violet')
        p2 = ax.bar(ind, data[2], width, bottom=data[0] + data[1], color='g')
        p3 = ax.bar(ind, data[3], width, bottom=data[0] + data[1] + data[2], color='r')

        ax.set_ylabel('kWh')
        ax.set_xlabel('month')
        ax.set_xticks(ind + width / 2.)

        fig.legend((p0[0], p1[0], p2[0], p3[0]), ('kitchen', 'laundry', 'aircon&heater', 'other'))
        fig.tight_layout()

        return self.create_website_plot(fig)


    def create_website_plot(self, fig):
        """
        Given a figure create a stream that can be placed into a <img > tag
        Use the following attribute value for the <img>tag
        <img src="data:image/png;base64,{{ results }}">

        :param fig: a figure created using mathlotlib
        :return: png figure as stream to insert into html
        """

        figfile = BytesIO()
        fig.savefig(figfile, format='png')
        figfile.seek(0)  # rewind to beginning of file
        website_png = base64.b64encode(figfile.getvalue()).decode('ascii')

        return website_png
