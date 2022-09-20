import aiohttp
import asyncio


async def main():
    params = {
        'name': 'germey',
        'age': 22
    }
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get', params=params) as response:
            print(await response.text())


if __name__ == '__main__':
    # 简写
    asyncio.run(main())