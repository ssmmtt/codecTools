import base64
import hashlib
import json
import os
import time
import tkinter as tk
import urllib.parse
from io import BytesIO
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

import pyperclip
from PIL import Image, ImageTk

from tabview import TabView

# 编译打包
# pyinstaller.exe -w -F -i .\ico.ico .\main.py

ico = 'AAABAAEAMDAAAAEAIACoJQAAFgAAACgAAAAwAAAAYAAAAAEAIAAAAAAAACQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACseBDLLixHs25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv+rdA3HGBACHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADJiRDq25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv+yeg/QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALR6D9PblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/bUsJfgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABALARTblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARC4FT9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/wwIAQ4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhFgMm25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAzYwR8NuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/5K9J//vz4///////////////////////////////////////9eO//9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/21KCX4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS////////////25YS/9uWEv/blhL/25YS//z26///////////////////////////////////////////////////////////////////////4ac6/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/3p8m////////////25YS/9uWEv/w1J3////////////////////////////y2an/3p0i/9uWEv/blhL/25YS/+KoO//25sb////////////////////////////blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAABUOAhnblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/3p8m////////////25YS//79+v/////////////////y2Kb/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv//////////////////////6L5t/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAANuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/3p8m/////////////////////////////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/////////////////+7OkP/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/snoP0AAAAAAAAAAAAAAAANuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/3p8m///////////////////////68N3/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/////////////////gpDP/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/wAAAAAAAAAAd1IKi9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/3p8m//////////////////z26v/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/////////////////25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/xgRAhsAAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/3p8m////////////////////////////////////////////3p4j/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/////////////fnx/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/6VwDb8AAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS//79+///////////////////////////////////////25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/+rAcf//////+u/a/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv95UwqN25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv+ocw7E25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/XkhL625YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv+xeA/O25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv+CWQmX25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8EAwAF25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS////////////25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv//////////////////////////////////////7MeC/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS////////////8NSe/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS//fmx////////////////////////////////////////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/8uLEewAAAAAnW0NuNuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS//vy4////////////92dIv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/ls1T/57lg/+e5YP/nuWD//////////////////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/yseBDIAAAAAAQEAAduWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/////////////////blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv///////////////////////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/wAAAAAAAAAAAAAAANuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/////////////////57tm/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/////////////////////////////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/yYkQ6gAAAAAAAAAAAAAAAEQuBlDblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS///////////////////////enyf/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/y2Kj//////////////////vz4/9uWEv///////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAAAAAAADblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/+/fr///////////////////////Tft//blhL/25YS/9uWEv/blhL/25YS/9uWEv/kslH//fny///////////////////////sx4D/25YS/9uWEv///////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAAAAAAAAfFQMk25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS////////////////////////////////////////////////////////////////////////////+/Pj/9uWEv/blhL/25YS/9uWEv///////////9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/9+fI/////////////////////////////////////////////vz4/+SvSv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/7R8D9IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/dnCD/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADEiBDnblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACJXgyf25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8RCwETAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqXQOxtuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/0QuBk8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJVmDK7blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/IRYDJgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxIgQ525YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/zYwR8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfFQMk25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEQuBk/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/FQ4CGQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQEAAZ1sDbjblhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/25YS/9uWEv/blhL/d1IKigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAwAFglkJl7F4D87XkhL6qHMOxHlTCo0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//4AA//8AAP/+AAA//wAA//gAAA//AAD/4AAAA/8AAP/AAAAB/wAA/wAAAAD/AAD+AAAAAD8AAPwAAAAAPwAA/AAAAAAfAAD4AAAAAA8AAPAAAAAABwAA8AAAAAAHAADgAAAAAAMAAMAAAAAAAwAAwAAAAAABAADAAAAAAAEAAIAAAAAAAAAAgAAAAAAAAACAAAAAAAAAAIAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAIAAAAAAAAAAgAAAAAAAAACAAAAAAAAAAIAAAAAAAQAAwAAAAAABAADAAAAAAAMAAOAAAAAAAwAA4AAAAAAHAADwAAAAAAcAAPgAAAAADwAA+AAAAAAfAAD8AAAAAB8AAP4AAAAAPwAA/wAAAAB/AAD/gAAAAf8AAP/gAAAD/wAA//AAAA//AAD//AAAH/8AAP//AAD//wAA///4H///AAA='
with open("icon.ico", "wb+") as tmp:
    tmp.write(base64.b64decode(ico))


# 在body中生成widget的函数，返回的widget将被添加到tabview的body中
def create_body():
    global body

    toolframe = Frame(body)
    toolframe.pack(fill=BOTH, expand=True)
    gui = ToolsGui(toolframe)
    gui.set_init_window()

    return toolframe


# 点击选项卡时的回调
def select(index):
    print("current selected -->", index)


# 删除选项卡时的回调，如果返回False将不会删除
def remove(index):
    print("remove tab -->", index)
    # if messagebox.askokcancel("标题", "确定要关闭该选项卡吗？"):
    return True
    # else:
    #     return False


class ToolsGui():
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        self.bs64image = None

    def md5_upper_event(self, event):
        self.str_trans_to_md5(True)

    def fast_copy(self):
        data = self.result_data_Text.get(0.0, END).strip()
        pyperclip.copy(data)

    # 设置窗口
    def set_init_window(self):
        # 左侧视图
        self.init_window_name.update()
        print(self.init_window_name.winfo_width())
        frm1 = Frame(self.init_window_name)
        frm1.pack(fill=BOTH, side=LEFT, expand=True)

        self.init_data_label = Label(frm1, text="待处理数据", font=("宋体", 15, "bold"), height=2, bg='dodgerblue')
        self.init_data_label.pack(fill=X)

        self.init_data_Text = ScrolledText(frm1, undo=True)  # 原始数据录入框
        self.init_data_Text.pack(fill=BOTH, expand=True)
        self.log_label = Label(frm1, text="日志", font=("宋体", 15, "bold"), height=2, bg='dodgerblue')
        self.log_label.pack(fill=X)
        self.log_data_Text = ScrolledText(frm1, )  # 日志框
        self.log_data_Text.pack(fill=BOTH, expand=True)

        # 中间按钮试图
        frm2 = Frame(self.init_window_name)
        frm2.pack(fill=BOTH, side=LEFT, expand=True)
        # md5计算
        self.str_trans_to_md5_button = Button(frm2, text="MD5计算\n（右键点击大写）", bg="limegreen",
                                              command=self.str_trans_to_md5)
        self.str_trans_to_md5_button.bind('<Button-3>', self.md5_upper_event, add=True)
        self.str_trans_to_md5_button.pack(fill=BOTH, expand=True)
        # base64编码
        self.str_trans_to_bs64_button = Button(frm2, text="base64编码", bg="gold",
                                               command=self.str_trans_to_bs64)
        self.str_trans_to_bs64_button.pack(fill=BOTH, expand=True)
        # base64解码
        self.bs64_trans_to_str_button = Button(frm2, text="base64解码", bg="limegreen",
                                               command=self.bs64_trans_to_str)
        self.bs64_trans_to_str_button.pack(fill=BOTH, expand=True)
        # url编码
        self.str_trans_to_url_button = Button(frm2, text="URL编码", bg="gold",
                                              command=self.str_trans_to_url)
        self.str_trans_to_url_button.pack(fill=BOTH, expand=True)
        # url解码
        self.url_trans_to_str_button = Button(frm2, text="URL解码", bg="limegreen",
                                              command=self.url_trans_to_str)
        self.url_trans_to_str_button.pack(fill=BOTH, expand=True)
        # unicode转中文
        self.unicode_trans_to_zh_button = Button(frm2, text="Unicode转中文", bg="gold",
                                                 command=self.unicode_trans_to_zh)
        self.unicode_trans_to_zh_button.pack(fill=BOTH, expand=True)
        # json格式化
        self.str_trans_to_json_button = Button(frm2, text="Json格式化", bg="limegreen",
                                               command=self.str_trans_to_json)
        self.str_trans_to_json_button.pack(fill=BOTH, expand=True)

        # base64转图片
        self.bs64_trans_to_pic_button = Button(frm2, text="base64转图片", bg="gold",
                                               command=self.bs64_trans_to_pic)
        self.bs64_trans_to_pic_button.pack(fill=BOTH, expand=True)

        # 图片转base64
        self.pic_trans_to_bs64_button = Button(frm2, text="图片转base64", bg="limegreen",
                                               command=self.pic_trans_to_bs64)
        self.pic_trans_to_bs64_button.pack(fill=BOTH, expand=True)

        # chrome请求头转换
        self.header_trans_to_json_button = Button(frm2, text="请求头转Json", bg="gold",
                                                  command=self.header_trans_to_json)
        self.header_trans_to_json_button.pack(fill=BOTH, expand=True)

        # 右侧结果试图
        frm3 = Frame(self.init_window_name)
        frm3.pack(fill=BOTH, side=RIGHT, expand=True)
        self.result_data_label = Label(frm3, height=2, text="输出结果", font=("宋体", 15, "bold"), bg="dodgerblue")
        self.result_data_label.pack(fill=X)
        copybtn = Button(self.result_data_label, text='一键复制', command=self.fast_copy)
        copybtn.pack(side=RIGHT)
        self.result_data_Text = ScrolledText(frm3)  # 处理结果展示
        self.result_data_Text.pack(fill=BOTH, expand=True)

    # 功能函数
    def str_trans_to_md5(self, upper=False):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                res = myMd5.hexdigest()
                if upper:
                    res = res.upper()
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def str_trans_to_bs64(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                res = base64.b64encode(src)
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def bs64_trans_to_str(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                res = base64.b64decode(src).decode()
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def str_trans_to_url(self):
        src = self.init_data_Text.get(0.0, END).strip().encode()
        if src:
            try:
                res = urllib.parse.quote(src)
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def url_trans_to_str(self):
        src = self.init_data_Text.get(0.0, END).strip()
        if src:
            try:
                res = urllib.parse.unquote(src)
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def unicode_trans_to_zh(self):
        src = self.init_data_Text.get(0.0, END).strip()
        print(src, type(src))
        if src:
            try:
                src = src.replace('\\\\u', '\\u')
                res = src.encode().decode('unicode_escape')
                print(res, type(res))
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def str_trans_to_json(self):
        src = self.init_data_Text.get(0.0, END).strip()
        if src:
            try:
                tmp = eval(src)
                res = json.dumps(tmp, ensure_ascii=False, indent=4)
                self.write_res_to_text(res)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def pic_trans_to_bs64(self):
        try:
            picpath = filedialog.askopenfilename(title='选择图片文件',
                                                 filetypes=[('PNG图片', '*.png'), ('JPG图片', ('*.jpg', '*.jpe', '*.jpeg')),
                                                            ('BMP图片', '*.bmp'), ('所有文件', '*')])
            if picpath:
                self.init_data_Text.delete(1.0, END)
                self.init_data_Text.insert(1.0, '图片路径：\n' + picpath)
                with open(picpath, 'rb') as handle:
                    image_base64 = str(base64.b64encode(handle.read()), encoding='utf-8')
                    self.write_res_to_text(image_base64)
        except Exception as e:
            self.result_data_Text.delete(1.0, END)
            self.write_log_to_text("[ERROR]:%s" % e)

    def bs64_trans_to_pic(self):
        src = self.init_data_Text.get(0.0, END).strip()
        if src:
            try:
                binary_data = base64.b64decode(src)
                # print(binary_data)
                img_data = BytesIO(binary_data)
                img_open = Image.open(img_data)
                self.bs64image = ImageTk.PhotoImage(img_open)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.image_create(END, image=self.bs64image)
            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    def header_trans_to_json(self):
        src = self.init_data_Text.get(0.0, END).strip()
        if ': ' in src:
            try:
                lines = src.split('\n')
                h = {}
                for line in lines:
                    if line:
                        l = line.split(': ')
                        h[l[0]] = l[1]
                res = json.dumps(h, ensure_ascii=False, indent=4, separators=(',', ': '))
                self.write_res_to_text(res)

            except Exception as e:
                self.result_data_Text.delete(1.0, END)
                self.write_log_to_text("[ERROR]:%s" % e)

    # 结果展示
    def write_res_to_text(self, res):
        # 输出到界面
        self.result_data_Text.delete(1.0, END)
        self.result_data_Text.insert(1.0, res)
        self.write_log_to_text("[INFO]:转换成功！")

    # 日志动态打印
    def write_log_to_text(self, logmsg):
        current_time = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
        logmsg_in = str(current_time) + logmsg + "\n"  # 换行
        self.log_data_Text.configure(state='normal')
        self.log_data_Text.insert(END, logmsg_in)
        self.log_data_Text.see(END)
        self.log_data_Text.configure(state='disabled')


# ----------------------- 使用示例 ----------------------------
root = tk.Tk()
root.title('编码工具集')
root.geometry("1200x640")
root.iconbitmap("icon.ico")
os.remove("icon.ico")
tab_view = TabView(root, generate_body=create_body,
                   select_listen=select, remove_listen=remove)

toolframe = Frame(tab_view.body)
toolframe.pack(fill=BOTH, expand=True)
gui = ToolsGui(toolframe)
gui.set_init_window()
tab_view.add_tab(toolframe, '编码工具')
body = tab_view.body

tab_view.pack(fill=BOTH, expand=True, pady=2)

root.mainloop()
