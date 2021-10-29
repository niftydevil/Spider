import requests
import time

from selenium import webdriver

# 先登录
login_url = "https://test-h5.hibixin.com/bixin/cash/index#/login"
driver = webdriver.Chrome()
driver.get(login_url)
driver.find_element_by_xpath('//*[@id="login-form"]/div[1]/div[1]/div[2]/input').send_keys('13120200909')
driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/div[1]/div[2]/input').send_keys('6666')
driver.find_element_by_xpath('//*[@id="login-form"]/button').click()


url = "https://test-h5.hibixin.com/api/payment/withdrawOpenService/queryWithdrawComposeInfo"
headers = {
    "cookies": "smidV2=20210824193211d95c16d217f19ad629f7afa69418b03e00e9fc75fadfa0bd0",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "x-accesstoken": "EiAoq85ADJsqD5A9kbyUrP-S9U829ABPMaQjnKa_zz_ECPk1J7ECMixWp61ceK_yRc69IYYfBKjAMVCumxx_I9nsy0x7FijgW2yu6U5kFWlolqy_8injX_pfjVsoL-6oY3Q_R32zPH05mxf1pw1IbEc4B5dgGbyyVB4_QW6FTfv1JiaCJ0epS6ka5xcLEbYtjqLeY-CNVr9Rg_aDMCvZId_WgO99YtQYLQU-OhW0a_ohuiO1YASq6CUgYeLCWOHab8_IxiVdCVMQC8l2ZZhbv1iHH4uzuP0rEwvScIZzE5o"
}
params = {
    "appId": 10,
    "app": {
        "name": "BIXIN_WECHAT_CLUB"
    },
    "assets": ["INCOME", "BALANCE"],
    "deviceId": "WHJMrwNw1k/GJYr0qPYYVhfngXDS+p6ghWTLw1h/qWm1ZhfJD+aw4XMKKU+HLhgh/aigetAH2RQ+4LbuBUq"
                "+zkE3cKcJhYYXGdCW1tldyDzmQI99"
                "+chXEipg2rk6qlTLa9lCUKKcsmkSqmJzoPeggwzYmmmXo8LlTkQE5YcNLqNo1CXZrYdSBTs0lQvqEsCWw7BE"
                "+uZ0vnrwp6L11y42HyDdKNgeUGJELOn2hVtPrQYyjAMeWs1X0lQ==1487582755342",
    "businessCode": "1002",
    "secretKey": "PudCfNTL"
}

response = requests.get(url=url, params=params, headers=headers)
with open("bixin.html", mode="w") as f:
    f.write(response.text)
