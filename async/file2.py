import asyncio


async def foo(n):
    await asyncio.sleep(5)
    print("[+] %d" % n)


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    await asyncio.gather(*tasks)


asyncio.run(main())
