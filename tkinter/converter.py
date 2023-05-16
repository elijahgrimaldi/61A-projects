import tkinter
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=50)
entry = tkinter.Entry(width=8)
entry.grid(row=0,column=1)
entry_label = tkinter.Label(text="Miles", font=("Arial", 18))
entry_label.grid(row=0,column=2)
calculation_label = tkinter.Label(text="is equal to", font=("Arial", 18))
calculation_label.grid(row=1,column=0)
result_label = tkinter.Label()
result_label.grid(row=1,column=1)
units_label = tkinter.Label(text="Km", font=("Arial", 18))
units_label.grid(row=1,column=2)
def calculate():
    res = int(entry.get())*1.60934
    result_label.config(text=f"{res}", font=("Arial", 18))
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)






window.mainloop()