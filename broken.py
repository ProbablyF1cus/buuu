import time
import asyncio


async def dish(plants, water, grow, islive):
    print(f"0 Beginning of sowing the {plants} plant")
    print(f'1 Soaking of the {plants} started')
    await asyncio.sleep(water / 1000)
    print(f"2 Soaking of the {plants} is finished")
    print(f"3 Shelter of the {plants} is supplied")
    await asyncio.sleep(grow / 1000)
    print(f"4 Shelter of the {plants} is removed")
    print(f"5 The {plants} has been transplanted")
    await asyncio.sleep(water / 1000)
    print(f"6 The {plants} has taken root")
    print(f"9 The seedlings of the {plants} are ready")


async def feed(plants):
    print(f'7 Application of fertilizers for {plants}')
    await asyncio.sleep(3 / 1000)
    print(f'7 Fertilizers for the {plants} have been introduced')
    print(f'8 Treatment of {plants} from pests')
    await asyncio.sleep(5 / 1000)
    print(f'8 The {plants} is treated from pests')


async def sowing(*data):
    tasks = []
    for who in data:
        tasks.append(asyncio.create_task(dish(*who)))
        tasks.append(asyncio.create_task(feed(who[0])))
    await asyncio.gather(*tasks)


data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews_2(*data))
print(time.time() - t0)