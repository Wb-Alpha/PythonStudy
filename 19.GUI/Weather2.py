import tkinter as tk

def button_function(entry):
    print("this is entry", entry)



HIEGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(height=HIEGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get", font=40, command=lambda: button_function(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text="This is a lable", bg='yellow')
label.place(relwidth=1, relheight=1)

root.mainloop()