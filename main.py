from head import *
from Runalgorithm import *
from Txtcompare import *
from UI_Front import *
from UI_Result import *

# 启动线程
threads = []
threads.append(threading.Thread(target=run))
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)  # 守护线程
        t.start()
root.mainloop()
