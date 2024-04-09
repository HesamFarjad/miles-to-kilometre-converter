from tkinter import *


def action():
    miles_val = float(input_val.get())
    final_val = round(miles_val * 1.60934, 2)
    label_preview.config(text=final_val)


window = Tk()
window.title("Mile to km convertor")
# window.minsize(500, 500)
window.config(padx=20, pady=20)

label = Label()
label.config(text="is equal to", font=("Arial", 26))
label.grid(row=1, column=0)

label_miles = Label(text="Miles", font=("Arial", 26))
label_miles.grid(row=0, column=2)

label_km = Label(text="KM", font=("Arial", 26))
label_km.grid(row=1, column=2)

label_preview = Label()
label_preview.grid(row=1, column=1)

input_val = Entry(width=7)
input_val.grid(row=0, column=1)

button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
