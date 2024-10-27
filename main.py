import tkinter
from tkinter import Entry

# 如果想要call所有的模組的話，可以這樣寫。
# from tkinter import *
def get_value():
    # 當觸發button_clicked時，my_label的字樣更改成 Button Got Clicked。
    print("I got clicked")
    e_text = input.get()
    my_label["text"] = e_text

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300) # 設定 tkinter寬500, 高300。
window.config(padx=20, pady=20) # Components跟視窗的內容內縮。

# Label
my_label = tkinter.Label(text="I'm a Label", font=("Arial", 24, "bold")) # 建立my_label內容
# my_label.place(x=0, y=0) # 放到精準的位置。
# my_label.pack() # 把my_label呈現在畫面上。
# 除此之外，我們可以用expand或者，side的方式，去呈現畫面的不同。
# 可參考 文件的檔案：https://tcl.tk/man/tcl8.6/TkCmd/pack.html

# 直接call my_label的方法。
my_label["text"] = "New Text"
my_label.config(text="New Text") #第二個方式。
my_label.grid(column=0, row=0)

# Entry
# Entry就是類似swift裡面的textField，裡面可以輸入內容。
input = Entry(width=10)
input.grid(column=4, row=3)

# text就是按鈕的名稱、command就是連結上button_clicked這個function(可以不用加上call function的括號。）
btn = tkinter.Button(window, text="Click me", command= get_value)
btn.grid(column=1, row=2)

new_btn = tkinter.Button(window, text="New Button")
new_btn.grid(column=3, row=0)

# 確保window有在執行。
window.mainloop()

# 總結一下學習內容，在Tkinter這個GUI的內容裡面，我們可以使用Label、Button、Entry
# 這些內容可以使用。
# Text, Spinbox, Scale(slider), Checkbox, Radiobutton, listbox