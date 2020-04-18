import requests
from bs4 import BeautifulSoup 
import time, datetime

sid = ""
dino_aspouk = "http://www.dinorpg.com/dino/2589011"
dino_marche = "http://www.dinorpg.com/dino/2588565"

cookie = {"sid": sid}
sk = str(BeautifulSoup(requests.get("http://www.dinorpg.com/shop", cookies=cookie).text, 'html.parser').find("form",{"id": "form_0"}).get('action'))[-5:]


nb_od = 0
while True:
	requests.post(dino_aspouk+"/act/maudit?buy=1;sk="+sk, data = {'oindex':'0','chk':sid,'qty':'9'}, cookies=cookie)	
	nb_od +=9
	for a in BeautifulSoup(requests.get(dino_marche+"/act/market/mine?sk="+sk,cookies=cookie).text, 'html.parser').findAll("a", href=True):
		if "validate" in a["href"]:
			requests.get("http://www.dinorpg.com"+a["href"],cookies=cookie)
	key = BeautifulSoup(requests.post(dino_marche+"/act/market/propose?submit=1;sk="+sk, data = {'o_odemon':nb_od,'minPrice':nb_od*5000},cookies=cookie).text, 'html.parser').find("input", {'name':'key'})['value']		
	requests.post(dino_marche+"/act/market/propose?submit=1;sk="+sk, data = {'o_odemon':nb_od,'minPrice':nb_od*5000,'key':key,'validate':'on'},cookies=cookie)
	
