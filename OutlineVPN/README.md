# OutlineVPN

Outline VPN is a free and open-source tool that deploys Shadowsocks servers on multiple cloud service providers. The software suite also includes client software for multiple platforms. Outline was developed by Jigsaw, a technology incubator created by Google.

## Download & Installation

```bash
sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"
```
Launch OutlineVPN-Manager and paste the result into the "Add New Server" box

## Automation
### I created a <a href="https://github.com/rhijjawi/Digisec.tools/blob/master/OutlineVPNKeygen.py">script</a> to automate the creation and emailing of private keys to customers
To run the sript, install Python and it's IDE, then find the python program above.
Open the python file in your favorite text editor, and replace the following lines with your servers API key.
```python
api_keynl = 'YourAPIKey' #Replace your API key with the API key given to you by Outline-Manager || This key should be the Netherlands
api_keyus = 'YourAPIKey' #Replace your API key with the API key given to you by Outline-Manager || This key should be the United States
api_keyaus = 'YourAPIKey' #Replace your API key with the API key given to you by Outline-Manager || This key should be the Australia
```

## Contributions
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
