#coding=utf-8
#!/usr/bin/env python3
import os,sys,time,requests,getpass
logo = """
    \x1b[1;92m$$$$$$$\  \x1b[1;96m$$\      \x1b[1;93m $$$$$$\  \x1b[1;94m $$$$$$\  
    \x1b[1;93m$$  __$$\ \x1b[1;94m$$ |     \x1b[1;92m$$  __$$\ \x1b[1;96m$$  __$$\ 
    \x1b[1;92m$$ |  $$ |\x1b[1;96m$$ |     \x1b[1;93m$$ /  $$ |\x1b[1;94m$$ /  \__|
    \x1b[1;93m$$ |  $$ |\x1b[1;94m$$ |     \x1b[1;92m$$ |  $$ |\x1b[1;96m$$ |$$$$\ 
    \x1b[1;92m$$ |  $$ |\x1b[1;96m$$ |     \x1b[1;93m$$ |  $$ |\x1b[1;94m$$ |\_$$ |
    \x1b[1;93m$$ |  $$ |\x1b[1;94m$$ |     \x1b[1;92m$$ |  $$ |\x1b[1;96m$$ |  $$ |
    \x1b[1;92m$$$$$$$  |\x1b[1;96m$$$$$$$$\ \x1b[1;93m$$$$$$  |\x1b[1;94m\$$$$$$  |
    \x1b[1;93m\_______/ \x1b[1;94m\________|\x1b[1;92m\______/ \x1b[1;96m \______/ 
\n \x1b[1;97m╔══════════════════════════════════════════╗
 ║\x1b[1;92m  Author\x1b[1;93m     :     Dead-Man | D3ADVAU    \x1b[1;97m ║
 ║\x1b[1;92m  Github \x1b[1;93m    :     github.com/D3ADVAU    \x1b[1;97m ║
 ║\x1b[1;92m  Facebook \x1b[1;93m  :       fb.com/D3ADVAU      \x1b[1;97m ║
 ╚══════════════════════════════════════════╝
"""
def logineffect():
  import time,sys,os,random
  colorrandom = ["\x1b[1;91m", "\x1b[1;92m", "\x1b[1;93m", "\x1b[1;94m", "\x1b[1;95m", "\x1b[1;96m"]
  animationlog = [random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"10% ", random.choice(colorrandom)+"  login in "+random.choice(colorrandom)+"20% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"30% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"40% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"50% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"60% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"70% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"80% ", random.choice(colorrandom)+"  Login in "+random.choice(colorrandom)+"90% ", random.choice(colorrandom)+"  Login in "+ random.choice(colorrandom)+"100% "]
  animation1 = [random.choice(colorrandom)+"[■□□□□□□□□□]",random.choice(colorrandom)+"[■■□□□□□□□□]",random.choice(colorrandom)+ "[■■■□□□□□□□]",random.choice(colorrandom)+ "[■■■■□□□□□□]", random.choice(colorrandom)+"[■■■■■□□□□□]", random.choice(colorrandom)+"[■■■■■■□□□□]", random.choice(colorrandom)+"[■■■■■■■□□□]", random.choice(colorrandom)+"[■■■■■■■■□□]", random.choice(colorrandom)+"[■■■■■■■■■□]", random.choice(colorrandom)+"[■■■■■■■■■■]"]
  os.system("clear")
  print (logo)
  for i in range(len(animationlog)):
    time.sleep(0.2)
    sys.stdout.write("  "+"\r" + animationlog[i % len(animationlog)])
    sys.stdout.write("" + animation1[i % len(animation1)])
    sys.stdout.flush()
  print("\n\x1b[1;97m")
def menu():
 os.system("clear")
 print(logo)
 print("\n\x1b[1;91m  [\x1b[1;93m01\x1b[1;91m]\x1b[1;92mCONTACT DEVOLOPER\n\n\x1b[1;91m  [\x1b[1;93m00\x1b[1;91m]\x1b[1;92mEXIT")
 chooseOption = input("\n\x1b[1;92m CHOOSE AN OPTION:\x1b[1;93m ")
 if chooseOption == "00" or chooseOption == "0":
  os.system("clear")
  print(logo)
  os.sys.exit()
 elif chooseOption == "1" or chooseOption == "01":
  os.system("clear")
  print(logo)
  os.system("xdg-open https://facebook.com/D3ADVAU")
  os.system("xdg-open https://facebook.com/D3ADVAU")
  menu()
 else:
  os.system("xdg-open https://facebook.com/D3ADVAU")
  print ("\x1b[1;92m[!] \x1b[1;96mFill in correctly")
  menu()
####login ####
apvl = requests.get("https://d3advau.ml/LOGIP").text
def main():
    os.system("clear")
    print (logo)
    print("\x1b[1;96m    TO LOGIN ENTER YOUR NAME AND PASSWORD")
    print("\x1b[1;96mOR IF YOU ARE NEW ENTER A NEW NAME AND PASSWORD")
    yname = input("\n\x1b[1;92mENTER YOUR NAME:\x1b[1;93m ")
    ypass = getpass.getpass("\n\x1b[1;92mENTER YOUR PASSWORD:\x1b[1;93m ")
    tid = requests.get("https://d3advau.ml/LOG-IP?name="+yname+"&pass="+ypass).text
    if tid in apvl:
        os.system("clear")
        print (logo)
        logineffect()
        menu()
    else:
      tid = requests.get("https://d3advau.ml/LOG-IP?name="+yname+"&pass="+ypass).text
      os.system("clear")
      print (logo)
      print("\x1b[1;92m YOUR ID : \x1b[1;96m"+tid)
      print("\n\x1b[1;92mSend Id code to admin for approve")
      ad = input("\n\x1b[1;92mpress enter to contact admin: ")
      os.system("xdg-open https://fb.me/D3ADVAU")
      main()
### RUN ###
if __name__ == "__main__":
    main()
