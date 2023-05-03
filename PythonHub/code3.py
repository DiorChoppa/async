import asyncio
from time import time


async def do_something(sec):
    await asyncio.sleep(sec)
    print('result', sec)

async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)
    await do_something(sec)

#1+2+3+4+5+6+7+8+9+10+11+12+13+14+15 = 120sec

async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 16):
            tg.create_task(print1(i))

start = time()
asyncio.run(main())
print(f'Время на работу: {time()-start}')