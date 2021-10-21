# 异步爬取优美图上的图片
import asyncio
import aiohttp

urls = [
    "https://www.youmeitu.com/Upload/20200721/1595294943505707.jpg",
    "https://www.youmeitu.com/Upload/20200716/1594862040511418.jpg",
    "https://www.youmeitu.com/Upload/20200721/1595295093163824.jpg"
]


# 有了url，下载图片并保存到本地的方法函数
async def aiodownload(url):
    # 发送请求
    # 得到图片内容
    # 保存图片到本地
    name = url.rsplit("/", 1)[1]
    # 创建异步session    aiohttp.ClientSession()  等价于  requests
    async with aiohttp.ClientSession() as session:
        # 发送异步请求 session.get()   返回response
        async with session.get(url) as response:
            # 把返回结果response 写入文件中
            with open(name, mode="wb") as f:
                # 读取内容是异步的，需要await挂起     response.content.read()  图片 字节保存
                f.write(await response.content.read())
    print(name, "搞定！")


# 多个url异步协程执行
async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
