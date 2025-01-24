# import tkinter as tk

from tkinter import *
root = Tk()
root.title("윈도우 프로그래밍 연습")
root.geometry("640x480")

# 기본창 띄우기
# label = Label(root, text = "안녕하세요")
# label.park(side = "left")

# 레이아웃 pack()방식
# label1 = Label(root, text = "Top", bg = "red", fg = "white")
# label1.pack(side= "top", fill = "x", padx = 10, pady = 10)

# label2 = Label(root, text = "Bottom", bg = "blue", fg = "white")
# label2.pack(side= "bottom", fill = "x", padx = 10, pady = 10)

# label3 = Label(root, text = "Left", bg = "green", fg = "white")
# label3.pack(side= "left", fill = "y", padx = 10, pady = 10)

# label4 = Label(root, text = "RIGHT", bg = "yellow", fg = "white")
# label4.pack(side= "right", fill = "y", padx = 10, pady = 10)

# label5 = Label(root, text = "CENTER", bg = "purple", fg = "white")
# label5.pack(side= "top", fill = "both", expand= True, padx = 10, pady = 10)


# 레이아웃 그리드 방식


# entry = Entry(root, width = )
# root.mainloop()

# root.mainloop().Pack()






# checkbutton
def show_state():
    print(f"check는 {var.get()}")


var = StringVar(value = "option1")  # 기본값을 나타낸다
radio1 = Radiobutton(root, text = "옵션1", variable= var, value="option1", command = show_state).pack(pady=10)
radio2 = Radiobutton(root, text = "옵션2", variable= var, value="option2", command = show_state).pack(pady=10)

root.mainloop()



def show_selected():
    selection = listbox.curselection()
    print(selection)
    if selection:
        print(f"선택된 과일을 : {listbox.get(selection[])}")


listbox = Listbox(root)
listbox.pack(pady = 10)
for item in ["사과", "바나나", "포도", "체리"]:
    listbox.insert(END, item)

button = Button(root, text = "선택", command = show_selected)
button.pack(pady=10)

root.mainloop()



from tkinter

window = TK()
window.title("쿠폰추첨기")
window.geometry("640x480")


label_img = Label(window)
img = PhotoImage(fle = "cupon.jpg")
label_img.config