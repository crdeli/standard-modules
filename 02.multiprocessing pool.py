# /usr/bin/env python3
# coding = utf-8

import multiprocessing as mp


def handle(i):
    print(i)


if __name__ == '__main__':
    try:
        p = mp.Pool(4)
        p.map(func=handle, iterable=['1','2'])
        p.close()
        p.join()
    except Exception:
        print('error')
        p.close()
        p.join()