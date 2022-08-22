import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= "O'Dara is a nerd and she owns it!", fg='purple', font=('segoe ui', 18, 'bold'))
    canvas1.create_window(250, 300, window=label1)
    
button1 = tk.Button(text='Click Me',command=hello, bg='red',fg='white')
canvas1.create_window(250, 150, window=button1)

root.mainloop()