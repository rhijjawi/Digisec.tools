#!/usr/bin/python
# Welcome to my custom Python script! I designed this for my MYP Grade 10 Personal Project
#
#
#
#
#
#
#
import smtplib #
import requests #
import json #
import pyperclip #
import argparse
import ssl
import urllib
import os

api_keynl = 'APIKEY1'
api_keyus = 'APIKEY2'
api_keyaus = 'APIKEY3'
apikey1 = 'Dutch' #Freindly Name for first server, it will be used for SMTB library mail delivey as well. Change this if the country of the VPN changes.
apikey2 = 'United States' #Freindly Name for second server.
apikey3 = 'Australia' #Freindly Name for third server.

choice = input(f"""
What would you like to do
[0] List all access keys
[1] Create a server on the {apikey1} server
[2] Create a server on the {apikey2} server
[3] Create a server on the {apikey3} server
[4] Create a server on All servers.
[5] Quick-Create on ALL
[6] Delete Key
""")
if choice == "0": #This stupid python if statement you made doesn't query the third server. Fix when possible
    responsenl = requests.get(f'{api_keynl}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    #responsenl.raise_for_status()
    datanl = responsenl.json()
    responseus = requests.get(f'{api_keyus}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    #responseus.raise_for_status()
    dataus = responseus.json() #Tell python to set this data type to JSON.
    keyus = dataus['accessKeys'] #Establish dictionary for specific server.
    keynl = datanl['accessKeys'] #Establish dictionary for the other server.
    print(f'{keyus}\n{keynl}') #Print all keys to console.
    exit() #Quit program when done
if choice == "1": #Create a server on the {apikey1} server
    keynl = f'You did not request an access key for the {apikey1} VPN, if you believe this is an error, please reply to this email.' #Set VPN to null as client did not request key for this specific server
    keyaus = f'You did not request an access key for the {apikey3} VPN, if you believe this is an error, please reply to this email.'
    print("Please wait") #Please wait
    responseus = requests.post(str(api_keyus)+'/access-keys',verify=False)
    print(f'Successfully added new key to {apikey2} servers.')
    responseus.raise_for_status() #Raise error if error is returned
    dataus = responseus.json()
    print(dataus)
    keyus = dataus['accessUrl']
    print(keyus)
    idus = dataus['id']
    print(idus)
if choice == "2": #Create a server on the {apikey2} server
    keyus = f'You did not request an access key for the {apikey2} VPN, if you believe this is an error, please reply to this email.'
    keyaus = f'You did not request an access key for the {apikey3} VPN, if you believe this is an error, please reply to this email.'
    responsenl = requests.post((f'{api_keynl}/access-keys'),verify=False)
    print("Successfully added new key to Dutch servers.")
    responsenl.raise_for_status()
    datanl = responsenl.json()
    print(datanl)
    keynl = datanl['accessKeys']
    idnl = datanl['accessUrl']['id']
    print(idnl)
    print(f'{keyus}\n{keynl}')
if choice == "3": #Create a server on the {apikey3} server
    keyus = 'You did not request an access key for the American VPN, if you believe this is an error, please reply to this email.'
    keynl = 'You did not request an access key for the Dutch VPN, if you believe this is an error, please reply to this email.'
    responseaus = requests.post((f'{api_keyaus}/access-keys'),verify=False)
    print("Successfully added new key to Aussie servers.")
    responseaus.raise_for_status()
    dataaus = responseaus.json()
    print(dataaus)
    keyaus = dataaus['accessKeys'][0]['accessUrl']
    idaus = dataaus['accessUrl']['id']
    print(idnl)
    print(f'{apikey3} Key:{keyaus}\n {apikey2} Key:{keyus}\n {apikey1} Keys:{keynl}')
if choice == "4": #
    responseus = requests.post((f'{api_keyus}/access-keys'),verify=False)
    responseus.raise_for_status()
    dataus = responseus.json()
    responsenl = requests.post((f'{api_keynl}/access-keys'),verify=False)
    responsenl.raise_for_status()
    datanl = responsenl.json()
    responseaus = requests.post((f'{api_keyaus}/access-keys'),verify=False)
    responseaus.raise_for_status()
    dataaus = responseaus.json()
    print(f'Successfully added new key to all servers.\n{dataus}\n{datanl}\n{dataaus}')
    keyus = dataus['accessUrl']
    keynl = datanl['accessUrl']
    keyaus = dataaus['accessUrl']
    idus = dataus['id']
    idnl = datanl['id']
    idaus = dataaus['id']
    print(f'US KEY:{keyus}\n DUTCH KEY:{keynl}\n AUSSIE KEY: {keyaus}')
if choice == "5":
    email = input("Enter recipient's email:")
    name = email
    responseus = requests.post((f'{api_keyus}/access-keys'),verify=False)
    responseus.raise_for_status()
    dataus = responseus.json()
    responsenl = requests.post((f'{api_keynl}/access-keys'),verify=False)
    responsenl.raise_for_status()
    datanl = responsenl.json()
    responseaus = requests.post((f'{api_keyaus}/access-keys'),verify=False)
    responseaus.raise_for_status()
    dataaus = responseaus.json()
    print("Successfully added new key to all servers.")
    print("\n")
    print(dataus)
    print(datanl)
    print(dataaus)
    keyus = dataus['accessUrl']
    keynl = datanl['accessUrl']
    keyaus = dataaus['accessUrl']
    idus = dataus['id']
    idnl = datanl['id']
    idaus = dataaus['id']
    print(f'US KEY:{apikey2}\n DUTCH KEY:{apikey1}\n{apikey3} KEY: {keyaus}')

    receivers = email
    sender = '*@gmail.com'
    gmail_pass = '*'
    message = """From: OutlineVPNissuer <OutlineVPNissuer@digisec.tools>
To: OutlineVPNUser <(OutlineUser@digisec.tools)>
Subject: Your VPN keys have arrived!

To avoid issues, I recommend you install Outline VPN Client, which is a client specifically made for the VPN server's infrastructure.
"""
    message += 'Your VPN keys:' + '\n'
    message += f'{apikey2}:\n{keyus}\n'
    message += 'NL:' + '\n' + str(keynl) + '\n'
    message += 'AUS:' + '\n' + str(keyaus) + '\n'
    try:
       smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
       smtpObj.ehlo()
       smtpObj.starttls()
       smtpObj.ehlo()
       smtpObj.login(sender, gmail_pass)
       smtpObj.sendmail(sender, receivers, message)
       smtpObj.quit()
       print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")
    responseus = requests.put(f'{api_keyus}/access-keys/{idus}/name', data = {'name':f'{email}'}, verify=False)
    responsenl = requests.put(f'{api_keynl}/access-keys/{idnl}/name', data = {'name':f'{email}'}, verify=False)
    responseaus = requests.put(f'{api_keyaus}/access-keys/{idaus}/name', data = {'name':f'{email}'}, verify=False)
    exit()
if choice == "6": #Create a delete request for a certain key from the database.
    #responsenl = requests.get(f'{api_keynl}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    #responsenl.raise_for_status()
    #datanl = responsenl.json()
    responseus = requests.get(f'{api_keyus}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    responseus.raise_for_status()
    dataus = responseus.json()
    keyus = dataus['accessKeys']
    #keynl = datanl['accessKeys']
    print(f'{apikey2} Keys: {keyus}\n\n\n{apikey1} Keys: keynl')
    deletewhich = input("""
    Which keys whould you like to delete? (This option will result in the removal of the keys from all servers, not just one. To remove one key from one server database, please use Outline Manager.)
    [Enter Key ID]
    """)
    responseus = requests.delete(f'{api_keyus}/access-keys/{deletewhich}',verify=False)
    responsenl = requests.delete(f'{api_keynl}/access-keys/{deletewhich}',verify=False)

if choice != "6":
    whatnext = input("""
    What would you like to do? (All options require you to rename the key!)
    [0] Send key(s) via email?
    [1] Copy key(s) to clipboard
    [2] Just rename US key
    [3] Just rename NL key
    [4] Just rename AUS key
    """)
    email = input("Enter recipient's email/name (If you use name, the email will not be able to send):")
    name = email
    files = {
        'name': (None, email)
        }
    if whatnext == "0": #[0] Send key via email?
        receivers = email
        sender = 'ramzihijjawi@gmail.com'
        gmail_pass = 'iijzjmeywyhpiihf'
        message = """From: OutlineVPNissuer <OutlineVPNissuer@digisec.tools>
    To: OutlineVPNUser <(OutlineUser@digisec.tools)>
    Subject: Your VPN keys have arrived!

    To avoid issues, I recommend you install Outline VPN Client, which is a client specifically made for the VPN server's infrastructure.
    """
        message += 'Your VPN keys:' + '\n'
        message += 'US:' + '\n' + str(keyus) + '\n'
        message += 'NL:' + '\n' + str(keynl) + '\n'
        message += 'AUS:' + '\n' + str(keyaus) + '\n'
        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.ehlo()
            smtpObj.login(sender, gmail_pass)
            smtpObj.sendmail(sender, receivers, message)
            smtpObj.quit()
            print("Successfully sent email")
        except SMTPException:
            print("Error: unable to send email")
        if choice == "1": #US
            responseus = requests.put(f'{api_keyus}/access-keys/{idus}/name', data = {'name':f'{email}'}, verify=False)
        if choice == "2": #NL
            responsenl = requests.put(f'{api_keynl}/access-keys/{idnl}/name', data = {'name':f'{email}'}, verify=False)
        if choice == "3": #AUSSIE
            responseaus = requests.put(f'{api_keyaus}/access-keys/{idaus}/name', data = {'name':f'{email}'}, verify=False)
        if choice == "4": #ALL KEYS
            responseus = requests.put(f'{api_keyus}/access-keys/{idus}/name', data = {'name':f'{email}'}, verify=False)
            responsenl = requests.put(f'{api_keynl}/access-keys/{idnl}/name', data = {'name':f'{email}'}, verify=False)
            responseaus = requests.put(f'{api_keyaus}/access-keys/{idaus}/name', data = {'name':f'{email}'}, verify=False)

    if whatnext == "1": #[1] Copy key to clipboard
        pyperclip.copy(finalkeystosend)
        #responseus = requests.put((f'{api_keyus}/access-keys/{idus}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        #responsenl = requests.put((f'{api_keynl}/access-keys/{idnl}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        responseus = requests.put(f'{api_keyus}/access-keys/{idus}/name', data = {'name':f'{email}'}, verify=False)
        responsenl = requests.put(f'{api_keynl}/access-keys/{idnl}/name', data = {'name':f'{email}'}, verify=False)
        responseaus = requests.put(f'{api_keyaus}/access-keys/{idaus}/name', data = {'name':f'{email}'}, verify=False)
    if whatnext == "2": #[2] Just rename the US key
        #responseus = requests.put((f'{api_keyus}/access-keys/{idus}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        responseus = requests.put(f'{api_keyus}/access-keys/{idus}/name', data = {'name':f'{email}'}, verify=False)
    if whatnext == "3": #[3] Just rename the NL key
        #responsenl = requests.put((f'{api_keynl}/access-keys/{idnl}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        responsenl = requests.put(f'{api_keynl}/access-keys/{idnl}/name', data = {'name':f'{email}'}, verify=False)
    if whatnext == "4":
        #responseaus = requests.put((f'{api_keyaus}/access-keys/{idaus}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        responseaus = requests.put(f'{api_keyaus}/access-keys/{idaus}/name', data = {'name':f'{email}'}, verify=False)
#MIT License - DO NOT MODIFY

#Copyright (c) [2020] [Ramzi Hijjawi]
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.'
