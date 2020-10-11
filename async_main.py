#import asyncio
import asyncio
import time

async def my_task(args):
   starttime = time.time()
   print("Total time is",time.time()-starttime)
   return args

def main():
    loop = asyncio.new_event_loop()
    coroutine1 = my_task(1)
    coroutine2 = my_task(2)
    task1 = loop.create_task(coroutine1)
    task2 = loop.create_task(coroutine2)
    loop.run_until_complete(asyncio.wait([task1, task2]))
    print('task1 result:', task1.result())
    print('task2 result:', task2.result())
    loop.close()

main()