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
api_keynl = 'APIURL'
api_keyus = 'APIURL'
api_keyaus = 'APIURL'

choice = input("""
On what server would you like to create a account?
[0] List all access keys
[1] US
[2] NL
[3] AUS
[4] All
[5] Delete Key
""")
if choice == "0":
    responsenl = requests.get(f'{api_keynl}/access-keys',verify=False)
    responsenl.raise_for_status()
    datanl = responsenl.json()
    responseus = requests.get(f'{api_keyus}/access-keys',verify=False)
    responseus.raise_for_status()
    dataus = responseus.json()
    keyus = dataus['accessKeys']
    keynl = datanl['accessKeys']
    print(keyus)
    print("\n")
    print(keynl)
    exit()
if choice == "1":
    keynl = 'You did not request an access key for the Dutch VPN, if you believe this is an error, please reply to this email.'
    keyaus = 'You did not request an access key for the Aussie VPN, if you believe this is an error, please reply to this email.'
    print("Please wait")
    responseus = requests.post(str(api_keyus)+'/access-keys',verify=False)
    print("Successfully added new key to US servers.")
    responseus.raise_for_status()
    dataus = responseus.json()
    print(dataus)
    keyus = dataus['accessUrl']
    print(keyus)
    idus = dataus['id']
    print(idus)
if choice == "2":
    keyus = 'You did not request an access key for the American VPN, if you believe this is an error, please reply to this email.'
    keyaus = 'You did not request an access key for the Aussie VPN, if you believe this is an error, please reply to this email.'
    responsenl = requests.post((f'{api_keynl}/access-keys'),verify=False)
    print("Successfully added new key to Dutch servers.")
    responsenl.raise_for_status()
    datanl = responsenl.json()
    print(datanl)
    keynl = datanl['accessKeys'][0]['accessUrl']
    idnl = datanl['accessUrl']['id']
    print(idnl)
    print(f'{keyus}\n{keynl}')
if choice == "3":
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
    print(f'Aussie Key:{keyaus}\n United States Key:{keyus}\n Dutch Keys:{keynl}')
if choice == "4":
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
    uskey = dataus['accessKeys'][0]['accessUrl']
    keynl = datanl['accessKeys'][0]['accessUrl']
    keyaus = dataaus['accessKeys'][0]['accessUrl']
    idus = dataus['id']
    idnl = datanl['id']
    idaus = dataaus['id']
    print(f'US KEY:{idus}\n DUTCH KEY:{idnl}\n AUSSIE KEY: {idaus}')
if choice == "5":
    stop
finalkeystosend = (f'NL: {keynl} \n US:{keyus} \n AUS:{keyaus}')

whatnext = input("""
What would you like to do? (All options require you to rename the key!)
[0] Send key(s) via email?
[1] Copy key(s) to clipboard
[2] Just rename US key
[3] Just rename NL key
[4] Just rename AUS key
""")
email = input("Enter recipient's email:")
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
    message += 'Your VPN keys:' + str('\n')
    message += 'US:' + '\n' + str(keyus)
    message += 'NL:' + '\n' + str(keynl)
    message += 'AUS:' + '\n' + str(keyaus)
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
        responseus = requests.put((f'{api_keyus}+/access-keys/{idus}/{name}'),verify=False)
    if choice == "2": #NL
        responsenl = requests.put((f'{api_keynl}/access-keys/{idnl}/{name}'),verify=False)
    if choice == "3": #AUSSIE
        responseaus = requests.put((f'{api_keyaus}+/access-keys/{idaus}/{name}'),verify=False)
    if choice == "4": #ALL KEYS
        responseus = requests.put((f'{api_keyus}+/access-keys/{idus}/{name}'),verify=False)
        responsenl = requests.put((f'{api_keynl}/access-keys/{idnl}/{name}'),verify=False)
        responseaus = requests.put((f'{api_keyaus}+/access-keys/{idaus}/{name}'),verify=False)

if whatnext == "1": #[1] Copy key to clipboard
    pyperclip.copy(finalkeystosend)
    responseus = requests.put((f'{api_keyus}/access-keys/{idus}/{name}'),verify=False)
    responsenl = requests.put((f'{api_keynl}/access-keys/{idnl}/{name}'),verify=False)
if whatnext == "2": #[2] Just rename the US key
    responseus = requests.put((f'{api_keyus}/access-keys/{idus}/{name}'),verify=False)
if whatnext == "3": #[3] Just rename the NL key
    responsenl = requests.put((f'{api_keynl}/access-keys/{idnl}/{name}'),verify=False)
if whatnext == "4":
    responseaus = requests.put((f'{api_keyaus}/access-keys/{idaus}/{name}'),verify=False)
