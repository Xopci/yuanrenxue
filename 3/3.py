import requests
from collections import Counter

session = requests.session()
headers = {
    "Host": "match.yuanrenxue.cn",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "\"Windows\"",
    "Accept": "*/*",
    "Origin": "https://match.yuanrenxue.cn",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://match.yuanrenxue.cn/match/3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
    "Cookie": "Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1704007252,1705130458,1705750005,1705795561; qpfccr=true; no-alert3=true; tk=-4628414839958046607; sessionid=r2w4cfgva3fn49zammpz0tazb12fnjrk; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1704007267,1705130511,1705750038,1705795579; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1705796102; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1705800118"
}
session.headers = headers
data_list = []
for page in range(1, 6):
    url = "https://match.yuanrenxue.cn/jssm"
    response = session.post(url)

    url = "https://match.yuanrenxue.cn/api/match/3"

    datas = session.get(url).json().get("data")
    print(datas)

    for i in datas:
        data_list.append(i["value"])

max = Counter(data_list)
print(max)
