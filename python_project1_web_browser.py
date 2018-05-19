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

elif ch=='3':
    search_data=input("Enter the URL to be retrieved: ")
    final_data=search_data.strip()
    fin=final_data.split()
    for i in final_data:
        page = requests.get("https://www.google.dz/search?q="+i)
        soup=BeautifulSoup(page.text,'html.parser')

    for i in soup.find_all('a'):
        #find all the values that starts with a
        a=i.get('href').split('https://')
        #splits data on the basis of https
        for element in a:
            #if any link starts with wikipedia then it prints it
            if(element.startswith('en.wikipedia')):
                print(element)

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
    webbrowser.open("https://")

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
    time.sleep(2)
    str1 = ''.join(list1)'''
    print(all_data)
    print("Name is:"+str(all_data.get("domain_name")))
    print("Email is:"+str(all_data.get("emails")))
    print("Address is: "+str(all_data.get("address"))+","+str(all_data.get("city"))+","+str(all_data.get("state")))
    #print(type(list(whois("https://www."+url))))
