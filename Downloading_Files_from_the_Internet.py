import aiohttp
import asyncio
import aiofiles
import platform

async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            async with aiofiles.open(filename, 'wb') as file:
                await file.write(await response.read())
            print(f"Downloaded {filename}")

# add list of urls to be downloaded as key value pair as mentioned below
urls = {
    'https://www.dkriesel.com/_media/science/neuronalenetze-en-zeta2-2col-dkrieselcom.pdf': 'neuronalenetze-en-zeta2-2col-dkrieselcom.pdf'
}

async def download_all():
    tasks = [download_file(url, filename) for url, filename in urls.items()]
    await asyncio.gather(*tasks)


if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(download_all())