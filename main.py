from window import Window
import pandas
import datetime
import os

"""
Ici on initialise l'IA avec ses informations enrengistrées dans "data/informations.xlsx" 
"""
class IA():

    def __init__(self, window):

        self.window = window
        try:
            self.data = pandas.read_excel("data/informations.xlsx", index_col=0)
        except:
            os.mkdir("data")
            frame = pandas.DataFrame({'Emotions': ['Neutral'],  'Emotion Levels': [0], 'Happiness': [50], 'Love': [50], 'Sadness': [0], 'Age': [self.get_age()[0]]})
            frame.to_excel("data/informations.xlsx", encoding='utf-8')
            self.data = pandas.read_excel("data/informations.xlsx", index_col=0)
            self.birthday = get_age()[1]

    def save_data(self):
        self.data.to_excel("data/informations.xlsx", encoding='utf-8')

    def get_age(self, age = 18):
        date = str(datetime.date.today())
        month = int(date[5:date.index("-", 6)])
        day = int(date[date.index("-", 7)+1:])
        year = int(date[0:4])
        birthday = False
        if month == 9:
            if day >= 22:
                if day == 22:
                    birthday = True
                age += 1
        age += year - 2017
        return age, birthday

if __name__ == "__main__":

    Monika = IA(window=Window(800, 500, "Monika"))
