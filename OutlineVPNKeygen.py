#!/usr/bin/python
# 
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

api_key1 = 'APIKEY1' # Netherlands {countryid1}
api_key2 = 'APIKEY2' # United States {countryid2}
api_key3 = 'APIKEY3' # United Kingdom {countryid3}
countryid1 = 'Netherlands' #Freindly Name for first server, it will be used for SMTB library mail delivey as well. Change this if the country of the VPN changes.
countryid2 = 'United States' #Freindly Name for second server.
countryid3 = 'United Kingdom' #Freindly Name for third server.

choice = input(f"""
What would you like to do
[0] List all access keys
[1] Create a server on the {countryid1} server
[2] Create a server on the {countryid2} server
[3] Create a server on the {countryid3} server
[4] Create a server on All servers.
[5] Quick-Create on ALL
[6] Delete Key
[7] Test SMTP
""")
if choice == "0": #This stupid python if statement you made doesn't query the third server. Fix when possible
    response1 = requests.get(f'{api_key1}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    response2 = requests.get(f'{api_key2}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    response3 = requests.get(f'{api_key3}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    response1.raise_for_status() #Display error when thrown so it isn't hidden
    response2.raise_for_status() #Display error when thrown so it isn't hidden
    response3.raise_for_status() #Display error when thrown so it isn't hidden
    data1 = response1.json() #Tell python to set this data type to JSON.
    data2 = response2.json() #Tell python to set this data type to JSON.
    data3 = response3.json() #Tell python to set this data type to JSON.
    key1 = data1['accessKeys'] #Establish dictionary for the other server.
    key2 = data2['accessKeys'] #Establish dictionary for specific server.
    key3 = data3['accessKeys'] #Establish dictionary for the third server.
    print(f'\n{countryid1}\n{key1}\n\n\n\n\n{countryid2}\n{key2}\n\n\n\n\n{countryid3}\n{key3}') #Print all keys to console.
    exit() #Quit program when done
if choice == "1": #Create a server on the Netherlands server
    key2 = f'You did not request an access key for the {countryid2} VPN, if you believe this is an error, please reply to this email.' #Set VPN to null as client did not request key for this specific server
    key3 = f'You did not request an access key for the {countryid3} VPN, if you believe this is an error, please reply to this email.'
    print(f'Please wait, creating a VPN key for {countryid1}.') #Please wait
    response1 = requests.post(str(api_key1)+'/access-keys',verify=False)
    print(f'Successfully added new key to {countryid1} servers.')
    response1.raise_for_status() #Raise error if error is returned
    data1 = response1.json()
    key1 = data1['accessUrl']
    id1 = data1['id']
    print(f'User Key:{key1}\nUser ID:{id1}')
if choice == "2": #Create a server on the United States server
    key1 = f'You did not request an access key for the {countryid1} VPN, if you believe this is an error, please reply to this email.'
    key3 = f'You did not request an access key for the {countryid3} VPN, if you believe this is an error, please reply to this email.'
    response2 = requests.post((f'{api_key2}/access-keys'),verify=False)
    print(f'Successfully added new key to {countryid2} servers.')
    response2.raise_for_status()
    data2 = response2.json()
    print(data2)
    key2 = data2['accessKeys']
    id2 = data2['accessUrl']['id']
    print(id2)
    print(f'{key2}\n{key1}')
if choice == "3": #Create a server on the British server
    key2 = 'You did not request an access key for the American VPN, if you believe this is an error, please reply to this email.'
    key1 = 'You did not request an access key for the Dutch VPN, if you believe this is an error, please reply to this email.'
    responseaus = requests.post((f'{api_key3}/access-keys'),verify=False)
    print("Successfully added new key to Aussie servers.")
    responseaus.raise_for_status()
    data3 = responseaus.json()
    print(data3)
    key3 = data3['accessKeys'][0]['accessUrl']
    id3 = data3['accessUrl']['id']
    print(id1)
    print(f'{countryid1} Key:{key1}\n {countryid2} Key:{key2}\n {countryid3} Keys:{key3}')
if choice == "4": #Create key for all servers (MAIN COMMAND)
    reponse1 = requests.post((f'{api_key1}/access-keys'),verify=False)
    response2 = requests.post((f'{api_key2}/access-keys'),verify=False)
    reponse3 = requests.post((f'{api_key3}/access-keys'),verify=False)
    response1.raise_for_status()
    response2.raise_for_status()
    response3.raise_for_status()
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()
    print(f'Successfully added new key to all servers.\n{data1}\n{data2}\n{data3}')
    key1 = data1['accessUrl']
    key2 = data2['accessUrl']
    key3 = data3['accessUrl']
    id1 = data1['id']
    id2 = data2['id']
    id3 = data3['id']
    print(f'{countryid1} KEY:{key1} ID:{id1}\n {countryid2} KEY:{key2} ID:{id2}\n {countryid3} KEY: {key3} ID:{id3}')
if choice == "5":#Quick Create on all servers
    email = input("Enter recipient's email:")
    name = email
    response1 = requests.post((f'{api_key1}/access-keys'),verify=False)
    response2 = requests.post((f'{api_key2}/access-keys'),verify=False)
    response3 = requests.post((f'{api_key3}/access-keys'),verify=False)
    response1.raise_for_status()
    response2.raise_for_status()
    response3.raise_for_status()
    data1 = response1.json()
    data2 = response2.json()
    data3 = response3.json()
    print("Successfully added new key to all servers.")
    print("\n")
    print(data2)
    print(data1)
    print(data3)
    key2 = data2['accessUrl']
    key1 = data1['accessUrl']
    key3 = data3['accessUrl']
    id2 = data2['id']
    id1 = data1['id']
    id3 = data3['id']
    print(f'{countryid1} KEY:{key1} ID:{id1}\n{countryid2} KEY:{key2} ID:{id2}\n{countryid3} KEY: {key3} ID:{id3}')
    receivers = email
    sender = '*@gmail.com'
    gmail_pass = '*'
    message = """From: OutlineVPNissuer <OutlineVPNissuer@digisec.tools>
To: OutlineVPNUser <(OutlineUser@digisec.tools)>
Subject: Your VPN keys have arrived!

To avoid issues, I recommend you install Outline VPN Client, which is a client specifically made for the VPN server's infrastructure.
"""
    message += 'Your VPN keys:' + '\n'
    message += f'{countryid2}:\n{key2}\n'
    message += f'{api_key1}\n{key1}\n'
    message += f'{api_key3}\n{key3}\n'
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
    responseus = requests.put(f'{api_key2}/access-keys/{id2}/name', data = {'name':f'{email}'}, verify=False)
    responsenl = requests.put(f'{api_key1}/access-keys/{id1}/name', data = {'name':f'{email}'}, verify=False)
    responseaus = requests.put(f'{api_key3}/access-keys/{id3}/name', data = {'name':f'{email}'}, verify=False)
    exit()
if choice == "6": #Create a delete request for a certain key from the database.
    responsenl = requests.get(f'{api_key1}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    responsenl.raise_for_status()
    data1 = responsenl.json()
    responseus = requests.get(f'{api_key2}/access-keys',verify=False) #Get list of access keys on the server. Do not verify SSL certificate
    responseus.raise_for_status()
    data2 = responseus.json()
    key2 = data2['accessKeys']
    key1 = data1['accessKeys']
    print(f'{countryid2} Keys: {key2}\n\n\n{countryid1} Keys: {key1}')
    deletewhich = input("""
Which keys whould you like to delete? (This option will result in the removal of the keys from all servers, not just one. To remove one key from one server database, please use Outline Manager.)
    [Enter Key ID]
    """)
    responseus = requests.delete(f'{api_key2}/access-keys/{deletewhich}',verify=False)
    responsenl = requests.delete(f'{api_key1}/access-keys/{deletewhich}',verify=False)

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
        sender = '*@gmail.com'
        gmail_pass = '*'
        message = """From: OutlineVPNissuer <OutlineVPNissuer@digisec.tools>
    To: OutlineVPNUser <(OutlineUser@digisec.tools)>
    Subject: Your VPN keys have arrived!

    To avoid issues, I recommend you install Outline VPN Client, which is a client specifically made for the VPN server's infrastructure.
    """
        message += 'Your VPN keys:' + '\n'
        message += f'{countryid1} key: {key1}\n{countryid2} key: {key2}\n{countryid3} key: {key3}'
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
            responseus = requests.put(f'{api_key2}/access-keys/{id2}/name', data = {'name':f'{email}'}, verify=False)
        if choice == "2": #NL
            responsenl = requests.put(f'{api_key1}/access-keys/{id1}/name', data = {'name':f'{email}'}, verify=False)
        if choice == "3": #AUSSIE
            responseaus = requests.put(f'{api_key3}/access-keys/{id3}/name', data = {'name':f'{email}'}, verify=False)
        if choice == "4": #ALL KEYS
            responseus = requests.put(f'{api_key2}/access-keys/{id2}/name', data = {'name':f'{email}'}, verify=False)
            responsenl = requests.put(f'{api_key1}/access-keys/{id1}/name', data = {'name':f'{email}'}, verify=False)
            responseaus = requests.put(f'{api_key3}/access-keys/{id3}/name', data = {'name':f'{email}'}, verify=False)

    if whatnext == "1": #[1] Copy key to clipboard
        pyperclip.copy(finalkeystosend)
        #responseus = requests.put((f'{api_key2}/access-keys/{id2}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        #responsenl = requests.put((f'{api_key1}/access-keys/{id1}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        response2 = requests.put(f'{api_key2}/access-keys/{id2}/name', data = {'name':f'{email}'}, verify=False)
        response1 = requests.put(f'{api_key1}/access-keys/{id1}/name', data = {'name':f'{email}'}, verify=False)
        response3 = requests.put(f'{api_key3}/access-keys/{id3}/name', data = {'name':f'{email}'}, verify=False)
    if whatnext == "2": #[2] Just rename the US key
        #responseus = requests.put((f'{api_key2}/access-keys/{id2}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        response2 = requests.put(f'{api_key2}/access-keys/{id2}/name', data = {'name':f'{email}'}, verify=False)
    if whatnext == "3": #[3] Just rename the NL key
        #responsenl = requests.put((f'{api_key1}/access-keys/{id1}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        response1 = requests.put(f'{api_key1}/access-keys/{id1}/name', data = {'name':f'{email}'}, verify=False)
    if whatnext == "4":
        #responseaus = requests.put((f'{api_key3}/access-keys/{id3}/{name}'),verify=False) THIS IS OLD CODE, USE THIS TO RECOVER PREVIOUS WORK
        response3 = requests.put(f'{api_key3}/access-keys/{id3}/name', data = {'name':f'{email}'}, verify=False)
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
