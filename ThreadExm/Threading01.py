#coding:utf-8
import time,threading
# #新线程执行的代码
# def loop():
#     print('thread %s is running...'%threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s'%(threading.current_thread().name,n))
#         time.sleep(3)
#     print('thread %s is ended.'%threading.current_thread().name)
# print('thread %s is running...'%threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.'%threading.current_thread().name)

# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(100000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import threading,multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 8
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()























