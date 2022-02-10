import os,time
os.system('pkg install wget')
os.system('clear')
print('\033[1;33mwelcome ye my tools') 
logo = """\033[1;31m
  ____________________ 
     ║▒▒▒▒▒▒▒▒▒▒║
     ║▒▒▒▒▒▒▒▒▒▒║
     ║▒▒▒▒▒▒▒▒▒▒║
     ║▒▒▒▒▒▒▒▒▒▒║
     ║▒▒▒▒▒▒▒▒▒▒║
     ║▒▒▒▒▒▒▒▒▒▒║
    ╔════════════╗
    ╚════════════╝
     ║██████████╚╗
     ║██╔══╗█╔═╗█║
     ║██║╬╔╝█╚╗║█║
     ║██╚═╝█║█╚╝█║
     ╚╗█████████═╝
     ╚╗║╠╩╩╩╩╩╝
        ║║┈┈┈█▐█████▒.｡oO
        ║██╠╦╦╦╗
        ╚╗██████
           ╚════╝
       ╔═✦•ೋ°♤♤°ೋ•✦═╗
   \033[1;31mtermux dz ngrok install
​​       ╚═✦•ೋ°♤♤°ೋ•✦═╝"""
print(logo)
time.sleep(4)
os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz')
os.system('tar -xvzf ngrok-stable-linux-arm64.tgz ngrok')
os.system('mv ngrok $HOME')
os.system('chmod +x *')
os.system('xdg-open https://dashboard.ngrok.com/login')
print('\033[1;31mPlease enter the site, record and copy your feedback and put it here to run Ngirok ') 
os.system('exit') 