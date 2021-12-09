import requests
import json

# url = "https://plogin.m.jd.com/login/login?appid=158&returnurl=https%3A%2F%2Flogistics-mrd.jd.com%2Fexpress%2F%23%2F"
headers = {
    # "cookie": "__jdu=16308965712321829242678; shshshfpa=cd1c212d-6a89-56c0-39e0-44f924d122b5-1630896575; shshshfpb=kYSRULUatdbP%2FKcLYDNo46w%3D%3D; TrackID=1hdIP1c4v9M8ize_MU91FvUMamWejyy17xwCOCJVRc8-rbN5kSmw4pm5CTBo2s6bCeQi1INDoNwNvDvJimRMkMAfz9o42CIuuKZhNgHFvYG-r3ZWj3auPhD0CJ5dLJi_j; pinId=4glSMOrE6aXQDpHYj1IMeA; unpl=V2_ZzNtbRVRQUF8D04GKRAPVmJQFF8RAEURJQtCUHpJXw1lAkEIclRCFnUURlRnGFwUZwYZX0ZcQhVFCEZkexhdBmEKFVxGUXMlfQAoVDYZMgYJA18QD2dAFUUIR2R7Hl4EbgsVWURXQBd2CE9XcxpZBmAFG21yV0UlRThHZHopXTUsbRMQQlBBFHwAQVB9GV8HZAMbXkpURhZyDk9keilf; __jdv=76161171|direct|-|none|-|1635748502712; __jdc=122270672; wlfstk_smdl=jhskmfme1qhyv8v9tii1sldo3kanwx2g; mba_muid=16308965712321829242678; visitkey=68345512855973913; retina=1; cid=9; webp=1; PPRD_P=LOGID.1635749545935.2087277583-UUID.16308965712321829242678; share_cpin=; share_open_id=; share_gpin=; shareChannel=; source_module=; erp=; sc_width=1440; cartLastOpTime=1635759975; cartNum=28; kplTitleShow=1; wq_addr=4850418360%7C2_2826_51942_0%7C%u4E0A%u6D77_%u5609%u5B9A%u533A_%u5357%u7FD4%u9547_%7C%u4E0A%u6D77%u5609%u5B9A%u533A%u5357%u7FD4%u9547%u5FB7%u534E%u4E00%u675126%u53F7302%7C121.313591%2C31.29578; jdAddrId=2_2826_51942_0; jdAddrName=%u4E0A%u6D77_%u5609%u5B9A%u533A_%u5357%u7FD4%u9547_; mitemAddrId=2_2826_51942_0; mitemAddrName=%u4E0A%u6D77%u5609%u5B9A%u533A%u5357%u7FD4%u9547%u5FB7%u534E%u4E00%u675126%u53F7302; areaId=2; ipLoc-djd=2-0-0-0; wxa_level=1; jxsid=16359959804415519924; 3AB9D23F7A4B3C9B=EBI246F42IGGWYMI6XUWGICDTPGZSZVVXWAYQ2447N3ATOCGTZH66H7GS6SWX7VAVCRTBRN7IETJLP2RDG4KUS6TTY; TrackerID=LsZUyKn9JRSnx7hCBTtHTVyMvlQT5e3ba7G3GUG5L8ndx-2sMNXI3WwsTiIynBTDA1kx1PYT0O-IFMw48CxY4-XkdbRfcISX18l_YwzTb5ZbfHHLwOIGZAhGNYiSxX2c; pt_key=AAJhg4rGADBZduC773AChYtb8AEuyIe9nClrkkbyijS0_nM-WxLhRxqcuU5LNNMuLvkHuRxYKPM; pt_pin=15821098636_p; pt_token=bpv4kkwt; pwdt_id=15821098636_p; sfstoken=tk01mcf351c7ca8sM3gzKzMrMiszIlk3UVipRGbIoy8I1pWS8ABLw4tpYxrN7JX6NZHEzh+oDyJq2DEE5QpdV3BZPqZr; shshshfp=d740d4dbb2de1b896d122ceb0e5d6dce; __jda=122270672.16308965712321829242678.1630896571.1636009304.1636012124.15; jxsid_s_u=https%3A//home.m.jd.com/myJd/newhome.action; __jdb=122270672.13.16308965712321829242678|15.1636012124; mba_sid=16360093041924229284781546318.13; __wga=1636012135520.1636010700561.1635995974667.1635754646805.8.4; jxsid_s_t=1636012135616; shshshsID=05e4fdc29075bb7d5b68380e4e1e962d_9_1636012135817; wqmnx1=MDEyNjM5MXRzb2VyPz0xMDJ5dDEzOWkoaE0xQWkgbG8vOHIxWVU0V1NIKQ%3D%3D",
    # "origin": "https://plogin.m.jd.com",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    # "pt_key": "AAJhf46oADCp5mUjeqy4Pv6rrANn7RWcwwNbPD0P41sY9lgpzLevJ1C8cgK9QlgFGe8EUDaROCA",
    # "pt_pin": "15821098636_p",
    "cookie": "pt_key=AAJhg4rGADBZduC773AChYtb8AEuyIe9nClrkkbyijS0_nM-WxLhRxqcuU5LNNMuLvkHuRxYKPM; pt_pin=15821098636_p",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "referer": "https://wqs.jd.com/"
}

url = "https://mapi.m.jd.com/config/display.action?isNewVersion=1&_format_=json"
params = {

}
# response = requests.get(url, params=params, headers=headers)
# print(response.text)
# with open("jd.html", mode="w", encoding="utf-8") as f:
#     f.write(response.text)

# 订单页面，获取物流信息
order_url = 'https://wq.jd.com/bases/orderlist/list?order_type=3&start_page=1&page_size=10&last_page=0&callback=dealListCbA&callersource=mainorder&traceid=1312635610577714579&t=1636010897791&sceneval=2&g_ty=ls&g_tk=5381'
order_params = {
    "order_type": "3",
    "start_page": "1",
    "page_size": "10",
    "last_page": "0",
    "callback": "dealListCbA",
    "callersource": "mainorder",
    "traceid": "1312635610577714579",
    "t": "1636010897791",
    "sceneval": "2",
    "g_ty": "ls",
    "g_tk": "5381"
}
order_response = requests.get(url=order_url, params=order_params, headers=headers)
# print(order_response.text)
info_str = order_response.text[12:-1]
info = json.loads(info_str)
# print(type(info))
order_lists = info['orderList']
# print(order_lists)
lists = []
for order_list in order_lists:
    orderId = order_list['orderId']
    factPrice = int(order_list['factPrice'])/100
    orderDetailLink = order_list['orderDetailLink']
    stateName = order_list['stateInfo']['stateName']
    shopName = order_list['shopInfo']['shopName']
    print(shopName)
    shopLink = order_list['shopInfo']['shopLink']
    productLists = order_list['productList']
    # print(productLists)
    # lists1 = []
    # for productList in productLists:
    #     title = productList['title']
    #     image = productList['image']
    #     amount = productList['amount']
    #     skuLink = productList['skuLink']
    #     lists1.append()
    # content = order_list['progressInfo']['content']
    # progressLink = order_list['progressInfo']['progressLink']
    # print(progressLink)
    # lists.append()
# print(lists)


