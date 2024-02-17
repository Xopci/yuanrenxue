import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs

ctx = execjs.compile(open("./2.js", encoding="utf-8").read()).call("get_data")["m"]

# print(ctx)
headers = {
    "authority": "match.yuanrenxue.cn",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://match.yuanrenxue.cn/match/1",
    "sec-ch-ua": "^\\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1702558928",
    "qpfccr": "true",
    "no-alert3": "true",
    "tk": "-4491408042880609388",
    "sessionid": "YourSessionId",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1702559029",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1702559029",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1702559103"
}
url = "https://match.yuanrenxue.cn/api/match/1"

num = 0
sum = 0

for i in range(1, 6):
    params = {
        "page": i,
        "m": ctx
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params)

    data = response.json()
    print(data)

    for d in data["data"]:
        number = list(d.values())[0]
        sum += number
        num += 1

average = sum / num
print(average)

