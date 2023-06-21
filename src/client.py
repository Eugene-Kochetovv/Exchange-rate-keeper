import aiohttp
import asyncio
import json

from currency.service import save_currencies

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingate.com/v2/rates/merchant/') as resp:
            if resp.status == 200:
                currencies = await resp.json()
                print(await save_currencies(currencies))
            else:
                pass


async def checking_task():
    while True:
        await asyncio.sleep(1)
        await main()

loop = asyncio.get_event_loop()
loop.create_task(checking_task())
loop.run_forever()
