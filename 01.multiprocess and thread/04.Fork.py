# fork多线程
# 主进程负责新建进程，子进程负责处理具体任务

import os 
import signal


pid = os.fork()
signal.signal(signal.SIGCHLD,signal.SIG_IGN)#避免僵尸进程，子进程结束后，有系统回收资源

if pid < 0:
    print('create process failed')
elif pid == 0:
    print("Child process:")
    print("当前进程的PID:",os.getpid())
    print("当前进程父进程的PID:",os.getppid())
else:
    print("Parent process:")
    print("pid:",pid)
    print("当前进程的PID号:",os.getpid())