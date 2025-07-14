import os
import sys
import time
import re
import random
import uuid
import json
import subprocess
import pycurl
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from random import choice as race
from string import digits, ascii_letters
import urllib.parse
import base64
import platform
import webbrowser
import datetime
import requests

# ===================================================================
# Color Definitions
# ===================================================================

class NebulaColors:
    def __init__(self):
        self.W = '\x1b[97;1m'
        self.R = '\x1b[91;1m'
        self.G = '\x1b[92;1m'
        self.Y = '\x1b[93;1m'
        self.B = '\x1b[94;1m'
        self.P = '\x1b[95;1m'
        self.C = '\x1b[96;1m'
        self.N = '\x1b[0m'

# ===================================================================
# Banners
# ===================================================================

def pro_banner():
    return ('''
\x1b[1;96m
███████╗██╗  ██╗ █████╗ ██╗  ██╗███████╗███████╗███╗   ██╗
██╔════╝██║  ██║██╔══██╗██║  ██╔╝██╔════╝██╔════╝████╗  ██║
███████╗███████║███████║█████╔╝ █████╗  █████╗  ██╔██╗ ██║
╚════██║██╔══██║██╔══██║██╔ ═██╗ ██╔══╝  ██╔══╝  ██║╚██╗██║
███████║██║  ██║██║  ██║██║  ██╗███████╗███████╗██║ ╚████║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
\x1b[1;95m╔═══════════════════════════════════════════════════════╗
\x1b[1;95m║\x1b[1;97m                ✦  𝗧𝗢𝗢𝗟 I𝗡𝗙𝗢 𝗣𝗔𝗡𝗘𝗟  ✦                  \x1b[1;95m║
\x1b[1;95m╚═══════════════════════════════════════════════════════╝
\x1b[1;96m   ➤ \x1b[1;97mCreator        : \x1b[1;96mShaheen Alam⚠️
\x1b[1;96m   ➤ \x1b[1;97mOperated By    : \x1b[1;92mVirus
\x1b[1;96m   ➤ \x1b[1;97mTool Access    : \x1b[1;93mFREE
\x1b[1;96m   ➤ \x1b[1;97mCurrent Version: \x1b[1;95m2.2
\x1b[1;92m─────────────────────────────────────────────────────────''')

def linex():
    color = NebulaColors()
    print(f'  {color.P}╔═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╗')
    print(f'  {color.P}║    {color.Y}★ PREMIUM TOOL INTERFACE ★    {color.P}║')
    print(f'  {color.P}╚═━─━━━━━━━━━━━━━━━━━━━━━━━━━━━━─━═╝{color.N}')

def clear():
    os.system('clear')
    print(pro_banner())

# ===================================================================
# Your remaining logic (unchanged)
# ===================================================================

# Example: welcome screen
print('\x1b[1;92m[~] WELCOME to ALPHA-X Institute 🚀✨\x1b[0m')
print('\x1b[1;96m[~] CREATOR: MR Likhon⚠️\x1b[0m')
os.system('xdg-open https://t.me/AlphaX_Institute')
time.sleep(2)

# Your user agent generator, device info, etc.
# No changes needed if not using SubscriptionManager!

# The rest of your cracker code
# For example:

class ASIMCracker:
    def __init__(self):
        self.oks = []
        self.cps = []
        self.loop = 0
        self.color = NebulaColors()
        self.user_agents = [ # simple pool
            'Mozilla/5.0 (Linux; Android 12; SM-A127F Build/SP1A...)',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X)...',
            # Add more or generate dynamically
        ]

    def old_menu(self):
        clear()
        print(f'{self.color.P}╔═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╗')
        print(f'{self.color.P}║         {self.color.Y}★ OLD ACCOUNT CRACKER ★         {self.color.P}║')
        print(f'{self.color.P}╠═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╣')
        print(f'{self.color.P}║ {self.color.C}[1] {self.color.G}CRACK 2009 ACCOUNTS  {self.color.Y}🔓           {self.color.P}║')
        print(f'{self.color.P}║ {self.color.C}[2] {self.color.G}CRACK 2009-2013 ACCOUNTS {self.color.Y}🔑      {self.color.P}║')
        print(f'{self.color.P}║ {self.color.C}[0] {self.color.R}⇦ BACK TO MAIN MENU   {self.color.B}🏠         {self.color.P}║')
        print(f'{self.color.P}╚═━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━═╝')
        choice = input(f'  {self.color.C}\x1b[1;96m ➤ Choose: {self.color.W}').strip()
        if choice in ('1', '01'):
            print('Start 2009 cracking...')
            # call your cracking logic
        elif choice in ('2', '02'):
            print('Start 2009-2013 cracking...')
            # call your cracking logic
        elif choice in ('0', '00'):
            sys.exit()
        else:
            print(f'\n  {self.color.R}⚠️ Invalid choice!')
            time.sleep(2)
            self.old_menu()

# ===================================================================
# Entry Point
# ===================================================================

if __name__ == '__main__':
    try:
        cracker = ASIMCracker()
        cracker.old_menu()
    except KeyboardInterrupt:
        print('\n\x1b[91;1m   ➤ Stopped\x1b[97;1m')
        sys.exit()
    except Exception as e:
        print(f'\n\x1b[91;1m   ➤ Error: {str(e)}\x1b[97;1m')
        sys.exit()

