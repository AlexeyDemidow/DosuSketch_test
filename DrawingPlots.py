import os

import pandas as pd


class DrawingPlots:

    filenames_tuple = ('plot_corners', 'plot_max', 'plot_min', 'plot_mean', 'common', 'ceiling', 'floor',)

    def draw_plots(self, df_path: str, cols: int) -> list[str]:
        """
        :param df_path: Path to Pandas json
        :param cols: Number of displayed columns in the plot
        :return: A list with paths to the plots
        """

        paths = []

        if not os.path.exists('plots/'):
            os.makedirs('plots/')

        df = pd.read_json(df_path)

        df.head(cols)[['gt_corners', 'rb_corners']].plot.bar().set_title(
            'Corner difference').get_figure().savefig('plots/' + self.filenames_tuple[0])

        df.head(cols)[['max', 'floor_max', 'ceiling_max']].plot.bar().set_title(
            'Max deviation').get_figure().savefig('plots/' + self.filenames_tuple[1])

        df.head(cols)[['min', 'floor_min', 'ceiling_min']].plot.bar().set_title(
            'Min deviation').get_figure().savefig('plots/' + self.filenames_tuple[2])

        df.head(cols)[['mean', 'floor_mean', 'ceiling_mean']].plot.bar().set_title(
            'Mean deviation').get_figure().savefig('plots/' + self.filenames_tuple[3])

        df.head(cols)[['min', 'max', 'mean']].plot.bar().set_title(
            'Common deviation').get_figure().savefig('plots/' + self.filenames_tuple[4])

        df.head(cols)[['ceiling_min', 'ceiling_max', 'ceiling_mean']].plot.bar().set_title(
            'Ceiling deviation').get_figure().savefig('plots/' + self.filenames_tuple[5])

        df.head(cols)[['floor_min', 'floor_max', 'floor_mean']].plot.bar().set_title(
            'Floor deviation').get_figure().savefig('plots/' + self.filenames_tuple[6])

        for i in range(len(self.filenames_tuple)):
            paths.append('plots/' + self.filenames_tuple[i] + '.png')
        return paths
