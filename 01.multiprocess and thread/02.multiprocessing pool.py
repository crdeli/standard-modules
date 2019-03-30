# /usr/bin/env python3
# coding = utf-8

import multiprocessing as mp


def handle(i):
    print(i)


if __name__ == '__main__':
    try:
        p = mp.Pool(4)
        p.map(func=handle, iterable=['1','2'])
        p.close()           #即不能再向进程池中加入事件
        p.join()            #阻塞等待进程池处理事件结束后回收进程池
    except Exception:
        print('error')
        p.close()
        p.join()