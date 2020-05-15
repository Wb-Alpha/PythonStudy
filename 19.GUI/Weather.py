import tkinter as tk

HEIGHT = 300
WIDTH = 400

root = tk.Tk() #生成root主窗口

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place( relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)#设置相对长度，宽度,相对上下左右间隙

#button1 = tk.Button(frame, text='button2', bg='grey', fg='blue')
#button1.pack(side='left', fill='x', expand=True)

button = tk.Button(frame, text="test button", bg='gray', fg='red')
button.grid(row=0, column=0)

label = tk.Label(frame, text='This is a label', bg='yellow')#面板
label.grid(row=1, column=1)

entry = tk.Entry(frame, bg='green')#输入文本框
entry.grid(row=2, column=2)

root.mainloop()#进入主消息循环吧（必备组件）
