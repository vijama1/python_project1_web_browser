import time;
import webbrowser;
import urllib3.request
import requests
from whois import whois
import platform
import os
from bs4 import BeautifulSoup
import subprocess
print("MENU LIST")
print("Press 1 for searching on Google ")
print("Press 2 for searching Images ")
print("Press 3 for getting the URL ")
print("Press 4 for getting current date and time ")
print("Press 5 for opening default web browser ")
print("Press 6 for Getting network IP ")
print("Press 7 for checking owner ")

ch=input("Enter your choice: ")

if ch=='1':
    print("Inside1")
    search_data=input("Enter the data: ")
    final_data=search_data.strip()
    done_data=final_data.split()
    for i in done_data:
        #opens a new tab for the given query and performs the google search
        webbrowser.open_new_tab("https://www.google.com/search?&q="+i)


elif ch=='2':
    search_data=input("Enter the image to be searched: ")
    final_data=search_data.strip()
    done_data=final_data.split()
    for i in done_data:
        #opens a new tab for the given query and performs searching of images
        a=webbrowser.open_new_tab("https://www.google.com/search?tbm=isch&q="+i)
#
elif ch=='3':
    data=input("Enter the url: ")
    url="https://google.com/search?q="+data
    #for i in search_data:
    page=requests.get(url)
        #print(page)
    soup=BeautifulSoup(page.content,'html5lib')
        #print(soup)
    all_links=soup.find_all("a")
    for i in all_links:
        #find all the values that starts with a

        link_href=i.get('href')
        #print(link_href)
        if "url?q=" in link_href and not "webcache" in link_href :
          #to replace url codes like ? as %3F and = as %3D as =
          if "%3F" in link_href :
            link_href=link_href.replace("%3F","?")
          if "%3D" in link_href:
            link_href=link_href.replace("%3D","=")
          #removing /url?q= from the link
          link_url=link_href.split('url?q=')[1]
          #filtering usefull part of url
          link_final=link_url.split('&sa=U')[0]
          print(link_final)
        #splits data on the basis of https
        #for element in a:
            #if any link starts with wikipedia then it prints it
            #if(element.startswith('en.wikipedia')):
        #print(i)

if ch=='4':
    #gives curren date and time
    splitted_value=time.ctime()
    print(splitted_value)
    day=splitted_value[0:11]+splitted_value[20:]
    print("Today is: "+day)
    time=splitted_value[11:19]
    print("Time is: "+time)

if ch=='5':
    #opens the default web browser with new tab
    webbrowser.get()

if ch=='6':
    # gives the list of all the IP addresses that system has been assigned
    #a=subprocess.Popen('hostname -I')
    ip=os.system('hostname -I')



if ch=='7':
    url=input("Enter the url:")
    all_data=whois("https://www."+url)
    #returns a dictionary containing all the data regarding the given url
    all_data_keys=whois("https://www."+url).keys()
    all_data_values=whois("https://www."+url).values()
    '''print(all_data_keys)
    print("---------------------------------------------------------------------")
    time.sleep(2)
    print(all_data_values)
    print("---------------------------------------------------------------------")
    time.sleep(2)'''
    print(all_data)
    print("Name is:"+str(all_data.get("domain_name")))
    print("Email is:"+str(all_data.get("emails")))
    print("Address is: "+str(all_data.get("address")))
    #print(type(list(whois("https://www."+url))))
