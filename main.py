from tkinter import *
from tkinter import ttk

F = "Friend"
L = "Love"
A = "Affair"
M = "Marriage"
E = "Enemies"
Se = "Sex"
game = [F, L, A, M, E, Se]
screen = Tk()
screen.config(bg="thistle", pady=50, padx=50)
screen.title("FLAMES CALCULATOR")
#Unused Variables
menu = Label(text="Main Menu", font=("Imprint MT Shadow", 50, "normal"), fg="red", bg="bisque")
f_b = ttk.Button(text="Flames", style='t.TButton')
p_b = ttk.Button(text="Percentage", style='t.TButton')
head = Label(text="FLAMES", font=("Modern No. 20", 50, "bold"), bg="light coral", fg="black", pady=20)
name_1 = Label(text="Name 1: ", font=("Modern No. 20", 27, "bold"), bg="light coral", fg="white", pady=20)
name_2 = Label(text="Name 2: ", font=("Modern No. 20", 27, "bold"), bg="light coral", fg="white", pady=40)
n_1 = ttk.Entry(font=("Modern No. 20", 25))
n_2 = ttk.Entry(font=("Modern No. 20", 25))
s = ttk.Style()
s.configure('s.TButton', font=("Modern No. 20", 20), foreground="black")
cal_but = ttk.Button(text="Calculate", style='s.TButton')
result = Label(text="", bg="light coral", fg="white", font=("Modern No. 20", 30, "bold"))
head_2 = Label(text="PERCENT", font=("Modern No. 20", 50, "bold"), bg="light coral", fg="black", pady=20)
f = Button(text="F", font=("Modern No. 20", 20, "bold"), bg="light coral", fg="white")
l = Button(text="L", font=("Modern No. 20", 20, "bold"), bg="light coral", fg="white")
a = Button(text="A", font=("Modern No. 20", 20, "bold"), bg="light coral", fg="white")
m = Button(text="M", font=("Modern No. 20", 20, "bold"), bg="light coral", fg="white")
e = Button(text="E", font=("Modern No. 20", 20, "bold"), bg="light coral", fg="white")
S = Button(text="S", font=("Modern No. 20", 20, "bold"), bg="light coral", fg="white")
percentage = Label(text=" ", fg="white", bg="light coral", font=("Matura MT Script Capitals", 50, "normal"), pady=30)


def names():
    NAME_1 = n_1.get()
    NAME_2 = n_2.get()
    flames_finder(NAME_1, NAME_2)


def names_2(a):
    NAME_1 = n_1.get()
    NAME_2 = n_2.get()
    outcome = a
    percentage_finder(NAME_1, NAME_2, outcome)


def flames_finder(NAME_1, NAME_2):
    global game
    game = [F, L, A, M, E, Se]
    num = int(len(NAME_2)) + int(len(NAME_1))
    i = 6
    while i != 1:
        temp = int(num % i) - 1
        game.remove(game[temp])
        i = i - 1
    outcome = game[0]
    percentage_finder(NAME_1, NAME_2, outcome)


def percentage_finder(NAME_1, NAME_2, outcome):
    outcome_1 = outcome
    outcome = f"{NAME_1}{outcome}{NAME_2}"
    name_list = [n.title() for n in outcome]
    num_list = []
    while len(name_list) != 0:
        i = 0
        temp = name_list[0]
        while temp in name_list:
            name_list.remove(temp)
            i = i + 1
        num_list.append(i)
    num_list_2 = []
    while len(num_list) != 2:
        num_list_2 = []
        while len(num_list) != 0:
            i = 0
            j = int(len(num_list)) - 1
            if i == j:
                temp = num_list[i]
                num_list.remove(num_list[i])
                if temp >= 10:
                    z = [n for n in str(temp)]
                    num_list_2.append(int(z[0]))
                    num_list_2.append(int(z[1]))
                    z = []
                else:
                    num_list_2.append(temp)
            else:
                temp = num_list[i] + num_list[j]
                num_list.remove(num_list[0])
                num_list = [n for n in num_list[::-1]]
                num_list.remove(num_list[0])
                num_list = [n for n in num_list[::-1]]
                if temp >= 10:
                    z = [n for n in str(temp)]
                    num_list_2.append(int(z[0]))
                    num_list_2.append(int(z[1]))
                    z = []
                else:
                    num_list_2.append(temp)
        num_list = num_list_2
    Percentage = "".join([str(n) for n in num_list]) + '%'
    changer(outcome_1, Percentage)


def changer(outcome_1, Percentage):
    result.config(text=f"{outcome_1} {Percentage}")
    percentage.config(text=f"{Percentage}")


def clear():
    Flames.destroy()
    Cal.destroy()
    button.destroy()
    Menu()


def clear_2():
    menu.destroy()
    f_b.destroy()
    p_b.destroy()
    FLAMES()


def clear_3():
    menu.destroy()
    f_b.destroy()
    p_b.destroy()
    PERCENT()


def Menu():
    screen.config(bg="bisque")
    menu.grid(row=0, column=1)
    s.configure('t.TButton', font=("Imprint MT Shadow", 50), foreground="dark green", background="bisque")
    f_b.config(command=clear_2)
    p_b.config(command=clear_3)
    f_b.grid(row=1, column=1)
    p_b.grid(row=2, column=1)


def FLAMES():
    screen.config(bg="light coral", padx=50, pady=50)
    head.grid(row=0, column=0, columnspan=2, padx=100)
    name_1.grid(row=1, column=0)
    name_2.grid(row=2, column=0)
    n_1.grid(row=1, column=1, columnspan=3)
    n_2.grid(row=2, column=1, columnspan=3)
    cal_but.config(command=names)
    cal_but.grid(row=3, column=0)
    result.grid(row=3, column=1)


def PERCENT():
    screen.config(bg="light coral", padx=50, pady=50)
    head_2.grid(row=0, column=3)
    f.config(command=lambda: names_2("FRIENDS"))
    l.config(command=lambda: names_2("LOVE"))
    a.config(command=lambda: names_2("AFFAIR"))
    m.config(command=lambda: names_2("MARRIAGE"))
    e.config(command=lambda: names_2("ENEMIES"))
    S.config(command=lambda: names_2("SEX"))
    f.grid(row=1, column=0)
    l.grid(row=1, column=1)
    a.grid(row=1, column=2)
    m.grid(row=1, column=4)
    e.grid(row=1, column=5)
    S.grid(row=1, column=6)
    name_1.grid(row=2, column=3)
    name_2.grid(row=4, column=3)
    n_1.grid(row=3, column=3)
    n_2.grid(row=5, column=3)
    percentage.grid(row=6, column=3)


Flames = Label(text="FLAMES", fg="#800080", font=("Imprint MT Shadow", 70, "normal"), bg="thistle")
Flames.grid(row=0, column=1)
Cal = Label(text="Calculator", fg="#800080", font=("Imprint MT Shadow", 70, "normal"), bg="thistle")
Cal.grid(row=1, column=1)
s = ttk.Style()
s.configure('my.TButton', font=("Imprint MT Shadow", 50), foreground="#800080")
button = ttk.Button(text="Start", width=12, style='my.TButton', command=clear)
button.grid(row=2, column=1)
screen.mainloop()