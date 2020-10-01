import pandas
import datetime

date = str(datetime.date.today())
birthday = False
age = 18

if __name__ == "__main__":

"""
Ici on regarde si il s'est la première fois et qui lance l'IA 
et donc si ce n'est pas le cas on crée le fichiers d'informations
Puis après ça on met à jour l'âge
"""
    try:
        data = pandas.read_csv("informations.csv")
    except:
        frame = pandas.DataFrame({'Emotions': ['Neutral'],  'Emotion Levels': [0], 'Happiness': [50], 'Love': [50], 'Sadness': [0], 'Age' : [18]})
        frame.to_csv("informations.csv", encoding='utf-8')
        data = pandas.read_csv("informations.csv")

    month = date[5:date.index("-", 6)]
    day = date[date.index("-", 7)+1:]
    year = int(date[0:4])
    if month == 9:
        if day >= 22:
            if day == 22:
                birthday = True
            age += 1
    age += year - 2017

    data['Age'] = age
    data.to_csv("informations.csv", encoding='utf-8')

