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
# db["pages"] = ["ech0by"]
# db["page_info"] = [""]
# db["edits"] = 0


while(1):
  clear()
  user = ""
  uinput = ""
  while uinput not in ["r", "l"]:
    uinput = input("~ ~ ~ ~ -  PyWiki - ~ ~ ~ ~\n"+str(len(db["usernames"])-1)+" users - "+str(len(db["pages"]))+" pages - "+str(db["edits"])+" edits\n\nType \"l\" for login and \"r\" for register\n")
    clear()
  if uinput == "r":
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
    clear()
    uinput = "s̷̡̟͈͕̯̘̙̙̣̼̰͔̫͍͖̻̱̜̗̹̰̩̒̎̀ͅ"
    while(uinput not in db["usernames"]):
      uinput = input("Username: ")
    user = uinput
    uinput = input("Password: ")
    if uinput != db["passwords"][db["usernames"].index(user)]:
      # # debug print password and user
      #print(uinput j+ " /// " + db["passwords"][db["usernames"].index(user)] + " /// " +user)
      quit()
    else:
      clear()
      print("Logged in as " + user)
      loggedUser = user
      userNum = db["usernames"].index(loggedUser)
  try:
    clear()
    print("Logged in as " + loggedUser+"\n\n")
    while(1):
      clear()
      uinput = input("~ ~ ~ ~ -  PyWiki - ~ ~ ~ ~\n"+str(len(db["usernames"])-1)+" users - "+str(len(db["pages"]))+" pages - "+str(db["edits"])+" edits\n\n1. Wiki Catalog\n")
      if uinput in ["1"]:
        if uinput == "1":
          clear()
          counter = 0
          for i in db["pages"]:
            print(str(counter)+". "+i)
            counter+=1
          input("Press [ENTER] to continue.")



  
  except:
    pass