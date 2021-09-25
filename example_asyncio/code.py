import asyncio
import time
from random import randrange


async def foo(t):
    time.sleep(t)
    print(f'This is from foo def finish for {t} seconds')
    await asyncio.sleep(0.01)
    return t


async def hello_world():
    result = await foo()
    print(f"This is from hello world {result}")


async def many_task():
    tasks = await asyncio.gather(foo(randrange(1, 4)), foo(randrange(1, 4)), foo(randrange(1, 4)))
    print(tasks)


async def many_task2():
    await asyncio.gather(
        foo(randrange(1, 4)), foo(randrange(1, 4)), foo(randrange(1, 4))
    )

async def concurrent_run():
    task1 = asyncio.create_task(foo(randrange(1, 4)))
    task2 = asyncio.create_task(foo(randrange(1, 4)))
    await task1
    await task2


start = time.time()
asyncio.run(many_task2())
print(f'Finis for {time.time() - start}')