import requests
import re
import time

def write_to_file(filename,name):
    f = open(filename,'a')
    f.writelines(name+'\n')
    f.close()

def get_proxy():
    global port,res
    url ='http://www.xicidaili.com/wt/'
    list= [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"        
        ]
    headers = {'User-Agent':list[0]}
    r = requests.get(url,headers = headers)
    res = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",r.text)
    port = re.findall(r"<td>([0-9]{2,5})</td>", r.text,flags=0)


def test_ip():
    headers = {"token": "f6600522c55de1292bf550f9958058d8"}
    url = 'http://ip.taobao.com/service/getIpInfo2.php'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    ip = res[1]+':'+port[1]
    data = {'ip':'myip'}
    for i in range(len(res)):
        time.sleep(2)
        try:
            proxies = {'http':'http:'+str(res[i])+':'+str(port[i])}
            r = requests.post(url,headers = headers,proxies = proxies,timeout = 3,data=data)
            proxie_ip = 'http:'+str(res[i])+':'+str(port[i])
            write_to_file('ip.txt',proxie_ip)
            print(r.text)
        except:
            print('http:' + str(res[i]) + ':' + str(port[i])+'不能用')

get_proxy()
test_ip()
