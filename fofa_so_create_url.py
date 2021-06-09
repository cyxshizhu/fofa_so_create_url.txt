#!/usr/bin/pytho3
# -*- coding: utf-8 -*-
import requests
import base64
import json
def usage():
    print("email和key参数分别是你自己的邮箱和fofa_api_key，使用脚本添加两个参数")
    print("不是fofa高级会员size填1000，填10000会报错")
    print("txt生成到你现在的目录，所以先cd到你想要的目录下面")
    print("用法 python3 file.py")
def fofa_so():
    cmd=input('请输入要查询的fofa规则:，比如app="致远互联-OA":')
    bytes_cmd=cmd.encode("utf-8")
    bytes_command=base64.b64encode(bytes_cmd)
    command=bytes_command.decode("utf-8")
    url = "https://fofa.so:443/api/v1/search/all?email=youremail&key=yourfofa_api_key&size=10000&qbase64=%s"% command
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5 (Ergänzendes Update)) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    r=requests.get(url, headers=headers)
    j=json.loads(r.text,strict=False)
    js=j['results']
    try:
        with open("%s结果.txt"% cmd,"a") as f:
            for i in range (0,10000):
                if 'http' in js[i][0] or 'https' in js[i][0]:
                    f.write (js[i][0])
                else:
                    f.write ('http://'+js[i][0])
                f.write ('\r\n')
    except Exception as e:
        pass
fofa_so()
