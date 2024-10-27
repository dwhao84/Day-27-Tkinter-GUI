from tkinter import *

win = Tk()
win.title("Mile to Kilometer Converter")
win.config(padx=50, pady=50)

def calculation():
    mile_value = input.get()
    km_value = (float(mile_value) * 1.609344)
    converted_label["text"] = km_value
    print(f"km_value: {km_value}")
    
is_equal_label = Label(text="is equal to")
converted_label = Label(text="0")
kilometers_label = Label(text="Km")
miles_label = Label(text="Miles")
calculate_btn = Button(text="Calculate", command=calculation)
input = Entry()

is_equal_label.grid(column=0, row=1)
input.grid(column=1, row=0)
converted_label.grid(column=1, row=1)
calculate_btn.grid(column=1, row=2)
miles_label.grid(column=2, row=0)
kilometers_label.grid(column=2, row=1)

win.mainloop()