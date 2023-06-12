# # import threading
# # from queue import Queue
# # from time import sleep
# #
# #
# # localstorage = threading.local()
# # lock1 = threading.Lock()
# # lock2 = threading.Lock()
# # event1 = threading.Event()
# # semaphore1 = threading.Semaphore(value=5)
# # barrier1 = threading.Barrier(5)
# # q = Queue()
# # q.put('value')
# # print(q.get())
# #
# #
# # def foo():
# #     with lock1:
# #         sleep(1)
# #         with lock2:
# #             print(threading.current_thread().name)
# #
# #
# # def bar():
# #     with lock2:
# #         sleep(1)
# #         with lock1:
# #             print(threading.current_thread().name)
# #
# #
# # def baz():
# #     print('ENTER')
# #     lock1.acquire()
# #     lock1.acquire()
# #     print(threading.current_thread().name)
# #     lock1.release()
# #     lock1.release()
# #
# #     # with lock1:
# #     #     with lock1:
# #     #         print(threading.current_thread().name)
# #
# #
# # # if __name__ == '__main__':
# # #     # thread = threading.Thread(target=baz)
# # #     # thread.start()
# # #     timer = threading.Timer(interval=10, function=baz)
# # #     timer.start()
# #     # threads = [threading.Thread(target=foo, name='Thread FOO'), threading.Thread(target=bar, name='Thread BAR')]
# #     # for thread in threads:
# #     #     thread.start()
# # #
# # def main(i):
# #     # with semaphore1:
# #     localstorage.a = i
# #     for _ in range(10):
# #         with lock1:
# #             print(localstorage.a)
# #         sleep(1)
# #
# #
# # if __name__ == '__main__':
# #     threads = [threading.Thread(target=main, args=(i, ), name=f'Thread-{i}') for i in range(10)]
# #     for thread in threads:
# #         thread.start()
# #
# #
# # def func1():
# #     sleep(5)
# #     event1.set()
# #
# #
# # def func2():
# #     event1.wait()
# #     event1.clear()
# #     print('enter')
# #
# #
# # # if __name__ == '__main__':
# # #     thread1 = threading.Thread(target=func1)
# # #     thread2 = threading.Thread(target=func2)
# # #     thread1.start()
# # #     thread2.start()
#
#
# import multiprocessing
# from time import sleep
#
#
# lock1 = multiprocessing.Lock()
#
#
# def main():
#     for _ in range(100):
#         with lock1:
#             print(multiprocessing.current_process().name)
#         sleep(1)
#
#
# if __name__ == '__main__':
#     processes = [multiprocessing.Process(target=main, name=f'Process-{i}') for i in range(10)]
#     for process in processes:
#         process.start()


from asyncio import Lock, Semaphore, Barrier, Queue, sleep, current_task, run, create_task, get_running_loop


async def foo():
    for _ in range(10):
        print(current_task().get_name())
        await sleep(1)


async def main():
    tasks = [create_task(foo(), name=f'Task-{i}') for i in range(10)]
    for task in tasks:
        await task


run(main())


def my_decorator(func):
    async def wrapper(*args, **kwargs):
        return await func(*args, **kwargs)

    return wrapper