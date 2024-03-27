import sys
print("Preparing Libraries (1/2)",end="\r")
import requests
print("Preparing Libraries (2/2)")
import os
#This is for updating Basic Utilities source code
print("Checking connection...")
try:
    rtest = requests.get("https://www.google.com")
except (requests.ConnectionError,requests.HTTPError):
    print("ERROR: You are not connected to the internet. Please try this again when you are")
    sys.exit(1)

print("Getting Data (1/2) [Changelog]",end="\r")
try:
    chl = requests.get("https://raw.githubusercontent.com/Enderbyte-Programs/Basic-Utilities/main/changelog.txt").text.splitlines()[-1].split(" ")
    while '' in chl:
        chl.remove('')
    ver = chl[0].replace(":","")
    
except (requests.ConnectionError,requests.HTTPError):
    print("An unexpected connection error occured.")
    sys.exit(1)
print("Getting Data (2/2) [Data]             ")

try:
    dat = requests.get("https://raw.githubusercontent.com/Enderbyte-Programs/Basic-Utilities/main/BasicUtilities.py").text.splitlines()
except (requests.ConnectionError,requests.HTTPError):
    print("An unexpected connection error occured.")
    sys.exit(1)

ins = input(f"The newest version of Basic Utilities source is {ver}. Do you want to download (and replace the old version)?")
if ins.lower().startswith("y"):
    try:
        print("Replacing file")
        with open("BasicUtilities.py","w+") as f:
            for line in dat:
                f.write(line+"\n")
    except:
        print("A file error occured.")
        sys.exit(2)
input("All finished. Press enter to exit")