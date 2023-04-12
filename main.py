#coding=utf-8
#!/usr/bin/env python3
import os,time,requests,getpass
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
api = "https://589389b5-1b60-4a6f-aef4-02a9fdba0df7.id.repl.co?"
def login():
    os.system("clear")
    print (logo)
    print("\n\x1b[1;91m  [\x1b[1;93m01\x1b[1;91m]\x1b[1;92mLOGIN\n\n\x1b[1;91m  [\x1b[1;93m02\x1b[1;91m]\x1b[1;92mSIGNUP\n\n\x1b[1;91m  [\x1b[1;93m02\x1b[1;91m]\x1b[1;92mEXIT")
    chooseOption = input("\n\x1b[1;92m CHOOSE AN OPTION:\x1b[1;93m ")
    if chooseOption== "00" or chooseOption=="0":
      os.system("clear")
      print(logo)
      os.sys.exit()
    elif chooseOption == "01" or chooseOption == "1":
      os.system("clear")
      print(logo)
      yuname = input("\n\x1b[1;92mEnter your username:\x1b[1;93m ")
      ypass = getpass.getpass("\n\x1b[1;92mEnter your password:\x1b[1;93m ")
      tid = requests.get(api+"login&u="+yuname+"&pass="+ypass)
      logdata=tid.json()
      if logdata["success"] == False :
        os.system("clear")
        print(logo)
        print(logdata["msg"])
        time.sleep(2)
        login()
      elif logdata["success"] == True :
        print(logo)
        logineffect()
        menu()
    elif chooseOption == "02" or chooseOption == "2":
      os.system("clear")
      print(logo)
      yuname = input("\n\x1b[1;92mEnter your username:\x1b[1;93m ")
      ypass = getpass.getpass("\n\x1b[1;92mEnter your password:\x1b[1;93m ")
      yname = input("\n\x1b[1;92mEnter your name:\x1b[1;93m ")
      ymail = input("\n\x1b[1;92mEnter your email address:\x1b[1;93m ")
      tid = requests.get(api+"signup&u="+yuname+"&pass="+ypass+"&n="+yname+"&m="+ymail)
      logdata=tid.json()
      if logdata['success'] == False :
        os.system("clear")
        print (logo)
        print("\n\x1b[1;91m"+logdata['msg'])
        time.sleep(2)
        login()
      elif logdata["success"] == True :
        os.system("clear")
        print(logo)
        logineffect()
        menu()
    else:
      os.system("clear")
      print (logo)
      input("\n\x1b[1;92mpress enter to contact admin: ")
      os.system("xdg-open https://fb.me/D3ADVAU")
      login()
### RUN ###
if __name__ == "__main__":
    login()
