import requests
from bs4 import BeautifulSoup 
import time, datetime


dino = "http://www.dinorpg.com/dino/2588565"
sid = ""


METIER = ["z","i1","i2","i3","i4","i5","i6","i7"]
cookie = {"sid": sid}
sk = str(BeautifulSoup(requests.get("http://www.dinorpg.com/shop", cookies=cookie).text, 'html.parser').find("form",{"id": "form_0"}).get('action'))[-5:]


def chasse():
	for j in range(5):
		for i in range(36):
			try:
				url = dino+"/act/chasse?;sk="+sk+";data=loy4%3A%255Fx"+METIER[i//6]+"y4%3A%255Fy"+METIER[i%6]+"gh"
				requests.get(url, cookies=cookie)
				#~ time.sleep(1)
			except:
				i-=1
				time.sleep(1)
				
def cueill():
	for j in range(5):
		for i in range(63):
			try:
				url = dino+"/act/cueill?sk="+sk+";data=loy4%3A%255Fx"+METIER[(i+2)%8]+"y4%3A%255Fy"+METIER[(i+2)//8]+"goR0"+METIER[(i+1)%8]+"R1"+METIER[(i+1)//8]+"goR0"+METIER[i%8]+"R1"+METIER[i//8]+"gh"
				requests.get(url, cookies=cookie)
				#~ time.sleep(1)
				i+=2
			except:
				i-=1
				time.sleep(1)
		url = dino+"/act/cueill?sk=1e9ad;data=loy4%3A%255Fx"+"i7"+"y4%3A%255Fy"+"i7"+"gh"
		requests.get(url, cookies=cookie)


def energy():
	for j in range(5):
		for i in range(36):
			try:
				url = dino+"/act/energy?;sk="+sk+";data=loy4%3A%255Fx"+METIER[i//6]+"y4%3A%255Fy"+METIER[i%6]+"gh"
				requests.get(url, cookies=cookie)
				#~ time.sleep(1)
			except:
				i-=1
				time.sleep(1)



requests.get(dino+"/act/move?sk="+sk+";to=frcbrt", cookies=cookie)
energy()
requests.get(dino+"/act/move?sk="+sk+";to=papy", cookies=cookie)
chasse()
requests.get(dino+"/act/move?sk="+sk+";to=fountj", cookies=cookie)
cueill()
requests.get(dino+"/act/move?sk="+sk+";to=dnv", cookies=cookie)
#fouille()
requests.get(dino+"/act/move?sk="+sk+";to=fountj", cookies=cookie)
requests.get(dino+"/act/move?sk="+sk+";to=port", cookies=cookie)
#peche()
requests.get(dino+"/act/move?sk="+sk+";to=fountj", cookies=cookie)
requests.get(dino+"/act/move?sk="+sk+";to=frcbrt", cookies=cookie)
requests.get(dino+"/act/move?sk="+sk+";to=marche", cookies=cookie)


#~ A FAIRE :
#~ url = dino + "/act/peche?;sk="+sk+";data=loy4%3A%255Fxi1y4%3A%255FyzgoR0zR1zgh"
#~ url = dino + "/act/fouiller?;sk="+sk+";data=loy4%3A%255Fxi7y4%3A%255Fyi4goR0i6R1i4gh"

#~ dnv = fouille
#~ ftnv = cueill
#~ papy = chasse
#~ forcebrut = Energy
#~ port = peche	
