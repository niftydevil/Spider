# 登录 -> 得到cookie
# 带着cookie 去请求到新的url（需要登录的ur) -> 从而获得需要登录才能看到的数据

# 必须把上面的两个操作连起来
# 我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中的cookie不会丢失
import requests
# 会话
session = requests.session()
data = {
    "loginName": "18614075987",
    "password": "q6035945"
}
# 1. 登录
url = "https://h5.17k.com/ck/user/login"
response = session.post(url=url, data=data)
# print(response.text)
print(response.cookies)
# 2. 拿数据
url_books = "https://user.17k.com/ck/author/shelf?platform=4&appKey=1351550300"
response_books = session.get(url_books)
print(response_books.json())