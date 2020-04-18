import requests
from bs4 import BeautifulSoup 
import time, datetime
from DATA import M_papy_joe, M_lanterne, M_shaman, M_elem, M_farm_tournoi, R_pigmou

#########################################################
sid = ""

#~ dino = "http://www.dinorpg.com/dino/2589066"
#~ LVL = 16

dino = ""
LVL = 0

race = "Pigmou"
competence = R_pigmou.COMPETENCE

NAME = "TOURNOI"
LVL_MAX = 14

LST_TODO = M_papy_joe.TODO + M_lanterne.TODO + M_shaman.TODO + M_elem.TODO + M_farm_tournoi.TODO

#########################################################

cookie = {"sid": sid}

def achat_dino():
	soup_url1 = BeautifulSoup(requests.get("http://www.dinorpg.com/shop/dinoz", cookies=cookie).text, 'html.parser')
	choix = soup_url1.find_all("a", {"class": "button bSmall"})[1]['href']
	if race != "" :	
		i = 0
		for a in soup_url1.find_all("div", {"class": "race"}) :
			if str(a.getText())[7:-1] == race:
				choix = soup_url1.find_all("a", {"class": "button bSmall"})[i]['href']
				break
			i +=1
	soup_url_dinoz = BeautifulSoup(requests.get("http://www.dinorpg.com"+choix, cookies=cookie).text, 'html.parser')
	dino = "http://www.dinorpg.com"+ str(soup_url_dinoz.find("form").get('action'))[:-5]
	soup_url_dinoz = BeautifulSoup(requests.post(dino+"/name",data={'name':NAME}, cookies=cookie).text, 'html.parser')
	url2 = "http://www.dinorpg.com/user/account?use_fast_map_move=on&use_no_popup=on&use_no_display_fight=on&use_fast_dialogs=on&use_smart_group=on&submitSettings=Valider"
	requests.get(url2, cookies=cookie)
	return dino
	
def lvl_up():
	url1 = dino+"/act/levelup?sk="+sk
	rep_url1 = requests.get(url1,cookies=cookie) 
	soup_url1 = BeautifulSoup(rep_url1.text, 'html.parser')
	choix = str(soup_url1.find_all("table", {"class" : "table select"})).split("document.location='")[1].split("sk=")[0]
	url2 = "http://www.dinorpg.com"+choix+"sk="+sk
	if "Feu" in soup_url1.find("div",{"class":"result"}).getText() and COMPETENCE[0] != competence[0]:
		url2 = dino+"/act/levelup?"+competence[0][len(COMPETENCE[0])]+";sk="+sk
		COMPETENCE[0].append(competence[0][len(COMPETENCE[0])])
	elif "Bois" in soup_url1.find("div",{"class":"result"}).getText() and COMPETENCE[1] != competence[1]:
		url2 = dino+"/act/levelup?"+competence[1][len(COMPETENCE[1])]+";sk="+sk
		COMPETENCE[1].append(competence[1][len(COMPETENCE[1])])
	elif "Eau" in soup_url1.find("div",{"class":"result"}).getText() and COMPETENCE[2] != competence[2]:
		url2 = dino+"/act/levelup?"+competence[2][len(COMPETENCE[2])]+";sk="+sk
		COMPETENCE[2].append(competence[2][len(COMPETENCE[2])])
	elif "Foudre" in soup_url1.find("div",{"class":"result"}).getText() and COMPETENCE[3] != competence[3]:
		url2 = dino+"/act/levelup?"+competence[3][len(COMPETENCE[3])]+";sk="+sk
		COMPETENCE[3].append(competence[3][len(COMPETENCE[3])])
	elif "Air" in soup_url1.find("div",{"class":"result"}).getText() and COMPETENCE[4] != competence[4]:
		url2 = dino+"/act/levelup?"+competence[4][len(COMPETENCE[4])]+";sk="+sk
		COMPETENCE[4].append(competence[4][len(COMPETENCE[4])])
	requests.get(url2,cookies=cookie) 	

def ressu():
	url1 = "http://www.dinorpg.com/shop?buy=1;sk="+sk
	requests.post(url1, data = {'oindex':'1','chk':sid,'qty':'1'}, cookies=cookie)	
	requests.get(dino+"/act/resurrect?sk="+sk, cookies=cookie)
	requests.get(dino+"/act/resurrect?angel=1;sk="+sk, cookies=cookie)
	requests.get(dino+"/act/stop_heal?sk="+sk+";ajax=1", cookies=cookie)
	print("!!")
	soins()

def soins():	
	url2 = "http://www.dinorpg.com/shop?buy=1;sk="+sk
	requests.post(url2, data = {'oindex':'4','chk':sid,'qty':'1'}, cookies=cookie)	
	url1 = dino+"/inventory/471355880/use?sk="+sk
	requests.get(url1, cookies=cookie)

def verification():
	rep_dino = requests.get(dino, cookies=cookie)
	soup_dino = BeautifulSoup(rep_dino.text, 'html.parser')
	pv = str(soup_dino.find("div", {"class": "lifetext"}).getText()).split(" / ")
	xp = str(soup_dino.find("div", {"class": "xptext"}).getText()).split(" / ")
	mort_ = 0
	lvl_ = 0
	if int(pv[0]) < int(int(pv[1])/3) :
		soins()
	if int(pv[0]) == 0 :
		ressu()
		mort_ = 2
	if int(xp[0]) >= int(xp[1]):
		lvl_up()
		lvl_ = 1
	return mort_ , lvl_

def combattre(url):
	requests.get(dino+url, cookies=cookie)

############################################################################# Programme

sk = str(BeautifulSoup(requests.get("http://www.dinorpg.com/shop", cookies=cookie).text, 'html.parser').find("form",{"id": "form_0"}).get('action'))[-5:]

#~ while True :
if True:
	COMPETENCE = [[],[],[],[],[]]
	if LVL == 0 :
		dino = achat_dino()
		LVL += 1			
	T = time.time()
	while LVL < LVL_MAX : 
		try:
			combattre("/act/fight?sk="+sk)
			a,b = verification()
			LVL += b
		except:
			time.sleep(1)
	i=0
	while i < len(LST_TODO) : 
		try:
			combattre(LST_TODO[i].replace("XXXXXXX",sk))
			if LST_TODO[i][5:11] != "dialog":
				a,b = verification()
				if "tournament" not in LST_TODO[i] :
					i -= a
		except:
			i -= 1
			time.sleep(1)
		i += 1
	print(datetime.timedelta(seconds=int(time.time() - T)))
	LVL = 0

