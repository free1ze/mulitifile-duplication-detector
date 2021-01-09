from head import *
def Quit():
    root.destroy()
root = Tk()
x = StringVar()
count = IntVar()
Q = StringVar()
Q.set("终 止")
root.title("查重")
root.configure(background="#FFCCCC")
root.geometry("650x480")
f1 = Frame(root)
Entry(f1, textvariable=x, width=70).grid(row=0, column=1)  # 能放下40个"█"
Label(f1, text=" loading ", bg="#FFCCCC").grid(row=0, column=2)
Label(f1, textvariable=count, bg="#FFCCCC").grid(row=0, column=3)
Label(f1, text="%", bg="#FFCCCC").grid(row=0, column=4)
scr = scrolledtext.ScrolledText(root, font=(
    '微软雅黑', 10), fg='black', width=65, height=15, wrap=NONE, bg="#CCFFCC")  # scrolledtext.ScrolledText
scrollx = Scrollbar(orient=HORIZONTAL)
scrollx.config(command=scr.xview)
scr.config(xscrollcommand=scrollx.set)
Button(root, textvariable=Q, command=Quit, bg="#FF69B4",
       fg="white", width=10).place(x=550, y=420)
scrollx.place(x=50, y=388, width=525)
scr.place(x=50, y=100)
f1.place(x=50, y=20)
root.resizable(0, 0)  # 防止用户调整尺寸
