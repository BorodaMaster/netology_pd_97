import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://0.0.0.0:8080/2")

        print(response.status)
        print(await response.json())


asyncio.run(main())
