import aiohttp
import asyncio


async def main():
    data = {
        'name': 'germey',
        'age': 22
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=data) as response:
            print(await response.text())


if __name__ == '__main__':
    # 简写
    asyncio.run(main())