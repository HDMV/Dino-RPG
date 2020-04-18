import requests
import time

sid = ""
dino = "http://www.dinorpg.com/dino/2572669"


cookie = {"sid": sid}
sk = str(BeautifulSoup(requests.get("http://www.dinorpg.com/shop", cookies=cookie).text, 'html.parser').find("form",{"id": "form_0"}).get('action'))[-5:]


url1 = dino+"/act/dig?sk="+sk
url2 = dino+"/act/dialog/mine?sk="+sk
url3 = dino+"/act/dialog/mine?goto=repair;sk="+sk
url4 = dino+"/act/dialog/mine?goto=thanks;sk="+sk

while True:
	try:
		requests.get(url1, cookies=cookie)
		requests.get(url2, cookies=cookie)
		requests.get(url3, cookies=cookie)
		requests.get(url4, cookies=cookie)
	except:
		time.sleep(1)
