import tensorflow
import keras
from sklearn import linear_model
import sklearn.utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("student-mat.csv", sep=";")
#g1 g2 g3 to oceny, przewidujemy ich 3 ocene na podstawie 2 ocen
# przyklad outcomu
# 8.486862657853845 [10  9  2  0  0] 0
# przewidujemy ze osoba ta dostanie 8.5 czyli 8 a tak naprawde dostała 0 [...] 0 <- to jest g3 prawdziwe


data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop(predict, axis=1))  # Usuwamy tylko kolumnę docelową "G3"
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

best = 0

#range(30) tyle razy maszyna przetestuje nasz model

'''
for _ in range(30):
#test_size sprawia ze kazdy model trenuje sie na 10% danych wiec kazdokrotnie sa inne dane
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print("Accuracy is: \n", acc)

#zapisujemy model jesli jest lepszy od naszego najlepszego
    if acc > best:
        best = acc
    #zapisujemy model
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
'''
#wczytujemy model
pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)


print('Coefficient: \n', linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    #predictions[x] to nasza przewidywana ocena
    # x_test[x] to nasza data bez g3
    # y_test[x] to nasze g3
    print(predictions[x], x_test[x], y_test[x])

p = 'G1'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()
















