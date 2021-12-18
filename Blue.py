from bs4 import BeautifulSoup #line:1
from collections import deque #line:2
import json #line:3
import nmap #line:4
import os #line:5
import re #line:6
import requests #line:7
import requests .exceptions #line:8
import time #line:9
from time import gmtime ,strftime #line:10
from urllib .error import URLError #line:11
from urllib .parse import urlsplit #line:12
import urllib3 #line:13
import urllib .request #line:14
from urllib .request import urlopen #line:15
def banner ():#line:18
    print ('''
 _______   __                     
/       \ /  |                    
$$$$$$$  |$$ | __    __   ______  
$$ |__$$ |$$ |/  |  /  | /      \ 
$$    $$  $$ |$$ |  $$ |/$$$$$$  |
$$$$$$$  |$$ |$$ |  $$ |$$    $$ |
$$ |__$$ |$$ |$$ \__$$ |$$$$$$$$/ 
$$    $$/ $$ |$$    $$/ $$       |
$$$$$$$/  $$/  $$$$$$/   $$$$$$$/           


        Blue - Information Gathering Tool
        Author: Hyro | https://github.com/hyro3000
 ''')#line:33
def menu ():#line:36
    print ("[+] 1.   Whois Lookup")#line:37
    print ("[+] 2.   DNS Lookup")#line:38
    print ("[+] 3.   Nmap Port Scan")#line:39
    print ("[+] 4.   HTTP Header Grabber")#line:40
    print ("[+] 5.   Clickjacking Test - X-Frame-Options Header")#line:41
    print ("[+] 6.   Robots.txt Scanner")#line:42
    print ("[+] 7.   Link Grabber")#line:43
    print ("[+] 8.   IP GeoLocation Finder")#line:44
    print ("[+] 9.   Traceroute")#line:45
    print ("[+] 10.  Have I been pwned")#line:46
    print ("[+] 11.  Exit\n")#line:47
def main ():#line:50
    OO0000OO00O0O00OO =("1")#line:51
    banner ()#line:52
    while OO0000OO00O0O00OO !=("11"):#line:54
        menu ()#line:55
        OO0000OO00O0O00OO =input ("[+] Enter your choice: ")#line:56
        if OO0000OO00O0O00OO ==("1"):#line:58
            try :#line:59
                OO0O00OO0000O00O0 =input ("[+] Enter Domain or IP Address: ").lower ()#line:60
                os .system ("reset")#line:61
                print (f"[+] Searching for... Whois Lookup: ".format (OO0O00OO0000O00O0 )+OO0O00OO0000O00O0 )#line:62
                time .sleep (1.5 )#line:63
                O00000000000O0000 =("whois "+OO0O00OO0000O00O0 )#line:64
                O00000000OOO00OOO =os .popen (O00000000000O0000 )#line:65
                O00OO000O0OO0O00O =str (O00000000OOO00OOO .read ())#line:66
                print (""+O00OO000O0OO0O00O +O00000000000O0000 +"")#line:67
            except Exception :#line:69
                pass #line:70
        elif OO0000OO00O0O00OO ==("2"):#line:72
            try :#line:73
                OO0O00OO0000O00O0 =input ("[+] Enter Domain or IP Address: ").lower ()#line:74
                os .system ("reset")#line:75
                print (f"[+] Searching for... DNS Lookup: ".format (OO0O00OO0000O00O0 )+OO0O00OO0000O00O0 )#line:76
                time .sleep (1.5 )#line:77
                O00000000000O0000 =("dig "+OO0O00OO0000O00O0 +" +trace ANY")#line:78
                O00000000OOO00OOO =os .popen (O00000000000O0000 )#line:79
                O00OO000O0OO0O00O =str (O00000000OOO00OOO .read ())#line:80
                print (""+O00OO000O0OO0O00O +O00000000000O0000 +"")#line:81
            except Exception :#line:83
                pass #line:84
        elif OO0000OO00O0O00OO ==("3"):#line:86
            try :#line:87
                OO0O00OO0000O00O0 =input ("Enter Domain or IP Address: ").lower ()#line:88
                os .system ("reset")#line:89
                print ("[+] Scanning.... Nmap Port Scan: "+OO0O00OO0000O00O0 )#line:90
                print ("[+] This will take a moment.\n")#line:91
                time .sleep (1.5 )#line:92
                OOO0OOO0O00OO0O00 =nmap .PortScanner ()#line:94
                O00000000000O0000 =("nmap -Pn "+OO0O00OO0000O00O0 )#line:95
                O0000000OO00000O0 =os .popen (O00000000000O0000 )#line:96
                O00OO000O0OO0O00O =str (O0000000OO00000O0 .read ())#line:97
                OOO0OO0OO00O0O0O0 ="logs/nmap-"+strftime ("%Y-%m-%d_%H:%M:%S",gmtime ())#line:98
                print (""+O00OO000O0OO0O00O +O00000000000O0000 +OOO0OO0OO00O0O0O0 +"")#line:100
                print ("[+] Nmap Version: ",OOO0OOO0O00OO0O00 .nmap_version ())#line:101
            except KeyboardInterrupt :#line:103
                    print ("\n")#line:104
                    print ("[-] User Interruption Detected..!")#line:105
                    time .sleep (1 )#line:106
        elif OO0000OO00O0O00OO ==("4"):#line:108
            try :#line:109
                OO0O00OO0000O00O0 =input ("[+] Enter Domain or IP Address: ").lower ()#line:110
                os .system ("reset")#line:111
                print ("[+] Scanning.... HTTP Header Grabber: \n"+OO0O00OO0000O00O0 )#line:112
                time .sleep (1.5 )#line:113
                O00000000000O0000 =("http -v "+OO0O00OO0000O00O0 )#line:114
                O00000000OOO00OOO =os .popen (O00000000000O0000 )#line:115
                O00OO000O0OO0O00O =str (O00000000OOO00OOO .read ())#line:116
                print (""+O00OO000O0OO0O00O +O00000000000O0000 +"")#line:117
            except Exception :#line:119
                pass #line:120
        elif OO0000OO00O0O00OO ==("5"):#line:122
            OO0O00OO0000O00O0 =input ("[+] Enter the Domain to test: ").lower ()#line:123
            os .system ("reset")#line:124
            if not (OO0O00OO0000O00O0 .startswith ("http://")or OO0O00OO0000O00O0 .startswith ("https://")):#line:126
                OO0O00OO0000O00O0 ="http://"+OO0O00OO0000O00O0 #line:127
            print ("[+] Testing...  Clickjacking Test: "+OO0O00OO0000O00O0 )#line:128
            time .sleep (2 )#line:129
            try :#line:130
                O0000000O00OO00O0 =requests .get (OO0O00OO0000O00O0 )#line:131
                OOO00OOO0O00OO0O0 =O0000000O00OO00O0 .headers #line:132
                print ("\nHeader set are: \n")#line:133
                for O0O0OOOO000O0OO00 ,O0OO0O00OO00000O0 in OOO00OOO0O00OO0O0 .items ():#line:134
                    print (""+O0O0OOOO000O0OO00 +":"+O0OO0O00OO00000O0 +"")#line:135
                if "X-Frame-Options"in OOO00OOO0O00OO0O0 .keys ():#line:137
                    print ("\n[+] Click Jacking Header is present")#line:138
                    print ("[+] You can't clickjack this site !\n")#line:139
                else :#line:140
                    print ("\n[*] X-Frame-Options-Header is missing ! ")#line:141
                    print ("[!] Clickjacking is possible, this site is vulnerable to Clickjacking\n")#line:142
            except Exception as O000OOOOO0O0O000O :#line:144
                print ("[+] Exception caught: "+str (O000OOOOO0O0O000O ))#line:145
        elif OO0000OO00O0O00OO ==("6"):#line:147
            try :#line:148
                OO0O00OO0000O00O0 =input ("Enter Domain: ").lower ()#line:149
                os .system ("reset")#line:150
                print ("[+] Scanning.... Robots.txt Scanner: \n"+OO0O00OO0000O00O0 )#line:151
                time .sleep (1.5 )#line:152
                if not (OO0O00OO0000O00O0 .startswith ("http://")or OO0O00OO0000O00O0 .startswith ("https://")):#line:154
                    OO0O00OO0000O00O0 ="http://"+OO0O00OO0000O00O0 #line:155
                O0O0000OO0OOOO0O0 =OO0O00OO0000O00O0 +"/robots.txt"#line:156
                try :#line:158
                    OO000O00O0O0O00OO =urlopen (O0O0000OO0OOOO0O0 ).read ().decode ("utf-8")#line:159
                    print (""+(OO000O00O0O0O00OO )+"")#line:160
                except URLError :#line:161
                    print ("[-] Can\'t access to {page}!".format (page =O0O0000OO0OOOO0O0 ))#line:162
            except Exception as O000OOOOO0O0O000O :#line:164
                print ("[+] Exception caught: "+str (O000OOOOO0O0O000O ))#line:165
        elif OO0000OO00O0O00OO ==("7"):#line:167
            try :#line:168
                OO0O00OO0000O00O0 =input ("Enter Domain: ").lower ()#line:169
                os .system ("reset")#line:170
                print ("[+] Scanning.... Link Grabber: \n"+OO0O00OO0000O00O0 )#line:171
                time .sleep (2 )#line:172
                if not (OO0O00OO0000O00O0 .startswith ("http://")or OO0O00OO0000O00O0 .startswith ("https://")):#line:173
                    OO0O00OO0000O00O0 ="http://"+OO0O00OO0000O00O0 #line:174
                OO0O00OO0000O00OO =deque ([OO0O00OO0000O00O0 ])#line:175
                O0OO00000OOO00OOO =set ()#line:176
                try :#line:178
                    while len (OO0O00OO0000O00OO ):#line:179
                        O00OOO00000OO0OO0 =OO0O00OO0000O00OO .popleft ()#line:180
                        O0OO00000OOO00OOO .add (O00OOO00000OO0OO0 )#line:181
                        O000OO0O0OO00OO0O =urlsplit (O00OOO00000OO0OO0 )#line:182
                        OO0OOO00O00000OO0 ="{0.scheme}://{0.netloc}".format (O000OO0O0OO00OO0O )#line:183
                        print ("[+] Crawling URL "+""+O00OOO00000OO0OO0 +"")#line:185
                        try :#line:186
                            OO0OO0000O000OOO0 =requests .get (O00OOO00000OO0OO0 )#line:187
                        except (requests .exceptions .MissingSchema ,requests .exceptions .ConnectionError ):#line:188
                            continue #line:189
                        OOO00OO0OOOOOO00O =BeautifulSoup (OO0OO0000O000OOO0 .text ,"lxml")#line:191
                        for O0O0OO0O0O0000O00 in OOO00OO0OOOOOO00O .find_all ("a"):#line:192
                            OO0OOOOOO000OOOOO =O0O0OO0O0O0000O00 .attrs ["href"]if "href"in O0O0OO0O0O0000O00 .attrs else ''#line:193
                            if OO0OOOOOO000OOOOO .startswith ("/"):#line:194
                                OO0OOOOOO000OOOOO =OO0OOO00O00000OO0 +OO0OOOOOO000OOOOO #line:195
                            if not OO0OOOOOO000OOOOO in OO0O00OO0000O00OO and not OO0OOOOOO000OOOOO in O0OO00000OOO00OOO :#line:196
                                OO0O00OO0000O00OO .append (OO0OOOOOO000OOOOO )#line:197
                            continue #line:198
                except KeyboardInterrupt :#line:200
                        print ("\n")#line:201
                        print ("[-] User Interruption Detected..!")#line:202
                        time .sleep (1 )#line:203
                        print ("\n[+] Exiting...\n")#line:204
            except Exception :#line:206
                pass #line:207
        elif OO0000OO00O0O00OO ==("8"):#line:209
            try :#line:210
                OO0O00OO0000O00O0 =input ("[+] Enter Domain or IP Address: ").lower ()#line:211
                O00OOO00000OO0OO0 =("http://ip-api.com/json/")#line:212
                OO0OO0000O000OOO0 =urllib .request .urlopen (O00OOO00000OO0OO0 +OO0O00OO0000O00O0 )#line:213
                OOOOOO0O0O0O0OO00 =OO0OO0000O000OOO0 .read ()#line:214
                O0000O000OOO00000 =json .loads (OOOOOO0O0O0O0OO00 )#line:215
                os .system ("reset")#line:216
                print (f"[+] Searching.... IP Location Finder: ".format (O00OOO00000OO0OO0 )+OO0O00OO0000O00O0 )#line:217
                time .sleep (1.5 )#line:218
                print ("\n [+] Url: "+OO0O00OO0000O00O0 +"")#line:220
                print (" [+] "+""+"IP: "+O0000O000OOO00000 ["query"]+"")#line:221
                print (" [+] "+""+"Status: "+O0000O000OOO00000 ["status"]+"")#line:222
                print (" [+] "+""+"Region: "+O0000O000OOO00000 ["regionName"]+"")#line:223
                print (" [+] "+""+"Country: "+O0000O000OOO00000 ["country"]+"")#line:224
                print (" [+] "+""+"City: "+O0000O000OOO00000 ["city"]+"")#line:225
                print (" [+] "+""+"ISP: "+O0000O000OOO00000 ["isp"]+"")#line:226
                print (" [+] "+""+"Lat & Lon: "+str (O0000O000OOO00000 ['lat'])+" & "+str (O0000O000OOO00000 ['lon'])+"")#line:227
                print (" [+] "+""+"Zipcode: "+O0000O000OOO00000 ["zip"]+"")#line:228
                print (" [+] "+""+"TimeZone: "+O0000O000OOO00000 ["timezone"]+"")#line:229
                print (" [+] "+""+"AS: "+O0000O000OOO00000 ["as"]+""+"\n")#line:230
            except URLError :#line:232
                print ("[-] Please provide a valid IP address!")#line:233
        elif OO0000OO00O0O00OO ==("9"):#line:235
            try :#line:236
                OO0O00OO0000O00O0 =input ("[+] Enter Domain or IP Address: ").lower ()#line:237
                os .system ("reset")#line:238
                print (f"[+] Searching for: Traceroute: ".format (OO0O00OO0000O00O0 )+OO0O00OO0000O00O0 )#line:239
                print ("[+] This will take a moment... Get some coffee :)\n")#line:240
                time .sleep (5 )#line:241
                O00000000000O0000 =("mtr "+"-4 -rwc 1 "+OO0O00OO0000O00O0 )#line:242
                O00000000OOO00OOO =os .popen (O00000000000O0000 )#line:243
                O00OO000O0OO0O00O =str (O00000000OOO00OOO .read ())#line:244
                print (""+O00OO000O0OO0O00O +O00000000000O0000 +"")#line:245
            except Exception :#line:247
                pass #line:248
        elif OO0000OO00O0O00OO ==("10"):#line:250
            try :#line:251
                OO0O00OO0000O00O0 =input ("[+] Enter email: ")#line:252
                os .system ("reset")#line:253
                print ("[+] Scanning....Have I been pwned: \n"+OO0O00OO0000O00O0 )#line:254
                time .sleep (1.5 )#line:255
                O00OOO00000OO0OO0 =("https://haveibeenpwned.com/api/v2/breachedaccount/%s"%OO0O00OO0000O00O0 )#line:256
                OO0OO0000O000OOO0 =requests .get (O00OOO00000OO0OO0 )#line:257
                if OO0OO0000O000OOO0 .status_code ==200 :#line:259
                    OO0OO0000O000OOO0 =OO0OO0000O000OOO0 .json ()#line:260
                    O0O00OO00OO0OO00O =len (OO0OO0000O000OOO0 )#line:261
                    for O0O0OOOO000O0OO00 in range (O0O00OO00OO0OO00O ):#line:263
                        O00000OOO000000O0 =str (OO0OO0000O000OOO0 [O0O0OOOO000O0OO00 ]["DataClasses"])#line:264
                        O00000OOO000000O0 =re .sub ("\[(?:[^\]|]*\|)?([^\]|]*)\]",r"\1",O00000OOO000000O0 )#line:265
                        O00000OOO000000O0 =O00000OOO000000O0 .replace ("'","")#line:266
                        print ("\n")#line:268
                        print ("[+] Name:     "+""+str (OO0OO0000O000OOO0 [O0O0OOOO000O0OO00 ]["Title"])+"")#line:269
                        print ("[+] Domain:   "+""+str (OO0OO0000O000OOO0 [O0O0OOOO000O0OO00 ]["Domain"])+"")#line:270
                        print ("[+] Breached: "+""+str (OO0OO0000O000OOO0 [O0O0OOOO000O0OO00 ]["BreachDate"])+"")#line:271
                        print ("[+] Details:  "+""+str (O00000OOO000000O0 )+"")#line:272
                        print ("[+] Verified: "+""+str (OO0OO0000O000OOO0 [O0O0OOOO000O0OO00 ]["IsVerified"])+"")#line:273
                else :#line:274
                    print ("[+] Email NOT Found in Database")#line:275
            except Exception :#line:277
                print ("[+] Unable to reach HaveIBeenPwned")#line:278
        elif OO0000OO00O0O00OO ==("11"):#line:280
            time .sleep (1 )#line:281
            print ("\n[+] Exiting...")#line:282
        else :#line:284
            print ("[-] Invalid option!")#line:285
if __name__ =="__main__":#line:290
    main ()#line:291
