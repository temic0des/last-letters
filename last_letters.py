import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class LastLetter:

    header_names = ('name', 'gender', 'number',)

    def __init__(self, file=None) -> None:
        self.file = file

    def load_file(self, data):
        try:
            df = pd.read_csv(data, names=self.header_names)
            return df
        except FileNotFoundError:
            pass

    
    def read_all_files(self, files: dict, folder_name=None):
        dataframes = []
        for file in files:
            if folder_name:
                df = self.load_file(f"{folder_name}/{file['file']}")
            else:
                df = self.load_file(file['file'])
            df['year'] = file['year']
            dataframes.append(df)
        combined_df = pd.concat(dataframes)
        return combined_df
    
    @staticmethod
    def get_letter(df, new_column_name, col, pos):
        df[new_column_name] = df[col].map(lambda name: name[pos].lower() if name else "")

    @staticmethod
    def save_plot(name):
        plt.savefig(name, format='png', dpi=150)
    
    def create_last_name_letter(self, df):
        self.get_letter(df=df, new_column_name='name_last_letter', col=self.header_names[0], pos=-1)
        return df
    
    def letter_count_chart(self, df):
        count = df['name_last_letter'].value_counts()
        count.plot(kind='bar')
        plt.title('Count of each last letter of the baby names')
        plt.xlabel('Letters')
        plt.ylabel('Frequency')
        self.save_plot('letter_count_chart.png')
        plt.show()

    def timeline_last_letter(self, df, letter):
        last_letter_timeline = df.where(df['name_last_letter'] == letter).groupby('year')['name_last_letter'].count().reset_index()
        last_letter_timeline['year'] = last_letter_timeline['year'].astype(int)
        last_letter_timeline.rename(columns={'name_last_letter': 'count'}, inplace=True)
        last_letter_timeline['count'] = last_letter_timeline['count'].astype(int)
        plt.plot(last_letter_timeline['year'], last_letter_timeline['count'])
        self.save_plot('timeline_last_letter.png')
        plt.show()

    def count_name_group(self, df):
        name_group = df.groupby(['name_last_letter', 'year'])['name_last_letter'].count()
        return name_group
    
    def crosstable_convert_ng(self, data):
        return data.unstack(0)
    
    def plot_converted_crosstable(self, data, cols_to_plot: list):
        data[cols_to_plot].plot()
        self.save_plot('converted_cross_table.png')
        plt.show()

    def create_first_name_letter(self, df):
        self.get_letter(df=df, new_column_name='name_first_letter', col=self.header_names[0], pos=0)
        return df
    
    def crosstable_convert_lfng(self, data):
        fl_name_group = data.groupby(['name_first_letter', 
                                      'name_last_letter'])['year'].count().unstack(0).sort_values(by='name_last_letter', axis=0)
        return fl_name_group
    
    def get_crosstable_heatmap(self, df_ctng):
        f, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(df_ctng, annot=True, linewidths=1, ax=ax)
        self.save_plot('crosstable_heatmap.png')
        plt.show()
