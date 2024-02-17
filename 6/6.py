import requests
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

ctx = execjs.compile(open("./6.js", mode="r", encoding="utf-8").read())


headers = {
    "authority": "match.yuanrenxue.cn",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}
cookies = {
    "qpfccr": "true",
    "sessionid": "yourSessionId",
    "Hm_lvt_9bcbda9cbf86757998a2339a0437208e": "1708138149,1708167771,1708167908,1708171479",
    "Hm_lpvt_9bcbda9cbf86757998a2339a0437208e": "1708171479",
    "Hm_lvt_c99546cf032aaa5a679230de9a95c7db": "1708138149,1708167771,1708167908,1708171479",
    "no-alert3": "true",
    "Hm_lpvt_c99546cf032aaa5a679230de9a95c7db": "1708171481"
}
datas = []
for i in range(1,6):
    data = ctx.call("getData", i)
    params = {
        "page": i,
        "m": data["m"],
        "q": str(i) + "-" + str(data["t"]) + "|"
    }
    # print(params)
    url = "https://match.yuanrenxue.cn/api/match/6"
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    print(params)
    print(response)

    for item in response["data"]:
        datas.append((item["value"] * 24))

print(sum(datas))