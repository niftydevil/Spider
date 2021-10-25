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


# 获取所有章节的url
def get_content_url():
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    response = requests.get(url)
    # print(response.text)
    items = response.json()["data"]["novel"]["items"]
    items_length = len(items)
    # print(items_length)
    content_urls = []
    for i in range(0, items_length):
        cid = items[i]["cid"]
        # print(cid)
        content_url = 'http://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500",' \
                      '"cid":"4306063500|' + cid + ',"need_bookinfo":1}'
        # print(content_url)
        content_urls.append(content_url)    # 列表后面添加对象，直接添加即可，不需要再复制
        # print(content_urls)
    return content_urls


# 有了url，下载小说内容并保存到本地的方法函数    异步下载小说内容
async def content_download(url):
    # print(url)
    name = "西游记"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # print(response.json())
            with open(name + ".txt", mode="wb") as f:
                content = response.json()["data"]["novel"]["content"]
                print(content)
                f.write(await content.read())


# 异步获取所有章节内容，并保存到本地
async def main():
    tasks = []
    for url in get_content_url():
        tasks.append(content_download(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
    # get_content_url()