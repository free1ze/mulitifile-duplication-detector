# coding=utf-8
from tkinter import *
from tkinter.filedialog import askdirectory
import time
import tkinter as tk
from tkinter import filedialog
from docx import Document
import re
import os
import base64
import sys
import datetime
import struct
import threading
from tkinter import scrolledtext
# =========================packPhoto=========================

# =============================GUI（X）===============================


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

f1 = Frame(root, bg="#FFCCCC")
f2 = Frame(root, bg="#FFCCCC")
Label(f1, text="目标路径:", bg="#FFCCCC").grid(row=0, column=0)
Entry(f1, textvariable=path1, width=50).grid(row=1, column=1)
Label(f1, width=5, bg="#FFCCCC").grid(row=0, column=2)
Button(f1, text="路径选择", command=selectPathA,
       bg="#FF69B4", fg="white").grid(row=1, column=3)
Label(f2, text="参考路径:", bg="#FFCCCC").grid(row=0, column=0)
Entry(f2, textvariable=path2, width=50).grid(row=1, column=1)
Label(f2, width=5, bg="#FFCCCC").grid(row=0, column=2)
Button(f2, text="路径选择", command=selectPathB,
       bg="#FF69B4", fg="white").grid(row=1, column=3)
Button(root, text="开始运行", command=Quit,
       bg="#FF69B4", fg="white").place(x=430, y=200)
Button(root, text="取消", command=KILL, bg="#FF69B4",
       fg="white").place(x=500, y=200)
f1.place(x=15, y=20)
f2.place(x=15, y=100)
root.protocol("WM_DELETE_WINDOW", KILL)
root.resizable(0, 0)  # 防止用户调整尺寸
root.mainloop()

# ==========================text compare===============================


def getText(wordname):
    d = Document(wordname)
    texts = []
    for para in d.paragraphs:
        texts.append(para.text)
    return texts


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def msplit(s, seperators=',|\.|\?|，|。|？|！'):
    return re.split(seperators, s)


def readDocx(docfile):
    # print('*' * 80)
    # print('文件', docfile, '加载中……')
    paras = getText(docfile)
    segs = []
    for p in paras:
        temp = []
        for s in msplit(p):
            if len(s) > 2:
                temp.append(s.replace(' ', ""))
        if len(temp) > 0:
            segs.append(temp)
    showInfo(segs, docfile)
    return segs


def showInfo(doc, filename='filename'):
    chars = 0
    segs = 0
    for p in doc:
        for s in p:
            segs = segs + 1
            chars = chars + len(s)
    # print('段落数: {0:>8d} 个。'.format(len(doc)))
    # print('短句数: {0:>8d} 句。'.format(segs))
    # print('字符数: {0:>8d} 个。'.format(chars))


def compareParagraph(doc1, i, doc2, j, min_segment=5):
    """
    功能为比较两个段落的相似度，返回结果为两个段落中相同字符的长度与较短段落长度的比值。
    :param p1: 行
    :param p2: 列
    :param min_segment = 5: 最小段的长度
    """
    p1 = doc1[i]
    p2 = doc2[j]
    len1 = sum([len(s) for s in p1])
    len2 = sum([len(s) for s in p2])
    if len1 < 10 or len2 < 10:
        return ([], 0)
    list = []
    for s1 in p1:
        if len(s1) < min_segment:
            continue
        for s2 in p2:
            if len(s2) < min_segment:
                continue
            if s2 in s1:
                list.append(s2)
            elif s1 in s2:
                list.append(s1)

    # 取两个字符串的最短的一个进行比值计算
    count = sum([len(s) for s in list])
    # ratio = float(count) / min(len1, len2)
    # if count > 10 and ratio > 0.1:
    #     print(' 发现相同内容 '.center(80, '*'))
    #     print('文件1第{0:0>4d}段内容：{1}'.format(i + 1, p1))
    #     print('文件2第{0:0>4d}段内容：{1}'.format(j + 1, p2))
    #     print('相同内容：', list)
    # print('相同字符比：{1:.2f}%\n相同字符数： {0}\n'.format(count, ratio * 100))
    return (list, count)

# =======================线程============================


def run():
    dir1 = filename1
    dir2 = filename2
    D1 = os.listdir(dir1)
    D2 = os.listdir(dir2)
    #print("批查重系统 Version:1.0")
    # print("注意:文件格式必须为docx")
    # print("若需要批量格式转化请联系本人")
    t1 = datetime.datetime.now()
    sim_list = []
    index = 1
    scr.insert(INSERT, '疑似相似文件:')
    for file1 in D1:
        index = index+1
        if index <= len(D1):
            num = int(index/len(D1)*100)
            count.set(num)
            a = ""
            num = int(num*56/100)
            for i in range(1, num):
                a = a+"█"
            x.set(a)
        for file2 in D2:
            count_all = 0
            doc1 = readDocx(dir1 + "\\"+file1)
            doc2 = readDocx(dir2 + "\\"+file2)
            for i in range(len(doc1)):
                # if i % 100 == 0:
                #     print(
                #         '处理进行中，已处理段落 {0:>4d} (总数 {1:0>4d} ） '.format(i, len(doc1)))
                for j in range(len(doc2)):
                    list, tempp = compareParagraph(doc1, i, doc2, j)
                    count_all += tempp
            info = [count_all, file1, file2]
            sim_list.append(info)
            if info[0] >= 1000:
                Str = '\n'+str(info[1])+'    '+str(info[2]) + \
                    ' '+'   相同字数:'+str(info[0])
                scr.insert(INSERT, Str)
                time.sleep(0.001)
            # if float(count_all)/min(len(doc1), len(doc2)) > 0.03:
            # # print(float(count_all)/min(len(doc1), len(doc2)))
            # print(len(doc1))
            # print('\n疑似相似文件:', file1, ' ', file2,
            #       '   相同字数:', count_all)

    def getKey(x):
        return int(x[0])

    t2 = datetime.datetime.now()
    Str = '\n比对完成，总用时: '+str(t2 - t1)
    scr.insert(INSERT, Str)
    time.sleep(0.001)
    sim_list.sort(key=getKey)
    time.sleep(0.001)
    Q.set("完 成")


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
# 启动线程
threads = []
threads.append(threading.Thread(target=run))
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)  # 守护线程
        t.start()
root.mainloop()
