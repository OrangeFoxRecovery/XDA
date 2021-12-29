#!/usr/bin/env python3

# Variables
FDEVICE = ""                # Device Codename
DEVICE_COMMON_NAME = ""     # Device Common Name
BUILD_DATE = ""             # Date of the Build
XDA_INIT_DATA = ""          # Date when the XDA Thread was Created
DOWNLOAD_LINK = ""          # Download Link of your Build
FOX_BUILD_TYPE = ""         # Beta / Stable / Unofficial

# Output File
OUTFILE = "output.txt"

# Open the Output File in Write Mode
FILE = open(OUTFILE,w)

# Head Part
HEAD="""
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
