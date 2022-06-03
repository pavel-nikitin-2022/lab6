from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import ttk
from tkinter import *
import tkinter as tk
from fpdf import FPDF
from web import find_files
from web import open_file
dir_name = None
window = None

#в ткинтере нет id у кнопок и таким убогим способом задаем каждой кнопке имя файла
class Update_Button:
    def __init__(self, string, name):
        self.name = name
        self.button = Button(string, text="Открыть", command= self.open_file, padx=5, pady=5).pack(side=LEFT)

    def open_file(self):
        open_file(self.name)

#события при нажатие на кнопку build
def build():
    name = dir_name.get()
    window.destroy()
    main_screen(find_files(name))

#верстка основного экрана
def main_screen(array):
    global dir_name
    global window 
    window = Tk()
    window.geometry("800x600")
    window.title("Найти pdf")

    str1 = Frame(window)
    str2 = Frame(window)

    str1.pack()
    str2.pack()

    Label(str1, text="Введите сторону дирректорию ", padx=5, pady=5).pack(side=LEFT)

    for i in array:
        string = Frame(window)
        string.pack()
        Label(string, text=i, padx=5, pady=5).pack(side=LEFT)
        Update_Button(string, i)    

    dir_name = Entry(str1, width=15)
    dir_name.pack(side=LEFT)

    Button(str2, text="Перейти", command=build, padx=5, pady=5).pack(side=LEFT)

    window.mainloop()

main_screen([])

