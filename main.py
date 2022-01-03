from tkinter import *
from tkinter import messagebox as mb
import random


window=Tk()
window.title('Таблица умножения - Тренажер')


def start():
    global score_int
    start_button.pack_forget()
    check_button.pack()
    score.pack()
    score_int=0
    make()

def make():
    global first_int
    global second_int
    global score_int
    first_int=random.randint(1,10)
    second_int=random.randint(1,10)
    condition.configure(text=f"{first_int}*{second_int}")
    score.configure(text=f"Правильных ответов: {score_int}")
    answer.delete(0, 'end')

def check():
    global score_int
    user_answer=int(answer.get())
    if (first_int*second_int)==user_answer:
        print("Правильно")
        score_int=score_int+1
    else:
        print("Неправильно")
    make()

condition=Label(window, text='''Нажмите "Старт" ''', font=("Arial", 25))
condition.pack()

answer=Entry(window, width=50)
answer.pack()

check_button=Button(window, text='Проверить!', font=("Arial", 13), command=check)
score=Label(window, text='...', font=("Arial", 10))

start_button=Button(window, text='Начать!', font=("Arial", 13), command=start)
start_button.pack()

window.mainloop()