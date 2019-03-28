# /usr/bin/env python3
# coding = utf-8

import multiprocessing as mp


def handle(i):
    print(i)


if __name__ == '__main__':
    try:
        p = mp.Process(target=handle, args=('1',))
        p.start()
        p.join()
    except Exception:
        p.join()