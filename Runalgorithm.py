# coding=utf-8
from head import *
def run():
    dir1 = filename1
    dir2 = filename2
    D1 = os.listdir(dir1)
    D2 = os.listdir(dir2)
    #print("批查重系统 Version:1.0")
    #print("注意:文件格式必须为docx")
    #print("若需要批量格式转化请联系本人")
    t1 = datetime.datetime.now()
    sim_list = []
    index = 1
    scr.insert(INSERT, '疑似相似文件:')
    for file1 in D1:
        index = index+1
        if index<=len(D1):
            num=int(index/len(D1)*100)
            count.set(num)
            a=""
            num=int(num*56/100)
            for i in range(1,num):
                a=a+"█"
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
            if info[0]>=1000:
                Str='\n'+str(info[1])+'    '+str(info[2])+' '+'   相同字数:'+str(info[0])
                scr.insert(INSERT,Str)
                time.sleep(0.001)
            # if float(count_all)/min(len(doc1), len(doc2)) > 0.03:
            # # print(float(count_all)/min(len(doc1), len(doc2)))
            # print(len(doc1))
            # print('\n疑似相似文件:', file1, ' ', file2,
            #       '   相同字数:', count_all)

    def getKey(x):
        return int(x[0])

    t2 = datetime.datetime.now()
    Str='\n比对完成，总用时: '+str(t2 - t1)
    scr.insert(INSERT, Str)
    time.sleep(0.001)
    sim_list.sort(key=getKey)
    time.sleep(0.001)
    Q.set("完 成")