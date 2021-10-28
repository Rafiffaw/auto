import os
from os import name
import telegram
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import schedule
import datetime
now = datetime.datetime.now()
now = now.strftime("%a")
i = 1


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


usernameStr = "0078904560"
passwordStr = "QC9ZDH"

browser.get('https://kbm.mtsn2ponorogo.sch.id/')
current_url = browser.current_url

username = browser.find_element_by_name('username')
username.send_keys(usernameStr)

password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_class_name('fa-sign-in')
signInButton.click()

lewatitmbl = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "introjs-skipbutton")))

lewatitmbl.click()

#VAR VAR VAR VAR VAR VAR VAR VAR VAR VAR VAR

def notify(message):
    token = '1959542063:AAGCe7w-2TGCZ_P3ZJPX-NbhB-EERllFSFY'
    chat_id = 1767730053
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)

def tele(name):
	sleep(2)
	url = browser.current_url
	cookies = {
    'PHPSESSID': 'ukcat1ebdkqm6dddn7arp3f353',
    'elmaData': 'UmdCMEt2TGp2RnN4aDZ4cDkreFpZZzIvSFlCZVFkWFY2RXhsdEQ4WmFwVmtDRENYbkU4YTBlY0V5MTdGdEZxSjNranMyVi9xQzBWTlV1UEJ2WjlZMVdnUDFoamtGZG1mdy9xbHFyekFvcURzK1JDVFRQbWFJcXA5ZXFYYW5wKzVBaURUU1JjaEFzOEczUjdFdkRwYmhnNlhZWmwvbHhqMkZtdWhlNXVRY09HRkdPcUs2VlpqUG1uTDVqMHhtbWR5dDZ1SndFZTJTSGE2ZDNnK0I3R3dtS2pTbTIyZ0cycUY5NEx5enpzOExGdz06VEhaNE0xTndjV2cyYkZKbFpsWktTdz09',
	}

	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Connection': 'keep-alive',
	}

	response = requests.get(url, headers=headers, cookies=cookies)
	soup = BeautifulSoup(response.content, 'lxml')
	jobs = soup.find_all('div', class_ = 'posty')
	for job in jobs:
		wkt = job.find('div', class_ = 'usy-dt').span.text
		if 'Jam' in wkt:
			isi = job.find('div', class_ = 'job_descp').text
			notify('Timeline Mata Pelajaran ' + name + isi)

def do():
	
	bkba = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'BAHAN AJAR')))
	bkba.click()
	
	bkab = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'REKAP KEHADIRAN ANDA')))
	bkab.click()

	frm = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'FORUM MADRASAH')))
	frm.click()

def work(name):
	tele(name)
	do()

def mnbk(name): 
	name = 'BK\n'
	bk = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP BIMBINGAN KONSELING')))
	bk.click()
	
	work(name) 

def mnipa(name):
	name = 'IPA\n'
	ipa = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K IPA BU MUNTIK')))
	ipa.click()
	
	work(name)

def mnmtk(name):
	name = 'MTK\n'
	mtk = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP - MATHEMATICS')))
	mtk.click()
	
	work(name)

def mnips(name):
	name = 'IPS\n'
	ips = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP- IPS')))
	ips.click()
	
	work(name)

def mnpkn(name):
	name = 'PKN\n'
	pkn = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-PPKn')))
	pkn.click()
	
	work(name)

def mnakd(name):
	name = 'Akidah\n'
	akidah = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K AKIDAH AKHLAK')))
	akidah.click()
	
	work(name)

def mnski(name):
	name = 'SKI\n'
	ski = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-SKI')))
	ski.click()
	
	work(name)
	
def mnind(name):
	name = 'B. Indonesia\n'
	ind = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K(ICP)-BAHASA INDONESIA')))
	ind.click()

	work(name)

def mnpjok(name):
	name = 'PJOK\n'
	pjok = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K-PJOK')))
	pjok.click()

	work(name)

def mnqdt(name):
	name = 'Qurdist\n'
	qdt = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-QURDITS')))
	qdt.click()

	work(name)

def mnpka(name):
	name = 'Prakarya\n'
	pka = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP PRAKARYA')))
	pka.click()

	work(name)

def mnbtq(name):
	name = 'BTQ\n'
	btq = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K BTQ')))
	btq.click()

	work(name)

def mnarb(name):
	name = 'B. Arab\n'
	arb = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K bahasa arab')))
	arb.click()

	work(name)

def mnjwa(name):
	name = 'B. Jawa\n'
	jwa = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K BHS JAWA')))
	jwa.click()

	work(name)

def mnsbk(name):
	name = 'SBK\n'
	sbk = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP-SBK')))
	sbk.click()

	work(name)

def mnfkh(name):
	name = 'Fikih\n'
	fkh = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8k icp')))
	fkh.click()

	work(name)

def mning(name):
	name = 'B. Inggris\n'
	ing = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.LINK_TEXT, '8K ICP Bhs Inggris')))
	ing.click()

	work(name)

	

#JADWAL JADWAL JADWAL JADWAL JADWAL JADWAL JADWAL


def senin(name):
	print('senin')
	mnbk(name)
	mnakd(name)
	mnbtq(name)
	mnind(name)
	mnarb(name)
	mnipa(name)

def selasa(name):
	print('selasa')
	mnbk(name)
	mnqdt(name)
	mnips(name)
	mnsbk(name)
	mnski(name)
	mning(name)

def rabu(name):
	print('rabu')
	mnbk(name)
	mnpkn(name)
	mnipa(name)
	mnmtk(name)
	mnjwa(name)
	mnind(name)

def kamis(name):
	print('kamis')
	mnbk(name)
	mnmtk(name)
	mnsbk(name)
	mnipa(name)
	mnarb(name)
	mnpka(name)

def jumat(name):
	print('jumat')
	mnbk(name)
	mnpjok(name)
	mnfkh(name)
	mnips(name)
	mnpkn(name)

def sabtu(name):
	print('sabtu')
	mnbk(name)
	mnmtk(name)
	mnpjok(name)
	mnind(name)
	mning(name)


schedule.every().monday.at("12:00").do(senin,name)
schedule.every().tuesday.at("12:00").do(selasa,name)
schedule.every().wednesday.at("12:00").do(rabu,name)
schedule.every().thursday.at("12:00").do(kamis,name)
schedule.every().friday.at("12:00").do(jumat,name)
schedule.every().saturday.at("12:00").do(sabtu,name)

while i==1:
	schedule.run_pending()
	sleep(1)
