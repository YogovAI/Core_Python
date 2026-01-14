# import asyncio

# async def task():
#     await asyncio.sleep(10)  # does NOT block entire program

# async def main():
#     await task()
#     print("done")

# asyncio.run(main())


import asyncio

async def job(name):
    print("start", name)
    await asyncio.sleep(5)
    print("end", name)

async def main():
    await asyncio.gather(
        job("A"),
        job("B"),
        job("C"),
    )

asyncio.run(main())
