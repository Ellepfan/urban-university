import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


test1 = pd.Series([4, 7, -5, 3]) # Создаём объект Series, содержащий числа.
print(test1) # Выводим объект на экран.
print()

city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723],
        'Население': [11.9, 4.9, 1.3, 1.6]} # Создаём словарь с нужной информацией о городах.

test2 = pd.DataFrame(city) # Превращаем словарь в DataFrame, используя стандартный метод библиотеки.
print(test2)
test2.to_csv('output.csv')
test2.to_csv('output2.csv', index=False)
test2.sort_values(by="Население", ascending= False)
print(test2)
print(test2.shape)
print()

data = [35000, 6000, 3000, 2000]
labels = ['Ноутбуки', 'Мониторы', 'Принтеры', 'Клавиатуры']
test = pd.Series(data, index=labels)
print(test)
print(test['Принтеры'])  # выводим значение 3000, обращаясь к элементу с меткой 'Принтеры'
print()

test3 = pd.read_csv('./hubble_data.csv')
print(test3)
print()


plt.close("all")
np.random.seed(123456)
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
df = df.cumsum()
plt.figure()
df.plot()
a = df.plot()
fig = a.get_figure()
fig.savefig('grah.png')

df3 = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum()
df3["A"] = pd.Series(list(range(len(df))))
df3.plot(x="A", y="B")

ax = df3.plot()
fig1 = ax.get_figure()
fig1.savefig('grah1.png')

