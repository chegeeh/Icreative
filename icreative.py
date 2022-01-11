import os
import sys
import sqlite3
import random
from random import randint
import socket
from datetime import *
import string
import re
import time
from PyDictionary import PyDictionary
import pyttsx3
import PyPDF2
from gtts import gTTS
from playsound import playsound
import instaloader


def dtime():   
         
         current_time = datetime.now()
         now = current_time.strftime("%H:%m:%S")
         date = current_time.strftime("%d/%m/%Y")
         
         
         print("\nDATE:" ,date)
         print("TIME:",now)
         
         
def MyCalc(num1, num2, oper):
      
     
      if oper == "+":
           result = num1 + num2
           print("\n[+]Result is: ",result)
           
      elif oper == "-":
           result = num1 - num2
           print("\n[+]Result is: ",result)

      elif oper == "/":
           result = num1 / num2
           print("\n[+]Result is: ",result)

      elif oper == "*":
           result = num1 * num2
           print("\n[+]Result is: ",result)
           

      
def rps(intro):     
    
         print("\n[+]You chose: " + intro)
         choses = ['R', 'P', 'S']
         opponent = random.choice(choses)
         print("\n[+]Comp chose: " + opponent)
         time.sleep(2)
         print("\n++++++ Rolling Dice ++++++")
         time.sleep(1.5)   
         print("\n[+]Predicting Outcome......")
         time.sleep(2)
           
         if opponent == str.upper(intro):
             print("\nTie")
         elif opponent == 'R' and intro.upper() == 'S':
             print("\n[[Scissors beats rock, comp wins!]]\n")
                 
         elif opponent == 'S' and intro.upper() == 'P':
             print("\n[[Scissors beats paper, Comp wins!]]\n")
            
         elif opponent == 'P' and intro.upper() == 'R':
             print("\n[[Paper beats rock, Comp wins!]]\n")
            
         else:
             print("\n[[You win!]]\n")
         
          
           
def pwmgr(numinput, app, length):
    
     password = string.ascii_letters+string.digits+string.punctuation
    
     for pwd in range(numinput):
         pw = ""
     for c in range(length):
         pw += random.choice(password)
     
     print("\n")
     print("  +" * 20) 
     print("   [+]Generated", app, "Password:","[",pw,"]")        
     print("  +" * 20)
     print("")
     time.sleep(1)
     
     sav = input("[+]Save the password (Y)es/(N)o: ") 
     if sav == "Y" or "y":
         f = open('password.txt', 'a')
         f.write(app+":" +pw)
         f.close()

     print("")
     print("  +" * 20) 
     print("  [+] Generated", app, "Password saved in password.txt")        
     print("  +" * 20, "\n")
     
def youdl(url):     
     yt = YouTube(url)
     print("[*] Downloading....")
     ys.download()
     print("[*] Download Successful!")





print("\n")
print("    ****"*10)
print("                          [         ICreaTive Co.        ]")
print("    ****"*10)

password = "pass" or ""

print("\n                                    *login first ")
print("                                   ---------------")
login = input("                                         ")
tout = 3

while login != password:
    login = input("\n * WARNING! * \n ------------\n[!]login failed!\n[!]Try Again\n:")
    time.sleep(1)
    tout -=1
    
    if tout == 0:
       sys.exit()
    elif password == "q":
        sys.exit()

while True:	
   print("\n Welcome to...\n")
   print("  **"*7)
   print("           THE HUB")
   print("  **"*7)
   dtime()
   print("\nLoading, please wait....")
   time.sleep(3)
   print("\n=================")
   print(   "PROGRAMMES:"   )
   print("=================")
   print("[a] = MyCalc")
   print("[b] = Rock, Paper, Scissors")
   print("[c] = Friendly Cow")
   print("[d] = Password Manager") 
   print("[e] = YouTube Downloader")
   print("[f] = Instagram Pic Downloader")
   print("[g] = Personal Dictionary")
   print("[h] = Video-Audio Converter")
   print("[i] = Text-audio Converter")
   print("[j] = Mirror! Mirror!")
   print("[k] = iBrowser")
   print("[l] = Quiz Show")
   print("[q] = Quit the programme")
   choice = input("\n>")


   if choice == "q":
      break
  
   if choice == "a":
      print("\n===================================")
      print("    ||      \\ //               ..       ")
      print(" ===||===     X    =====     ======     ")
      print("    ||      // \\               ..       ")
      print("===================================")
      
      num1 = float(input("\n[*] Enter first number: "))
      num2 = float(input("[*] Enter second number: "))
      oper = input("[*] Choose Operater (+,-,/,*)\n: ")
      MyCalc(num1, num2, oper)

      time.sleep(2)
      ch = input("[+] Continue? (Y)es / (N)o: ")    
     
      if ch == "Y" or "y":
              MyCalc(num1, num2, oper)
      elif ch == "N" or "n":
               break
           
           
           
           
   if choice == "b":
         print("===================================")
         print(" [R]ock, [P]aper, [S]cissors v1.0")
         print("===================================")
         time.sleep(2)
         print("[*] LOCATION: THe Hub")
         time.sleep(1.5)
         print("[*] MISSION: Deafeat the r@nd0m A.I\n")
         time.sleep(1.5)
         print("[*] Choose your WEAPON")
         print("[R]ock, [P]aper, [S]cissors")
         intro = input(": ")
         if not re.match("[SsRrPp]", intro):
             print("[!]Chose your WEAPON:")
             intro=input("[!][R]ock, [P]aper, [S]cissors: ")
             continue
 
         rps(intro)
         
         name = input("[*]Rematch (y/n): ")
        
         if not re.match("[Yy]", name):
                break
         else:
             rps(intro)
   
   if choice == "c":
      print("===================================")
      print("      Friendly Cow v1.0")
      print("===================================")
      

      name=input("What is your name,stranger? \n:")
      print("\n{ Good M00'ning", name,"}")

      print("              \   ^__^      ") 
      print("               \  (oo)\_______   *")
      print("                  (__)\       )\/")
      print("                      ||----w |  ")
      print("                      ||     ||   ")

      time.sleep(2)
      print("\n{ Welcome to the FORTUNATE COW}\n")

      print("                       \   ^__^      ") 
      print("                        \  (oo)\_______   *")
      print("                           (__)\       )\/")
      print("                               ||----w |  ")
      print("                               ||     ||   ")
      
      time.sleep(2)
      
      fortune_list=['happy', 'sad', 'joy', 'happy', 'blessed', 'angry', 'hate', 'caring', 'passionate']

      fortune = random.choice(fortune_list)

      print("\n{ Here is Your Fortune::",fortune,"}")

      print("                               \   ^__^      ") 
      print("                                \  (oo)\_______   *")
      print("                                   (__)\       )\/")
      print("                                       ||----w |  ")
      print("                                       ||     ||   ")
      
      input(":")
      
      



   if choice == "d":
     print("===================================")
     print("  ----Password Manager v1.0----")
     print("===================================")
     
     numinput = 5
     
     app = input("\n[+] Generating password for: ")
     length = int(input("\n[+] Password length: "))
     
     
     pwmgr(numinput, app, length)
     
     
     name = input("[*]Generate another Password Y/N: ")
        
     if not re.match("[Yy]", name):
                break
     else:
            pwmgr(numinput, app, length)
            
            

   if choice == "e":

     print("===================================")
     print(" ----YouTube Downloader v1.0----")
     print("===================================")
     
     url = input("[+]Enter the video url: ")
     youdl(url)

     
   if choice == "f":
     print("===================================")
     print(" Instagram Profile Downloader v1.0")
     print("===================================")
     
     
     bot = instaloader.Instaloader()
     link = input("[+]Username: ")
     print(bot.download_profile(link,profile_pic_only=True))
     print("[*]Profile Download Successful")
 
   
   if choice == "g":
     print("===================================")
     print("  ----Inbuilt Dictionary v1.0----")
     print("===================================")
     
     dict = PyDictionary()
     
     word = dict.meaning(input("[+]Enter your word: "))
     print(word)
     
   
   if choice == "h":
     print("===================================")
     print("  Video-Audio converter v1.0----")
     print("===================================")

     vid = input("[+]Directory of the Video: ")
     
     video = moviepy.editor.VideoFileClip(vid)
     audio = video.audio
     
     audio.write_audiofile(vid)
     print("[*]Conversion Successfully") 


   
   
   if choice == "i":
     print("===================================")
     print(" ----Text-Audio Converter v1.0----")
     print("===================================")
     
     files = input("[+]Directory of the File: ")
     path = open(files, 'rb')
     reader = PyPDF2.PdfFileReader(path)
     page = reader.getPage(0)
     text = page.extractText()
     
     speak = pyttsx3.init()
     speak.say(text)
     speak.runAndWait()


   if choice == "j":
     print("===================================")
     print("     ----Mirror! Mirror! v1.0----")
     print("===================================")
     audio = "audio.mp3"
     language = 'en'
     text = input("[*]What is your desire:")
     clip = gTTS(text, lang = language, slow=False)
     
     clip.save(audio)
     playsound(audio)

   if choice == "k":
     print("===================================")
     print("     ----iBrowser v1.0----")
     print("===================================")

     dtime()
     
   if choice == "l":
      print("===================================")
      print("       ----The Quiz Show----")
      print("===================================")
      
      counter = int(input("\n[+] Number of players: "))
      players = []
     
      for i in range(counter):
            p_name = input("\n[+] Player name: ")
            players.append(p_name)
            
            
      print("\n[+] Confirm players:", players)
       
      ch = input("(Y)es/(N)o: ")
      if not re.match("[Yy]", ch):
         break 
      else:
         chose = random.choice(players)
         print("\n[*]", chose, "'s turn")
         quiz=input("\n[*]what is the capital of city of Kenya:")
      if quiz == "Nairobi":
         print("\n[+]Correct")
      else:
         print("\n[+]Incorrect, Try Again!") 


