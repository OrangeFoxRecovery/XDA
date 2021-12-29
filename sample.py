#!/usr/bin/env python3

# Variables
FDEVICE = ""                # Device Codename
DEVICE_COMMON_NAME = ""     # Device Common Name
RELEASE_DATE = ""           # Date of Release of the Build
XDA_INIT_DATA = ""          # Date when the XDA Thread was Created
DOWNLOAD_LINK = ""          # Download Link of your Build
FOX_BUILD_TYPE = ""         # Beta / Stable / Unofficial
FOX_VERSION = ""            # The Full Version of the Release. (eg. "R11.1_1")

FOX_SOURCES = "https://gitlab.com/OrangeFox"
SOURCE_CHANGELOG = "https://wiki.orangefox.tech/changelog"
NEWS_CHANNEL = ""           # Telegram Updates Channel
SUPPORT_CHAT = ""           # Telegram Support Chat

DEVICE_TREE = ""            # The Link of the Device Tree
KERNEL = ""                 # The Link of the Kernel (Source or Prebuilt)

MAINTAINER = ""             # Name of the Maintainer
MAINTAINER_XDA_URL = ""     # XDA URL of the Maintainer
DONATION_URL = ""           # Your Donation Link. Leave Blank if None.

# Output File
OUTFILE = "output.txt"

# Import Required Libraries
import sys

# Open the Output File in Write Mode
FILE = open(OUTFILE,w)

# Head Part
HEAD = """
[CENTER][COLOR=rgb(251, 160, 38)][SIZE=7]OrangeFox Recovery Project[/SIZE][/COLOR]
[IMG]https://image.ibb.co/cTMWux/logo.jpg[/IMG][/CENTER]
[CODE]
/*
* Your warranty is now void.
*
* We're not responsible for bricked devices, dead SD cards,
* thermonuclear war, or you getting fired because the alarm app failed. Please
* do some research if you have any concerns about features included in this recovery
* before flashing it! YOU are choosing to make these modifications, and if
* you point the finger at us for messing up your device, we will laugh at you.
*
*/
[/CODE]
[CENTER][SIZE=5]OrangeFox is [URL='https://www.gnu.org/philosophy/free-sw.html']FREE SOFTWARE[/URL][/SIZE][/CENTER]
"""

# Information
INFO = """
ℹ️ [B][SIZE=4]Information[/SIZE][/B]
Status: """ + FOX_BUILD_TYPE + """
Version: """ + FOX_VERSION + """
Release Date: """ + RELEASE_DATE + """
"""

# Sources
SOURCES = """
ℹ️[B] Sources[/B]
Source Code: [U][URL]""" + FOX_SOURCES + """[/URL][/U]
Device Tree: [URL]""" + DEVICE_TREE + """[/URL]
Kernel: [URL]"""+ KERNEL + """[/URL]
Template Generator: https://github.com/OrangeFoxRecovery/XDA.git
"""

# Downloads
DOWNLOADS = """
[SIZE=4]⬇️[/SIZE][B][SIZE=4]Downloads:[/SIZE][/B]
[URL='"""+ DOWNLOAD_LINK +"""'][U]"""+ DOWNLOAD_LINK +"""[/U][/URL]
"""

# Installation
INSTALLATION = """
[B][SIZE=4]📲 Installation:[/SIZE][/B]
[URL='https://wiki.orangefox.tech/en/guides/installing_orangefox'][U]https://wiki.orangefox.tech/en/guides/installing_orangefox[/U][/URL]
"""

# Documentation
DOCUMENTATION = """
[B][SIZE=4]📚 Documentation (FAQ):[/SIZE][/B]
[URL='https://wiki.orangefox.tech/en/guides'][U]https://wiki.orangefox.tech/en/guides[/U][/URL]
"""

# Donations
if DONATION_URL=="":
    DONATION_URL="https://t.me/Sushrut1101"
DONATIONS = """
[B][SIZE=4]💰 Donations:[/SIZE][/B]
[U][URL]"""+ DONATION_URL +"""[/URL][/U]
"""

# Source Changelogs
if FOX_SOURCES=="https://gitlab.com/OrangeFox":
    SOURCE_CHANGELOG = "https://wiki.orangefox.tech/changelog"
CHANGELOG = """
[B][SIZE=4]📒 Source changelog:[/SIZE][/B]
[URL='""" + SOURCE_CHANGELOG + """'][U]""" + SOURCE_CHANGELOG + """[/U][/URL]
"""

# Telegram Channels
if FOX_BUILD_TYPE.lower()=="stable":
    NEWS_CHANNEL="https://t.me/OrangeFoxUpdates"
    SUPPORT_CHAT="https://t.me/OrangeFoxChat"
elif FOX_BUILD_TYPE.lower()=="beta":
    NEWS_CHANNEL="https://t.me/OrangeFoxBetaTracker"
    SUPPORT_CHAT="https://t.me/OrangeFoxBeta"
elif FOX_BUILD_TYPE.lower()=="unofficial":
    if NEWS_CHANNEL=="":
        NEWS_CHANNEL="https://t.me/ROMRecoveryNews"
    if SUPPORT_CHAT=="":
        SUPPORT_CHAT="https://t.me/OrangeFoxRecoveryUnofficial"
TG_CHANNELS = """
[B][SIZE=4]📣 Telegram Channels:[/SIZE][/B]
News - [URL='""" + NEWS_CHANNEL + """'][U]""" + NEWS_CHANNEL + """[/U][/URL]
Support Chat - [URL='""" + SUPPORT_CHAT + """'][U]""" + SUPPORT_CHAT + """[/U][/URL]
"""

# OrangeFox App
APP = """
🦊[B][SIZE=4] OrangeFox App:[/SIZE][/B]
https://[URL='http://app.orangefox.tech/'][U]https://app.orangefox.tech/[/U][/URL]
"""

# XDA DevDB Information
XDA_DEV_INFO = """
[B][U]XDA : DevDB Information[/U]
OrangeFox Recovery Project, Tool/Utility for """ + FDEVICE + """ (""" + DEVICE_COMMON_NAME + """)
"""

# Contributions
CONTRIBUTIONS = """
[U]Contributors[/U][/B]
[URL='"""+MAINTAINER_XDA_URL+"""']"""+MAINTAINER+"""[/URL], [URL='https://forum.xda-developers.com/m/Sushrut1101.10817501/']Sushrut Gupta[/URL] ,[URL='https://forum.xda-developers.com/member.php?u=5850987']DarthJabba9[/URL], [URL='https://forum.xda-developers.com/member.php?u=9034403']MrYacha[/URL]
"""

# Credits
CREDITS = """
[B]Credits[/B]
* TeamWin - for TWRP
* The OrangeFox Team - for your hard work
* All our testers - for your patience and help
* [USER=10817501]@Sushrut1101[/USER] - For this XDA Template
* [URL='"""+MAINTAINER_XDA_URL+"""']"""+MAINTAINER+"""[/URL] - Maintainer
"""

# The Output
OUTPUT = HEAD + '\n' + INFO + '\n' + SOURCES + '\n' + DOWNLOADS + '\n' + INSTALLATION + '\n' + DOCUMENTATION + '\n' + DONATIONS + '\n' + CHANGELOG + '\n' + TG_CHANNELS + '\n' + APP + '\n' + XDA_DEV_INFO + '\n' + CONTRIBUTIONS + '\n' + CREDITS + '\n'

# Write the Output to the Outfile
FILE.write(OUTPUT)

# Close the File
FILE.close()

# Print a Message
print("DONE! You can now Find the Output in:",OUTFILE,'\n')

# Exit
sys.exit()
