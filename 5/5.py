import requests
import execjs

ctx = execjs.compile(open('./5.js', mode='r', encoding="utf-8").read())
data = ctx.call('get_data')
headers = {
    "authority": "match.yuanrenxue.cn",
    "referer": "https://match.yuanrenxue.cn/match/5",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


datas = []
for page in range(1, 6):
    cookies = {
        "sessionid": "YourSessionId",
        "RM4hZBv0dDon443M": data["rm4"]

    }
    url = "https://match.yuanrenxue.cn/api/match/5"
    params = {
        "page": page,
        "m": data["m"],
        "f": data["f"]
    }
    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()
    print(response)
    for item in response['data']:
        datas.append(item['value'])

max = sorted(datas, reverse=True)[:5]
print(sum(max))
