import tkinter
from tkinter import *
from tkinter import ttk

import requests


# requests  - библиотека для выполнения HTTP-запросов на языке Python.
# Она создана для упрощения взаимодействия с API и веб-сервисами,
# получения данных с веб-сайтов и выполнения других задач на основе HTTP.
#
# Tkinter – это кроссплатформенная библиотека для разработки графического интерфейса на языке Python



def click_button():
    try:
        url = 'http://192.168.113.192/switch/401/turn_on'
        response = requests.get(url, timeout=3)
        btn["image"] = python_logo_on
    except:
        python_logo_of = PhotoImage(file=r'of.png')
        # изменяем текст на кнопке
        btn["image"] = python_logo_of


root = Tk()  # создаем корневой объект - окно
root.title("401")  # устанавливаем заголовок окна
root.geometry("50x30+0+0")  # устанавливаем размеры окна

# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
root.resizable(False,
               False)  # Его первый параметр указывает, может ли пользователь растягивать окно по ширине, а второй параметр - можно ли растягивать по высоте
root.attributes("-alpha", 0.7)
root.attributes("-topmost", True)
root.attributes("-toolwindow", True)


python_logo_on = PhotoImage(file=r'open.png')

btn = ttk.Button(image=python_logo_on, command=click_button)  # создаем кнопку из пакета ttk
btn.pack()


root.mainloop()


# С помощью библиотек requests и Tkinter я создал приложение с графическим интерфейсом,
# которое посылает get запрос при нажатии кнопки