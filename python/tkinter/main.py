import tkinter
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    my_label.config(text=f"{input.get()}")



button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.pack()


 








window.mainloop()