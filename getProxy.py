import requests

def get_proxy(timeout = 2, extract_maximum = 5):
    print(f"[*]自動獲取proxy中...")
    res = requests.get('https://free-proxy-list.net/')
    import re
    m = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)
    proxyList = []

    num = 0
    for ip in m:
        proxy = {
            'http':"http://" + ip,
            'https':"http://" + ip
        }
        try:
            res = requests.get('https://api.ipify.org?format=json', proxies=proxy, timeout = timeout)
            proxyList.append(ip)
            print(ip)
            num += 1
            if num == extract_maximum:
                print(f"[!]proxy獲取成功...")
                break
        except:
            print(ip, "FAILED")
            pass
    return proxyList

valid_proxy = get_proxy(extract_maximum=2)

print(valid_proxy)
