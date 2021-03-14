import asyncio
from random import randrange


async def foo(n):
    s = randrange(5)
    print("[%d] start sleeping for %d" % (n, s))
    await asyncio.sleep(s)
    print("[+] %d finish sleep" % n)


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    result = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    return result


asyncio.run(main())
