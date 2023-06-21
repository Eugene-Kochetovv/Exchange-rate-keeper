import aiohttp
import asyncio

from currency.service import new_currencies

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingate.com/v2/rates/merchant/') as resp:
            if resp.status == 200:
                currencies = await resp.json()
                print(await new_currencies(currencies))

            else:
                pass







asyncio.run(main())
