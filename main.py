from window import Window
import pandas
import datetime

date = str(datetime.date.today())
birthday = False
main = Window(800, 500, "Monika")

def get_age(age = 18):
    month = int(date[5:date.index("-", 6)])
    day = int(date[date.index("-", 7)+1:])
    year = int(date[0:4])
    if month == 9:
        if day >= 22:
            if day == 22:
                birthday = True
            age += 1
    age += year - 2017
    return age

if __name__ == "__main__":

    """
    Ici on regarde si il s'est la première fois et qui lance l'IA 
    et donc si ce n'est pas le cas on crée le fichiers d'informations
    Puis après ça on met à jour l'âge
    """

    try:
        data = pandas.read_excel("data/informations.xlsx", index_col=0)
    except:
        frame = pandas.DataFrame({'Emotions': ['Neutral'],  'Emotion Levels': [0], 'Happiness': [50], 'Love': [50], 'Sadness': [0], 'Age' : [18]})
        frame.to_excel("data/informations.xlsx", encoding='utf-8')
        data = pandas.read_excel("data/informations.xlsx", index_col=0)
    data['Age'] = get_age()
    data['Emotions'] = "Stressed"
    try:
        data.to_excel("data/informations.xlsx", encoding='utf-8')
    except Exception as error:
        raise NameError("PermissionError")

