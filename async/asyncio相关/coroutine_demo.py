import asyncio


async def execute(x):
    print('Number: ', x)

# 调用async关键字定义的方法，返回一个协程对象，不会真正的执行
coroutine = execute(1)
print('Coroutine: ', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
# 将协程对象注册到事件循环，并启动事件循环
# loop.run_until_complete(coroutine)

# 自己构造task的过程其实可以省略。因为直接注册coroutine也是可以的（见上面）。
# task比coroutine多了状态信息
task = loop.create_task(coroutine)
print('Task: ', task)
loop.run_until_complete(task)
print('Task: ', task)
print('After calling loop')