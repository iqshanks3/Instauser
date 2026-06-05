import requests
from user_agent import generate_user_agent as elia
import random
import os
#_______
Z = '\033[1;31m'  # احمر
X = '\033[1;33m'  # اصفر
Z1 = '\033[2;31m'  # احمر ثاني
F = '\033[2;32m'  # اخضر
A = '\033[2;34m'  # ازرق
C = '\033[2;35m'  # وردي
B = '\033[2;36m'  # سماوي
Y = '\033[1;34m'  # ازرق فاتح
W = "\033[1;37m"  # White
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
P = '\x1b[1;97m'
J22='\x1b[38;5;209m'
C1='\x1b[38;5;120m'
#_____
hq = f""" {B}
{J22}▬▬▬{P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{F}▬▬{J22}shanks  {F}▬▬{P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22}▬▬▬

         ██╗ ███╗   ██╗ ███████╗ ████████╗  █████╗
         ██║ ████╗  ██║ ██╔════╝ ╚══██╔══╝ ██╔══██╗
         ██║ ██╔██╗ ██║ ███████╗    ██║    ███████║
         ██║ ██║╚██╗██║ ╚════██║    ██║    ██╔══██║
         ██║ ██║ ╚████║ ███████║    ██║    ██║  ██║
         ╚═╝ ╚═╝  ╚═══╝ ╚══════╝    ╚═╝    ╚═╝  ╚═╝
        {X}¸.•´¯`•.¸¸ {F} [꧁shanks ꧂ ]    {X}¸.•´¯`•.¸¸                       
              {F}TLE : @iqshanks12  /  @iqshanks12
    
 {J22}▬▬▬{P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{F}▬▬{J22} Instagram  {F}▬▬{P}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{J22}▬▬▬
"""
print(hq)
print(' \x1b[1;32m ادخل توكن بوتك')
tok = input('[shanks]\033[1;37m  𝑻𝑶𝑲𝑬𝑵 : ')
print(' \x1b[1;32m ادخل ايدي بوتك')
iid = input('\033[1;32m[shanks]\033[1;37m 𝑰𝑫 : ')
video_url = "https://t.me/XERTIsl/8"  
rd = requests.get(
    f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text='
    '┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉\n'
    '╮❲ تم تشغيل الاداة بنجاح ❳\n'
    '┤❲ سيتم ارسال الصيد الي بوتك ❳\n'
    '┤❲ المبرمج ❳ > shanks\n'
    '╯❲ حساباتي ❳ ⇣\n'
    'BY❲ @iqshanks12❳ 💬 ❲ @iqshanks12 ❳\n'
    '┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉'
)
os.system('clear')
good = 0
bad = 0
os.system('clear')
res = requests.get('https://www.instagram.com/api/graphql').cookies.get_dict()
elia1 = 'qwertyuioiplkjhgfdsamnbvcxz1234567890_'
def elia2(elia1,res):
	global tok,iid,good,bad
	while True:
			user = ''.join(random.choice(elia1) for _ in range(4))
			cookies = {
			    'csrftoken': res['csrftoken'] ,
			    'mid':res['mid'],
			}	
			headers = { 
			    'sec-fetch-site': 'same-origin',
			    'user-agent': str(elia()),
			    'x-csrftoken': res['csrftoken'],
			    'x-fb-lsd': 'AdRIz2UBeC7SaZ1axfMw2NQ9vLc',
			    'x-ig-app-id': '936619743392459',
			}			
			data = {
			    'lsd': 'AdRIz2UBeC7SaZ1axfMw2NQ9vLc',
			    'variables': f'{{"input":{{"field_name":"USERNAME","username":{{"sensitive_string_value":"{user}"}}}},"scale":2}}',
			    'doc_id': '25391252800555418',
			}			
			response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data).text
			if "SUCCESS" in response:
				good+=1
				os.system('clear')
				print(hq)
				print(f' {F} GOOD : {good} | {Z1} BAD : {bad} \n {P} Username : {user} ')
				ff = f"""
━────━shanks ━────━
🥷🏻𝒖𝒔𝒆𝒓𝒏𝒂𝒎𝒆: @{user}   
━────━shanks ━────━
﴾ py - @iqshanks12 • @iqshanks12  • ﴿    				
				"""
				requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={iid}&text={ff}')
			else:
				bad+=1
				os.system('clear')
				print(hq)
				print(f' {F} GOOD : {good} | {Z1} BAD : {bad} \n {P} Username : {user} ')	
elia2(elia1,res)		