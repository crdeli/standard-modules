# /usr/bin/env python3
# coding = utf-8
# 多进程标准模板

import multiprocessing as mp


def handle(i):
    print(i)
    while True:
        pass

if __name__ == '__main__':
    try:
        for i in range(3)
            p = mp.Process(target=handle, args=('1',))
            p.daemon = False    #默认值为False 表示主进程运行结束后 不会影响子进程的运行，知道子进程运行完，进程才会结束
                                #如果设置为True 则主进程运行完毕则所有子进程也不再运行一起退出
            process.append(p)
        for p in process:
            p.start()
        for i in process:
            i.join()            #阻塞等对应子进程的退出,然后回收子进程
    except Exception:
        pass