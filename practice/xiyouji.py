# 1. 先确定内容否在网页源代码中，若不在找到内容所在的接口，URL
# 2. 找到URL后，获取小说的名称和所有cid
# 3. 循环cid，拼接出URL，获取所有内容
# 4. 保存小说

"""
同步操作：获取名称，cid的URL
http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}
异步操作：获取所有章节内容，保存到本地
http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}
"""

import requests
import asyncio
import aiohttp
import aiofiles


# 有了url，下载小说内容并保存到本地的方法函数    异步下载小说内容
async def content_download(content_url, title):
    # print(url)
    # name = "西游记"
    async with aiohttp.ClientSession() as session:
        async with session.get(content_url) as response:
            contents = await response.json()
            # print(contents)
            async with aiofiles.open("novel/" + title + ".txt", mode="w", encoding="utf-8") as f:
                await f.write(contents["data"]["novel"]["content"])


# 获取所有章节的url
async def get_content_url():
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    response = requests.get(url)
    # print(response.text)
    items = response.json()["data"]["novel"]["items"]
    items_length = len(items)
    # print(items_length)
    tasks = []
    for i in range(0, items_length):
        cid = items[i]["cid"]
        title = items[i]["title"]
        # print(cid)
        content_url = 'http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500",' \
                      '"cid":"4306063500|' + cid + '","need_bookinfo":1}'
        # print(content_url)
        tasks.append(content_download(content_url, title))  # 列表后面添加对象，直接添加即可，不需要再赋值
    await asyncio.wait(tasks)
    # print(content_urls)


# 异步获取所有章节内容，并保存到本地
# async def main():
#     tasks = []
#     for url in get_content_url():
#         tasks.append(content_download(url))
#     await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(get_content_url())
