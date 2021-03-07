import os
from time import sleep
m='\033[1;31m';h='\033[1;32m';k='\033[1;33m';b='\033[1;34m';u='\033[1;35m';c='\033[1;36m';p='\033[1;37m';mb='\033[1;41m';n='\033[0m'

os.system('clear')
print(f'''
{m}•{k}•{h}•{b}________________________{h}•{k}•{m}•
{b}   |{mb} TERMUX KEY BY NAYARA {n}{b}|''')
sleep(4)
print(f'\n{b}({m}!{b}){h} Menambahkan Tombol...')
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
buka = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
buka.write(key)
buka.close()
sleep(2)
os.system('termux-reload-settings')
print(f'{b}({m}!{b}){u} Selesai...')
print(f'{b}({m}!{b}){u} Silahkan Reload Termux Anda...')
sleep(2)
print(f'{n}')
os.system('clear')
