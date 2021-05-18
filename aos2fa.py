#All libraries
#import requests

import requests
import cv2 as cv
import numpy as np
import time
import serial
from PIL import ImageGrab,Image
#https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html?fbclid=IwAR2ljBHB4fnNir3_bZ7IHQIEc8YpQV1Hs4Rkxw0JQpve1fdRo4hn9_wKfOk
port = serial.Serial("COM3")
#-----------

#Telegram ile bağlantı
def send_msg(text):
	token = "" #your token
	chat_id = "" #your id

	url_req = "https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chat_id+"&text="+text
	results = requests.get(url_req)
	#return results.json()


#All funcs
#Mouse ile ilgili--
def koordinata_cevir(x,y):  #İçine koyulan x ve y değerlerini ör: x=50,y=100  00500100 haline çevirir
	x_kor = str(x)
	y_kor = str(y)
	if(len(x_kor) < 4):
		while(4!=len(x_kor)):
			x_kor = '0'+x_kor
	else:
		pass
	if(len(y_kor) < 4):
		while(4!=len(y_kor)):
			y_kor = '0'+y_kor
	else:
		pass
	return str(x_kor)+str(y_kor)
def koordinat_gonder(x,y,bekle):
	port.write(koordinata_cevir(x,y).encode('utf-8'))
	time.sleep(bekle)

def kolon_sec(x):
	#img = cv.imread("C:/Users/gold/Desktop/bo.jpg",0)
	im = ImageGrab.grab()
	img = cv.cvtColor(np.array(im), cv.COLOR_RGB2GRAY)

	img2 = img.copy()

	template = cv.imread('/carpi'+str(x)+'.jpg',0)
	# All the 6 methods for comparison in a list

	img = img2.copy()
	method = eval('cv.TM_CCOEFF_NORMED')
	# Apply template Matching
	res = cv.matchTemplate(img,template,method)
	min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
	port.write(koordinata_cevir(max_loc[0],max_loc[1]).encode('utf-8'))
#---------------------------


#Klavye ile ilgili------
tus_1 = "-1"
tus_2 = "-2"
vurma_List = ["-3","-4","-5","-6"]
combo_baslat = "-7"
#ilk üç buff basıldığı an oto saldırıyor
tus_8 = "-8" # art of fiercennes
tus_9 = "-9" # intense blade
tus_10 = "-10" # TUŞ 0 fury potion
tus_11 = "-11" # TUŞ - hp potion
tus_12 = "-12" # TUŞ = Knucklet A
yalap_salap ="-13"
sagtik = "-14"
esc = "-15"
bak = "-16"
# "-17" "-18" "-19" "-20" doludur
alt_e1 = "-29" #F3 ATACK
alt_0 = "-28" # F4 BM2
alt_1 = "-21" # F5 Crit dmg +%20 buf
alt_2 = "-22" # F6 Regeneration
alt_3 = "-23" # F7 BOŞ
alt_4 = "-24" # F8 field of fear tek rakibe saldırı buff ı
alt_5 = "-25" # BM3

dgden_cik = "-33"
muhtemel_Yer = "-34"
dg_giris = "-35"
oldumu_tikla = "-38"
#---------------
#Canavar plağı koordinatları--- RGB değerleri bilgisayarlarda farklılık gösterecek
plakkor= (570,13,571,14) #can barı plağı
dtkor= (555,16,556,17) #can barı dolumu boşmu
canazrgb = (581,16,582,17)
canavardahaazrgb = (565,16,566,17)
spbarrgb = (154,39,155,40)
hpbarrgb = (175,23,176,24)
golemrgb = (487,23,488,24) #golem 1
golemcanazrgb = (788,23,789,24) # golem2
bm2_canvarmirgb = (397,25,398,26) #bm2 varken cani varmi
dgekranisecilimi = (501,299,502,300)
karakter_yattimi = (554,472,555,473)
mavialev_kapi = (654,25,655,26)
#-------------
def ssalmak():
	global r,g,b,r1,g1,b1,r3,g3,b3,r4,g4,b4,r5,g5,b5,r6,g6,b6,r7,g7,b7,r8,g8,b8,r9,g9,b9,r10,g10,b10,r11,g11,b11,r12,g12,b12
	plimage = ImageGrab.grab(plakkor)
	r, g, b = plimage.getpixel((0, 0))
	#print(r,g,b)
	dtimage = ImageGrab.grab(dtkor)
	r1, g1, b1 = dtimage.getpixel((0, 0))
	#print("1inciler",r1,g1,b1)
	canazimage = ImageGrab.grab(canazrgb)
	r3, g3, b3 = canazimage.getpixel((0, 0))
	#print(r1,g1,b1)
	candahaazimage = ImageGrab.grab(canavardahaazrgb)
	r4, g4, b4 = candahaazimage.getpixel((0, 0))
	#print(r1,g1,b1)	
	spimage = ImageGrab.grab(spbarrgb)
	r5, g5, b5 = spimage.getpixel((0, 0))
	#print("sp icin",r5,g5,b5)	
	hpimage = ImageGrab.grab(hpbarrgb)
	r6, g6, b6 = hpimage.getpixel((0, 0))
	#print(r1,g1,b1)
	golemimage = ImageGrab.grab(golemrgb)
	r7, g7, b7 = golemimage.getpixel((0, 0))
	#print(r1,g1,b1)		
	golemcanazimage= ImageGrab.grab(golemcanazrgb)
	r8, g8, b8 = golemcanazimage.getpixel((0, 0))

	bm2canvarmiimage= ImageGrab.grab(bm2_canvarmirgb)
	r9, g9, b9 = bm2canvarmiimage.getpixel((0, 0))
	
	dgekranisecilimiimg= ImageGrab.grab(dgekranisecilimi)
	r10, g10, b10 = dgekranisecilimiimg.getpixel((0, 0))
	#print("rgb10lar :",r10,g10,b10)

	karakter_yattimiimg= ImageGrab.grab(karakter_yattimi)
	r11, g11, b11 = karakter_yattimiimg.getpixel((0, 0))
	#print("rgb11lar :",r11,g11,b11)

	mavialev_kapiimg= ImageGrab.grab(mavialev_kapi)
	r12, g12, b12 = mavialev_kapiimg.getpixel((0, 0))
	#print("rgb11lar :",r12,g12,b12)
#---------------------------

#Mouse ile kolonlara seçip tıklama func

def Kolon_tiklatma():
	time.sleep(1)
	kolon_sec(1)
	time.sleep(1)
	kolon_sec(2)
	
#------------
def tikla_bas(x,bekle):
	port.write(x.encode('utf-8'))
	time.sleep(bekle)


#MAİN FUNCS
combo_basdelay = 1.2 #1.31

combo_delaylist1 = [1.42,1.59,1.97,1.84]


combo_delaylist15 = [1.4,1.58,2.95,1.82]


combo_delaylist2 = [1.42,1.59,1.97,1.84]

combo_delaylist25 = [1.4,1.58,2.95,1.82]

def combo_ilkon(x,y):
	for i in range(x,y):

		ssalmak()
		if ((r and g and b)==172 and (r1==239 and g1==208 and b1==139)):
			if ((r and g and b)==172 and (r1==239 and g1==208 and b1==139) and (66<(r3 and g3 and b3)<74)):
				port.write(str(int(vurma_List[i])+int("-14")).encode('utf-8'))
				time.sleep(combo_delaylist15[i])
			else:
				port.write(vurma_List[i].encode('utf-8'))
				time.sleep(combo_delaylist1[i])
		elif(((r and g and b)==172 and (r1==239 and g1==208 and b1==139)) == False):
			return iki_Kolon_Bolgesi()
		else:
			pass

def combo_sonon(x,y):
	for i in range(x,y):

		ssalmak()
		if ((r and g and b)==172 and (r1==239 and g1==208 and b1==139)):
			if((r and g and b)==172 and (r1==239 and g1==208 and b1==139) and (66<(r3 and g3 and b3)<74)):
				port.write(str(int(vurma_List[i])+int("-14")).encode('utf-8'))
				time.sleep(combo_delaylist25[i])
			else:
				port.write(vurma_List[i].encode('utf-8'))
				time.sleep(combo_delaylist2[i])	
		elif(((r and g and b)==172 and (r1==239 and g1==208 and b1==139)) == False):
			return iki_Kolon_Bolgesi()
		else:
			pass	
def combo_ilkon_part2(x,y):
	for i in range(x,y):

		ssalmak()
		if ((r and g and b)==172 and (r1==239 and g1==208 and b1==139)):
			if ((r and g and b)==172 and (r1==239 and g1==208 and b1==139) and (66<(r3 and g3 and b3)<74)):
				port.write(str(int(vurma_List[i])+int("-14")).encode('utf-8'))
				time.sleep(combo_delaylist15[i])
			else:
				port.write(vurma_List[i].encode('utf-8'))
				time.sleep(combo_delaylist1[i])
		elif(((r and g and b)==172 and (r1==239 and g1==208 and b1==139)) == False):
			break
		else:
			pass

def combo_sonon_part2(x,y):
	for i in range(x,y):

		ssalmak()
		if ((r and g and b)==172 and ((229<r1<250) and (205<g1<215) and (145<b1<155))):
			if(((r and g and b)==172 and (r1==239 and g1==208 and b1==139)) and (66<(r3 and g3 and b3)<74)):
				port.write(str(int(vurma_List[i])+int("-14")).encode('utf-8'))
				time.sleep(combo_delaylist25[i])
			else:
				port.write(vurma_List[i].encode('utf-8'))
				time.sleep(combo_delaylist2[i])	
		elif(((r and g and b)==172 and (r1==239 and g1==208 and b1==139)) == False):
			break
		else:
			pass					
					
#----------------------------------------------------------------			

def iki_Kolon_Bolgesi():
	global bufdelay1,bufdelay2,bufdelayalt1,bufdelayalt2,kilit,ikikule_limit

	port.write(bak.encode('utf-8'))
	time.sleep(1.1)

	ikikule_limit+=1
	ssalmak()
	
	if((r5 and g5 and b5)==95):
		time.sleep(1.2)				
		port.write(tus_10.encode('utf-8'))
		#print("sp bastı")
		time.sleep(1.2)
	#print("sp rgbsi",r5,g5,b5)
	
	if((r6 and g6 and b6)==76):
		time.sleep(1.5)				
		port.write(tus_11.encode('utf-8'))
		print("hp bastı")
		#time.sleep(1.2)
	#print("sp",r5,g5,b5,"----hp",r6,g6,b6)
	while((r and g and b)==172 and (r1==239 and g1==208 and b1==139)): #plağı var canı var
		ikikule_limit = 0

		if((r and g and b)==172 and (r1==239 and g1==208 and b1==139) and (66<(r4 and g4 and b4)<74)):
			pass
		else:

			if(((time.time()-bufdelayalt2)/120)>0.99):  # art of sniping 120snde bir
				time.sleep(1.2)			
				port.write(alt_1.encode('utf-8'))
				bufdelayalt2 = time.time()	
				print("art of sniping")
				time.sleep(3.5)
			port.write(alt_2.encode('utf-8'))
			#print("hp skili bastı")
			time.sleep(1.4)

			port.write(combo_baslat.encode('utf-8'))
			time.sleep(combo_basdelay)

		combo_ilkon(0,4)
		combo_ilkon(0,4)
		combo_ilkon(0,1)
		combo_sonon(1,4)
		combo_sonon(0,4)
		combo_sonon(0,4)
		combo_sonon(0,2)
		if((r and g and b)==172):
			time.sleep(0.5)
			port.write(esc.encode('utf-8'))			
	if((r and g and b)==172 and (r1==239 and g1==208 and b1==139)==False):
		pass

	elif((r and g and b)!=172 and (r1!=239 and g1!=208 and b1!=139)):
		ikikule_limit+=2
		if((r11==123) and (g11==27) and (b11==159)):
			time.sleep(3)
			print("Okçu yattı!")
			send_msg("Okçu yattı!")
			port.write(oldumu_tikla.encode('utf-8'))
			time.sleep(1)
			olursepart_2()

		elif(time.time()-dg_bitis_zaman>dgde_gececekzaman):
			kilit = True
			print("KİLİT ÇALIŞTI")
					
		else:
			if(((time.time()-bufdelayalt1)/450)>0.99):  # buf 1 ve 2 aslnda 1400 snde bir
				time.sleep(1)				
				port.write(tus_8.encode('utf-8'))
				time.sleep(1.2)				
				port.write(tus_9.encode('utf-8'))
				time.sleep(1.2)
				print("buf 1 ve 2 çalıştı")
				port.write(alt_3.encode('utf-8'))
				bufdelayalt1 = time.time()
				time.sleep(1)
			Kolon_tiklatma()
			time.sleep(7)
			port.write(tus_11.encode('utf-8'))
			#print("hp bastı")
			time.sleep(1.2)	
			port.write(alt_2.encode('utf-8'))
			print("hp skili bastı")
			time.sleep(1.7)			

	else:
		pass
	
def mushid_Bolgesi():

	global bufdelay1,bufdelay2,bufdelayalt1,bufdelayalt2,mushid_limit
	port.write(bak.encode('utf-8'))
	time.sleep(1)
	ssalmak()

	mushid_limit+=1


	if((r5 and g5 and b5)==95):
		time.sleep(1.2)				
		port.write(tus_10.encode('utf-8'))
		print("sp bastı")
		time.sleep(1.2)
		print("sp",r5,g5,b5)
	if((r6 and g6 and b6)==76):
		time.sleep(1.5)				
		port.write(tus_11.encode('utf-8'))
		print("hp bastı")
		time.sleep(1.2)

	while((r and g and b)==172 and (r1==239 and g1==208 and b1==139)): #plağı var canı var
		mushid_limit = 0
		if((r and g and b)==172 and (r1==239 and g1==208 and b1==139) and (66<(r4 and g4 and b4)<74)):
			pass
		else:									
			port.write(combo_baslat.encode('utf-8'))
			time.sleep(combo_basdelay)
		print("buraya girdi")
		combo_ilkon_part2(0,4)
		combo_ilkon_part2(0,4)
		combo_ilkon_part2(0,1)
		combo_sonon_part2(1,4)
		combo_sonon_part2(0,4)
		combo_sonon_part2(0,4)
		combo_sonon_part2(0,2)


		
def part_1():
	port.write(dg_giris.encode('utf-8')) # SİENA 1 YERİNE 2 Yİ SEÇTİN ve entera tıkladın
	time.sleep(5)



def part_2():
	global mushid_limit,dg_bitis_zaman
	#Golemlere İlerle
	time.sleep(3)

	#***************************************
	port.write("-26".encode('utf-8'))
	time.sleep(29) # hesaba göre 25.25
	#***************************************




	#BURADA 40 SANİYE SAVAŞIR SONRA DİĞER KAPIYA GİDER--------
	mushid_limit = 0
	mushid_zaman = time.time()
	while(True):
		if(time.time()-mushid_zaman>60):
			print("bu if  çalıştı")
			print(time.time()-mushid_zaman)
			if((r and g and b)==172):
				time.sleep(0.9)
				port.write(esc.encode('utf-8'))
				time.sleep(0.9)
			break
		else:	
			mushid_Bolgesi()
			if(mushid_limit>20):
				time.sleep(1)
				part_4()
				part_1()
				dg_bitis_zaman = time.time()
				part_2()
				return 0
		time.sleep(0.85)

	

	#***************************************
	port.write("-27".encode('utf-8'))
	time.sleep(16) # hesaba göre 12.5
	#***************************************


	#-28 DOLU

	#-29 DOLU
	#YENİ PROJE BURDAN BAŞLIYOR



	port.write(alt_0.encode('utf-8'))#  bm2 açıyoruz
	bm2vakti = time.time()
	ssalmak()
	time.sleep(1)
	iki_golem_limit = 0
	while(((r7 and g7 and b7 and r8 and b8 and g8)==224)==False):
		if((r11==123) and (g11==27) and (b11==159)):
			time.sleep(3)
			print("Okçu yattı!")
			port.write(oldumu_tikla.encode('utf-8'))
			time.sleep(1)
			olursepart_2(1)
			return 0
		port.write(bak.encode('utf-8'))
		time.sleep(1)
		ssalmak()
		iki_golem_limit+=1
		if(iki_golem_limit>20):
			time.sleep(1)
			part_4()
			part_1()
			dg_bitis_zaman = time.time()
			part_2()
			return 0

	while(((r7 and g7 and b7)==224) or ((r8 and b8 and g8)==224)):
		port.write(alt_e1.encode('utf-8'))
		time.sleep(1)
		ssalmak()
		

	#***************************************
	port.write("-30".encode('utf-8'))
	time.sleep(14) # hesaba göre 10.75
	#***************************************


	
	time.sleep(1.5)
	port.write(bak.encode('utf-8'))
	time.sleep(1)
	ssalmak()

	while(r9==232 and g9==161 and b9==0): #barikata ölümüne vuruyoruz
		#port.write(vurma_List[0].encode('utf-8'))
		port.write(alt_e1.encode('utf-8'))
		time.sleep(1)  
		ssalmak()

	time.sleep(3)
	port.write(bak.encode('utf-8'))
	time.sleep(2)
	ssalmak()
	time.sleep(1)
	port.write(alt_1.encode('utf-8'))
	time.sleep(1.3)
	port.write(alt_4.encode('utf-8'))
	time.sleep(1.3)
	while((r1==239 and g1==208 and b1==139) or (r9==232 and g9==161 and b9==0) or (time.time()-bm2vakti<110)): #boss a  ölene kadar vuruyoruz
		if(time.time()-bm2vakti>90):
			time.sleep(1)
			port.write(vurma_List[0].encode('utf-8'))

		else:	
			port.write(alt_e1.encode('utf-8'))
		time.sleep(1.5)  
		ssalmak()
		time.sleep(1)
		port.write(bak.encode('utf-8'))
		time.sleep(1)
	

	#***************************************
	port.write("-31".encode('utf-8'))
	time.sleep(27) # hesaba göre 23 
	#***************************************

	time.sleep(1)
	port.write(bak.encode('utf-8'))
	time.sleep(2)
	ssalmak()
	time.sleep(1)
	port.write(alt_2.encode('utf-8'))
	print("hp skili bastı")
	time.sleep(1.2)	
	if(r12==235 and g12==235 and b12==235):
		while(r1==239 and g1==208 and b1==139): #kapiya  ölene kadar vuruyoruz
			port.write(vurma_List[0].encode('utf-8'))
			time.sleep(1)	
			ssalmak()


		


	#***************************************
	port.write("-32".encode('utf-8'))
	time.sleep(10) # hesaba göre 7
	#**************************************

def olursepart_2(x=0):
	global mushid_limit,dg_bitis_zaman
	#Golemlere İlerle
	time.sleep(3)

	#***************************************
	port.write("-36".encode('utf-8'))
	time.sleep(27) # hesaba göre 25.25
	#***************************************

	#BURADA 40 SANİYE SAVAŞIR SONRA DİĞER KAPIYA GİDER--------
	if(i==1):
		mushid_limit = 0
		mushid_zaman = time.time()
		while(True):
			if(time.time()-mushid_zaman>60):
				print("bu if  çalıştı")
				print(time.time()-mushid_zaman)
				if((r and g and b)==172):
					time.sleep(0.9)
					port.write(esc.encode('utf-8'))
					time.sleep(0.9)
				break
			else:	
				mushid_Bolgesi()
				if(mushid_limit>20):
					time.sleep(1)
					part_4()
					part_1()
					dg_bitis_zaman = time.time()
					part_2()
					return 0
			time.sleep(0.85)
	#***************************************
	port.write("-27".encode('utf-8'))
	time.sleep(16) # hesaba göre 12.5
	#***************************************


	#-28 DOLU

	#-29 DOLU
	#YENİ PROJE BURDAN BAŞLIYOR



	port.write(alt_0.encode('utf-8'))#  bm2 açıyoruz
	bm2vakti = time.time()
	ssalmak()
	time.sleep(1)
	iki_golem_limit = 0
	while(((r7 and g7 and b7 and r8 and b8 and g8)==224)==False):
		if((r11==123) and (g11==27) and (b11==159)):
			time.sleep(3)
			print("Okçu yattı!")
			time.sleep(1)
			port.write(oldumu_tikla.encode('utf-8'))
			time.sleep(1)
			olursepart_2()
			return 0
		port.write(bak.encode('utf-8'))
		time.sleep(1)
		ssalmak()
		iki_golem_limit+=1
		if(iki_golem_limit>20):
			time.sleep(1)
			part_4()
			part_1()
			dg_bitis_zaman = time.time()
			part_2()
			return 0


	while(((r7 and g7 and b7)==224) or ((r8 and b8 and g8)==224)):
		port.write(alt_e1.encode('utf-8'))
		time.sleep(1)
		ssalmak()
		

	#***************************************
	port.write("-30".encode('utf-8'))
	time.sleep(14) # hesaba göre 10.75
	#***************************************

	if(x==1):
		time.sleep(1.5)
		port.write(bak.encode('utf-8'))
		time.sleep(1)
		ssalmak()

		while(r9==232 and g9==161 and b9==0): #barikata ölümüne vuruyoruz
			#port.write(vurma_List[0].encode('utf-8'))
			port.write(alt_e1.encode('utf-8'))
			time.sleep(1)  
			ssalmak()

		time.sleep(3)
		port.write(bak.encode('utf-8'))
		time.sleep(2)
		ssalmak()
		time.sleep(1)
		port.write(alt_1.encode('utf-8'))
		time.sleep(1.3)
		port.write(alt_4.encode('utf-8'))
		time.sleep(1.3)
		while((r1==239 and g1==208 and b1==139) or (r9==232 and g9==161 and b9==0) or (time.time()-bm2vakti<110)): #boss a  ölene kadar vuruyoruz
			if(time.time()-bm2vakti>90):
				time.sleep(1)
				port.write(vurma_List[0].encode('utf-8'))

			else:	
				port.write(alt_e1.encode('utf-8'))
			time.sleep(1.5)  
			ssalmak()
			time.sleep(1)
			port.write(bak.encode('utf-8'))
			time.sleep(1)


	if(x==1):
		#***************************************
		port.write("-31".encode('utf-8'))
		time.sleep(27) # hesaba göre 23 
		#***************************************
	else:
		#***************************************
		port.write("-37".encode('utf-8'))
		time.sleep(21) # hesaba göre .. 
		#***************************************
	time.sleep(1)
	port.write(bak.encode('utf-8'))
	time.sleep(2)
	ssalmak()
	time.sleep(1)
	port.write(alt_2.encode('utf-8'))
	print("hp skili bastı")
	time.sleep(1.2)	
	if(r12==235 and g12==235 and b12==235):
		while(r1==239 and g1==208 and b1==139): #kapiya  ölene kadar vuruyoruz
			port.write(vurma_List[0].encode('utf-8'))
			time.sleep(1)	
			ssalmak()

	#***************************************
	port.write("-32".encode('utf-8'))
	time.sleep(10) # hesaba göre 7
	#**************************************

def part_4():
	global bufdelayalt1
	print("PART 4 UYGULANDI")
	port.write(dgden_cik.encode('utf-8'))
	send_msg("DG den çıkıldı! ",(4800-(time.time()-bufdelayalt1))/60," dakika boşta kaldı!")
	time.sleep(5)
	"""
	time.sleep(2)
	port.write(koordinata_cevir(1293,121).encode('utf-8')) # DGDEN ÇIKMAK İÇİN ÇARPI BUTONU
	time.sleep(2)
	port.write(koordinata_cevir(638,450).encode('utf-8')) # ÇIKIŞ İÇİN ENTER BUTONU
	"""
	time.sleep(4)
	port.write(muhtemel_Yer.encode('utf-8'))
	#port.write(koordinata_cevir(644,324).encode('utf-8')) # ÇIKTIĞINDA VARACAĞIN MUHTEMEL GİRİŞ YERİNE TIKLADIN
	time.sleep(2)
	ssalmak()
	time.sleep(1)
	zaman_siniri = time.time()
	while((r10 == 22 and g10 == 24 and b10 == 27)==False):
		port.write(vurma_List[0].encode('utf-8'))
		time.sleep(2)
		port.write(muhtemel_Yer.encode('utf-8')) # ÇIKTIĞINDA VARACAĞIN MUHTEMEL GİRİŞ YERİNE TIKLADIN
		time.sleep(2)
		ssalmak()
		time.sleep(1)
		if(time.time()-zaman_siniri>400):
			send_msg("Part_4 de giriş yeri bulunamadı oyundan çıkılıyor!(program kapandı)")
			quit()
		if((r11==123) and (g11==27) and (b11==159)):
			time.sleep(3)
			print("Okçu yattı!")
			port.write(oldumu_tikla.encode('utf-8'))
			send_msg("Part_4 deyken öldü oyundan çıkılıyor!(program kapandı)")
			quit()




"""
#------------
#MAİN
#------------
giris_miktar = 8
kilit = False
dgde_gececekzaman = 4100
for i in range(giris_miktar):
	

	#MEKANDASIN MAİN
	time.sleep(2)
	dg_bitis_zaman = time.time()
	bufdelay1,bufdelay2,bufdelayalt1,bufdelayalt2 = time.time(),time.time(),time.time(),time.time()

	ikikule_limit = 0
	while(True): # BURASI ÇOK ÖNEMLİ ******************************
		if(ikikule_limit>20):
			break
		elif(kilit==True):
			kilit = False
			break
		else:
			iki_Kolon_Bolgesi()
	print("3 BİTTİ")
	part_4()
	#part_1()
	#part_2()

send_msg("FOR DÖNGÜSÜ SONA ERDİ!(program kapandı)")
"""
bufdelayalt2 = time.time()
while(True):
	if(((time.time()-bufdelayalt2)/120)>0.99):  # art of sniping 120snde bir
		time.sleep(1.2)			
		port.write(alt_1.encode('utf-8'))
		bufdelayalt2 = time.time()	
		print("art of sniping")
		time.sleep(3.5)
	port.write(alt_2.encode('utf-8'))
	#print("hp skili bastı")
	time.sleep(1.4)

	port.write(combo_baslat.encode('utf-8'))
	time.sleep(combo_basdelay)

	combo_ilkon(0,4)
	combo_ilkon(0,4)
	combo_ilkon(0,1)
	combo_sonon(1,4)
	combo_sonon(0,4)
	combo_sonon(0,4)
	combo_sonon(0,2)
	time.sleep(1)