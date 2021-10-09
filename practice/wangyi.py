import requests

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.71 Safari/537.36 ",
    "referer": "https://music.163.com/song?id=1347529801",
    "cookie": "_ntes_nuid=a1fe146046cfccf0fa531323b662d378; _ntes_nnid=273feae3856785405d9597b1e4bf4d76,"
              "1632645355618; JSESSIONID-WYYY=uFtNdIvXtf1%2BdvkVIH3Po7%2FhGFooyPZoPaq4tEvUkZ%2Fil9xHlsM%2FtHPa8qk"
              "%5CnzE3gv9ri1GXjUkdVniziS6Ztm4UXV9jj%2BTb%2FOFhhZZ2JP2xxURsl3aOF88IDaKJ3fjvPoMGT%2B94eoI36llh4IPj"
              "%2BfVvlm3shdYYTR%2FM6Drz6mnyQXWE%3A1633775223761; _iuqxldmzr_=32; "
              "NMTID=00OnJdR0xXI47XWcE6lvqEhRkoCfxEAAAF8ZHwNFA; WEVNSM=1.0.0; WNMCID=ltlbkh.1633773424331.01.0; "
              "WM_NI=JK4xw2rbfRGj2ALedlfL2flsJYGFWqtyjBX01peX%2BVT67cjeiUnaAqj74D7bCJaiJ7PW2qXc6wbFf%2F7%2F"
              "%2FdDKfR2C5RiXnb9Ldq%2FUqmTMR7urNh5EjnHRiuz1nBtUbhAXZzc%3D; "
              "WM_NIKE=9ca17ae2e6ffcda170e2e6ee84cb6894b29f95bb68a89e8fb7d15e839a9eaef83f85b4b8adb64e859b898aca2af0fea"
              "7c3b92a8a95fc99f63ab2beaab3c662f29f8486e768a694fe87ef798a8789a7d67bb8a7a6a3db3cf3b0abb9aa5e98eaf984e96f"
              "ab8ba282c47baae9fca5b66a8196af8ac93d9489fe92db69f6a9aea7e525f5f1e185c741a68efea4b85aab88a283bc48a8afe1b"
              "6f46798939ed8f87a8eb8fba6e9668c8ea796f93bae9ebcb6e1648388969be237e2a3; WM_TID=fXRuavUl4dFEUFFURQdrpThgP"
              "rRHEDmO "
}

response = requests.post(url, headers=headers)
print(response.text)