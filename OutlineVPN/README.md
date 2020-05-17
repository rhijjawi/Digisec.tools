# OutlineVPN

Outline VPN is a free and open-source tool that deploys Shadowsocks servers on multiple cloud service providers. The software suite also includes client software for multiple platforms. Outline was developed by Jigsaw, a technology incubator created by Google.

## Download & Installation

```bash
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"
```

Launch OutlineVPN-Manager and paste the result into the "Add New Server" box

## Automation
### I created a script to automate the creation and emailing of private keys to customers
```python
import smtplib 
import requests 
import json 
import pyperclip 
api_keynl = 'YourAPIKey'
api_keyus = 'YourAPIKey'
api_keyaus = 'YourAPIKey'
```

## Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
