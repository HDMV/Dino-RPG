import requests
import time

sid = ""
dino = "http://www.dinorpg.com/dino/2587099"

sk = str(BeautifulSoup(requests.get("http://www.dinorpg.com/shop", cookies=cookie).text, 'html.parser').find("form",{"id": "form_0"}).get('action'))[-5:]
cookie = {"sid": sid}

url = dino+"/act/fight?sk="+sk
url2 = dino+"/act/resurrect?sk="+sk
url3 = dino+"/act/resurrect?confirm=1;sk="+sk
url4 = dino+"/act/stop_heal?sk="+sk+";ajax=1"


while True:
	try:
		requests.get(url, cookies=cookie)
		requests.get(url2, cookies=cookie)
		requests.get(url3, cookies=cookie)
		requests.get(url4, cookies=cookie)
	except:
		time.sleep(1)
