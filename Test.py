import tkinter as tk
from tkinter import ttk
from db import Database

db2 = Database('storetest.db')
newWindow = tk.Tk()
newWindow.title("Namenabfrage")
newWindow.geometry("1200x800")
namenlabel = tk.Label(newWindow,
                      text="Bitte geben Sie hier den Namen und die Email-Adresse von sich und Ihren Freunden an, "
                           "die mit Ihnen zum Event gehen",
                      font=('Arial bold', 16))
namenlabel.place(x=10, y=80)
def openNewWindow():
    newWindow2 = tk.Toplevel(newWindow)
    db22 = Database('UNIT.db')

    newWindow2.title("Namenabfrage2")
    newWindow2.geometry("1200x800")
    namenlabel1 = tk.Label(newWindow2,
                           text="Bitte geben Sie hier den Namen und die Email-Adresse von sich und Ihren Freunden an, "
                                "die mit Ihnen zum Event gehen",
                           font=('Arial bold', 16))
    namenlabel1.place(x=10, y=80)
    button_next22 = tk.Button(newWindow2, text="Nächste Seite",
                              command=lambda: [newWindow2.destroy(), print(name11.get()), print(name22.get()), add2()])
    button_next22.bind()
    button_next22.place(x=750, y=700)
    buttonQuit22 = tk.Button(newWindow2, text="Exit", command=newWindow2.destroy)

    buttonQuit22.place(x=10, y=700)
    pb22 = ttk.Progressbar(newWindow2, orient='horizontal', mode='determinate', length=400)

    def add2():
        db22.insert2(name11.get(), name22.get())

    pb22.place(x=400, y=20)
    pb22['value'] = 20
    sociallabel1 = tk.Label(newWindow2, text="Und loggen Sie sich zusätzlich auf einer Social Media Platform ein, "
                                             "um extra Informationen und Angebote erhalten zu können:",
                            font=("Arial Bold", 16))
    sociallabel1.place(x=10, y=330)
    name11 = tk.StringVar()
    nameneintrag1 = tk.Frame(newWindow2)
    nameneintrag1.place(x=100, y=130)
    name_label1 = tk.Label(nameneintrag1, text="Dein Name:")
    name_label1.pack(fill='x', expand=True)
    name_entry1 = tk.Entry(nameneintrag1, textvariable=name11)
    name_entry1.pack(fill='x', expand=True)
    print(name11.get())

    name22 = tk.StringVar()
    nameneintrag22 = tk.Frame(newWindow2)
    nameneintrag22.place(x=400, y=130)
    name22_label = tk.Label(nameneintrag22, text="Namen der Freunde:")
    name22_label.pack(fill='x', expand=True)
    name22_entry = tk.Entry(nameneintrag22, textvariable=name22)
    name22_entry.pack(fill='x', expand=True)
    print(name22.get())

button_next = tk.Button(newWindow, text="Nächste Seite",
                        command=lambda: [openNewWindow(), newWindow.wait_window(), print(name1.get()), print(name2.get()),
                                         add()])
button_next.bind()
button_next.place(x=750, y=700)
buttonQuit2 = tk.Button(newWindow, text="Exit", command=newWindow.destroy)

buttonQuit2.place(x=10, y=700)
pb2 = ttk.Progressbar(newWindow, orient='horizontal', mode='determinate', length=400)


def add():
    db2.insert2(name1.get(), name2.get())


pb2.place(x=400, y=20)
pb2['value'] = 20
sociallabel = tk.Label(newWindow, text="Und loggen Sie sich zusätzlich auf einer Social Media Platform ein, "
                                       "um extra Informationen und Angebote erhalten zu können:",
                       font=("Arial Bold", 16))
sociallabel.place(x=10, y=330)
name1 = tk.StringVar()
nameneintrag = tk.Frame(newWindow)
nameneintrag.place(x=100, y=130)
name_label = tk.Label(nameneintrag, text="Dein Name:")
name_label.pack(fill='x', expand=True)
name_entry = tk.Entry(nameneintrag, textvariable=name1)
name_entry.pack(fill='x', expand=True)
print(name1.get())

name2 = tk.StringVar()
nameneintrag2 = tk.Frame(newWindow)
nameneintrag2.place(x=400, y=130)
name2_label = tk.Label(nameneintrag2, text="Namen der Freunde:")
name2_label.pack(fill='x', expand=True)
name2_entry = tk.Entry(nameneintrag2, textvariable=name2)
name2_entry.pack(fill='x', expand=True)
print(name2.get())





tk.mainloop()
