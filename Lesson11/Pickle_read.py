import pickle

secretFile = open("serteFile.txt", "rb")
locations = pickle.load(secretFile)

print(locations['Максим'])
print(locations['Даниил'])