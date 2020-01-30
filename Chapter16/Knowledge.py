from multiprocessing import Process

'''
# 子进程代码
def test(interval):
    print("我是子进程")


# 执行主进程
def main():
    print("主进程开始")
    p = Process(target=test, args=(1,))
    p.start()
    print("主进程结束")

if __name__ == '__main__':
    main()
'''

# ======================实例1================
# print("======================实例1================")
# -*- coding:utf-8 -*-
from multiprocessing import Process
import time
import os


# 两个子进程会调用的两个方法
def child_1(interval):
    print("子进程(%s)开始执行,父进程为（%s)" % (os.getpid(), os.getppid()))
    t_start = time.time()  # 计时开始
    time.sleep(interval)  # 程序将会被挂起interval秒
    t_end = time.time()
    print("子进程(%s)执行时间为'0.2f'秒" % (os.getpid()), t_end - t_start)


def child_2(interval):
    print("子进程(%s)开始执行,父进程为（%s)" % (os.getpid(), os.getppid()))
    t_start = time.time()  # 计时开始
    time.sleep(interval)  # 程序将会被挂起interval秒
    t_end = time.time()
    print("子进程(%s)执行时间为'0.2f'秒" % (os.getpid()), t_end - t_start)


if __name__ == '__main__':
    print("----------父进程开始执行---------")
    print("父进程PID:%s" % os.getpid())
    p1 = Process(target=child_1, args=(1,))
    p2 = Process(target=child_2, name="mrsoft", args=(2,))
    p1.start()
    p2.start()
    # 同时父进程仍然往下执行，如果P2进程还在执行，将会返回True
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    # 输入p1和p2进程的别名和PID
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("------等待子进程----------")
    p1.join()
    p2.join()
    print("---------父进程执行结束--------")


# -*-coding:utf-8 -*-
# 继承Process类
# print("------------继承Process类--------------")
class SubProcess(Process):
    # 由于Process类本身也有__init__初始犯法，这个子类相当是重写了父类这个方法
    def __init__(self, interval, name=""):
        Process.__init__(self)  # 调用父类初始化方法
        self.interval = interval
        if name:
            self.name = name

    # 重写了Process类的run()方法
    def run(self):
        print("子进程（%s） 开始执行，父进程为（%s）" % (os.getpid(), os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("子进程(%s)执行结束，耗时%0.2f秒" % (os.getpid(), t_stop - t_start))


if __name__ == "__main__":
    print("---------父进程开始执行--------")
    print("父进程PID:%s" % os.getpid())
    p1 = SubProcess(interval=1, name='mrsoft')
    p2 = SubProcess(interval=2)
    # 对一个不帮韩target属性的Process类执行start方法，就会运行这个类中的run方法
    # 故这里会执行p1.run()
    p1.start()
    p2.start()
    # 输出p1和p2的进程的执行状态，如果真正进行，返回True
    print("p1.is_alive=%s" % p1.is_alive())
    print("p2.is_alive=%s" % p2.is_alive())
    # 输出p1和p2进程的别名和PID
    print("p1.name=%s" % p1.name)
    print("p1.pid=%s" % p1.pid)
    print("p2.name=%s" % p2.name)
    print("p2.pid=%s" % p2.pid)
    print("----------等待子进程----------")
    p1.join()
    p2.join()
    print("-----------父进程结束----------")

# 使用进程池创建大量进程
from multiprocessing import Pool


# print("---------#使用进程池创建大量进程---------")
def task(name):
    print("子进程（%s）执行task %s..." % (os.getpid(), name))
    time.sleep(1)  # 睡眠1秒


if __name__ == '__main__':
    print("父进程(%s):." % os.getpid())
    p = Pool(7)
    for i in range(50):
        p.apply_async(task, args=(i,))
    print("等待所有子进程结束")
    p.close()
    p.join()
    print("所有子进程结束")



# 通过队列实现进程间的通讯
# -*-coding:utf-8-*-
from multiprocessing import process


# print("-------通过队列实现进程间的通讯----------")
def plus():
    print("---------子进程1开始--------")
    global g_num
    g_num += 50
    print("g_num is %d" % g_num)
    print("子进程1结束")


def minus():
    print("-----------子进程2开始---------")
    global g_num
    g_num -= 50
    print("g_num is %d" % g_num)
    print("--------子进程2结束---------")


g_num = 100
if __name__ == '__main__':
    print('------主进程开始---------')
    print('g_num is %d' % g_num)
    p1 = Process(target=plus)
    p2 = Process(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("主进程结束")

# 学习队列Queue的相关用法
from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)  # 初始化一个Queue对象，最多可以接受3条put消息
    q.put("消息1")
    q.put("消息2")
    print(q.full())
    q.put("消息3")
    print(q.full())

    # 因为消息队列已满，下面的try都会抛出异常
    # 第一个try会等待两秒后抛出异常，第二个try 会立即抛出异常
    try:
        q.put("消息4", True, 2)
    except:
        print("消息队列已满，现有消息数量：%s" % q.qsize())

    try:
        q.put_nowait("消息4")
    except:
        print("消息队列已满，现有消息数量:%s" % q.qsize())

    # 读取消息时，会先判断消息队列是否为空，在读取
    if not q.empty():
        print('----从队列中获取消息----')
        for i in range(q.qsize()):
            print(q.get_nowait())
    if not q.full():
        q.put_nowait("消息4")




# 使用队列来进行进程之间的通讯
# -*- coding:utf-8 -*-
from multiprocessing import Queue, Process
import time

# 向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息" + str(i)
            q.put(message)
            print("写入:%s" % message)


# 从队列中读取数据
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print("读取%s" % q.get(True, 2))

if __name__ == '__main__':
    print("使用队列来进行进程之间的通讯")
    print("-----父进程开始------")
    q = Queue()
    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("父进程结束")

