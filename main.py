from replit import db
import random
import os
import math
import time

###

# Read the README.md
# MIT License

###

def sleep(seconds):
  time.sleep(seconds)


def clear():
  if os.name == 'posix':
      _ = os.system('clear')
  else:
  # for windows platfrom
    _ = os.system('cls')
    
###

# reset wiki
# db["usernames"] = [""]
# db["passwords"] = [""]
# db["pages"] = [""]
# db["page_info"] = [""]
# db["page_type"] = []
# db["edits"] = 1

###

# forever loop
while(1):
  # print login page
  clear()
  user = ""
  uinput = ""
  while uinput not in ["r", "l"]:
    uinput = input("~ ~ ~ ~ -  PyWiki - ~ ~ ~ ~\n"+str(len(db["usernames"])-1)+" users - "+str(len(db["pages"]))+" pages - "+str(db["edits"])+" edits\n\nType \"l\" for login and \"r\" for register\n")
    clear()
  # check input
  if uinput == "r":
    # account creation
    temp1 = ""
    while temp1 in db["usernames"]:
      clear()
      temp1 = input("Account Creation:\nUsername: ")
    temp2 = ""
    while len(temp2) < 3:
      clear()
      temp2 = input("Name available!\nEnter Password (min 3 chars)\n")
  
    db["usernames"].append(temp1)
    db["passwords"].append(temp2)
    db["notes"].append("")
    # print(str(db["usernames"]))
    # print(str(db["passwords"]))
    print("Registered!")
    uinput = ""
  
  if uinput == "l":
    # login
    clear()
    uinput = "s̷̡̟͈͕̯̘̙̙̣̼̰͔̫͍͖̻̱̜̗̹̰̩̒̎̀ͅ"
    while(uinput not in db["usernames"]):
      clear()
      uinput = input("Username: ")
    user = uinput
    uinput = input("Password: ")
    if uinput != db["passwords"][db["usernames"].index(user)]:
      quit()
    else:
      # logged in
      clear()
      print("Logged in as " + user)
      loggedUser = user
      userNum = db["usernames"].index(loggedUser)
  try:
    # announce login
    clear()
    print("Logged in as " + loggedUser+"\n\n")
    while(1):
      # main loop
      clear()
      # input/main menu
      uinput = input("~ ~ ~ ~ -  PyWiki - ~ ~ ~ ~\n"+str(len(db["usernames"])-1)+" users - "+str(len(db["pages"]))+" pages - "+str(db["edits"])+" edits\nType \"cancel\" at any time to return here.\n\n1. Wiki Catalog\n2. Open a page\n\n")
      if uinput in ["1", "2"]:
        # catalog
        if uinput == "1":
          clear()
          counter = 0
          for i in db["pages"]:
            print(str(counter)+". "+i)
            counter+=1
          input("Press [ENTER] to continue.\n")
        # open a page
        if uinput == "2":
          uinput = ""
          while uinput not in ["n","i","cancel"]:
            clear()
            uinput = input("Open from page name or id? (n/i)\n")

          if uinput == "n":
            uinput = ""
            while uinput not in db["pages"]:
              clear()
              uinput = input("Enter page name: ")
            id = db["pages"].index(uinput)
            
          if uinput != "cancel":
            clear()
            input(db["pages"][id]+"\n\n"+db["page_info"][id]+"\n\nPress [ENTER] to continue.")
            
          
          



  
  except:
    pass