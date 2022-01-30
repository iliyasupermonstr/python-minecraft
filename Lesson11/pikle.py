import pickle
locations = {"Максим": "Небо",
             "Антон": "Деревня",
             "Даниил": "Башня"}

secretFile= open("serteFile.txt", "wb")

pickle.dump(locations, secretFile)