# import asyncio
#
#
# async def func():
#     print("1010101010101101010101")
#
#
# if __name__ == '__main__':
#     func()  # 上面函数加了async之后，此时的函数是异步协程函数，执行得到的是一个协程对象，需要导入asyncio包
#     asyncio.run(func())  # 协程程序运行需要asyncio模块支持

import asyncio
import time


async def func1():
    print("1111111111111111")
    # time.sleep(3)   # 当程序中出现同步操作（time.sleep()为同步)的时候，异步就中断了
    await asyncio.sleep(3)  # 需要使用asyncio.sleep()，不会中断异步，这是异步操作的代码；await挂起，挂起之后就会切换到别的任务
    print("1111111111111111")


async def func2():
    print("2222222222222222")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("2222222222222222")


async def func3():
    print("3333333333333333")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("3333333333333333")


# if __name__ == '__main__':
#     f1 = func1()
#     f2 = func2()
#     f3 = func3()
#     tasks = [f1, f2, f3]  # 把所有的任务塞在一个列表中
#     t1 = time.time()
#     asyncio.run(asyncio.wait(tasks))  # 一次启动多个任务，基本固定搭配，需要wait方法
#     t2 = time.time()
#     print(t2-t1)

async def main():
    # 第一种方法
    # f1 = func1()
    # await f1    # 一般await挂起操作放在协程对象前面
    # 第二种方法
    tasks = [
        func1(),
        func2(),
        func3()
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
