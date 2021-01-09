from head import *
def selectPathA():
    global filename1
    filename1 = askdirectory()
    path1.set(filename1)

def selectPathB():
    global filename2
    filename2 = askdirectory()
    path2.set(filename2)

def Quit():
    root.destroy()
def KILL():
    sys.exit()
root = Tk()
root.title("文档比对 (Version:1.0.0)")
root.configure(background="#FFCCCC")
root.geometry("550x250")
path1 = StringVar()
path2 = StringVar()

f1=Frame(root,bg="#FFCCCC")
f2=Frame(root,bg="#FFCCCC")
Label(f1,text = "目标路径:", bg="#FFCCCC").grid(row = 0, column = 0)
Entry(f1,textvariable = path1, width=50).grid(row=1, column=1 )
Label(f1,width=5,bg="#FFCCCC").grid(row = 0, column=2)
Button(f1, text = "路径选择", command = selectPathA, bg="#FF69B4", fg="white").grid(row = 1,column=3)
Label(f2,text = "参考路径:", bg="#FFCCCC").grid(row = 0, column = 0)
Entry(f2, textvariable = path2, width=50).grid(row = 1, column = 1)
Label(f2,width=5,bg="#FFCCCC").grid(row = 0, column=2)
Button(f2, text = "路径选择", command = selectPathB, bg="#FF69B4", fg="white").grid(row = 1,column=3)
Button(root,text="开始运行", command=Quit, bg="#FF69B4", fg="white").place(x=430, y=200)
Button(root,text="取消", command=KILL, bg="#FF69B4", fg="white").place(x=500, y=200)
f1.place(x=15, y=20)
f2.place(x=15, y=100)
root.protocol("WM_DELETE_WINDOW", KILL)
root.resizable(0,0) #防止用户调整尺寸
root.mainloop()