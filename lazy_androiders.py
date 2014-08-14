#!/usr/bin/env python

"""Lazy Androiders is a simple script that downloads and sets ups the android tools for you. Easy Peezy! No more hassles!"""
 
__author__ = "Alexandre Juca"
__email__  = "corextechnologies@gmail.com"
__license__= """
Copyright (c) 2013-2014 Alexandre Juca <corextechnologies@gmail.com>
 
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
USA

"""

import sys
import os
import platform
import urllib.request as urlreq



__VERSION__ = 0.1
__AUTHOR__ = "Alexandre Juca corextechnologies@gmail.com"
__INFO__ = "Lazy Android - The lazy Android Developers mate."

__ADT_LINUX_32__ = "http://dl.google.com/android/adt/adt-bundle-linux-x86-20140702.zip"
__ADT_LINUX_64__ = "http://dl.google.com/android/adt/adt-bundle-linux-x86_64-20140702.zip"

__INSTALL_PATH__ = "/lazy_android/"
__FILENAME_32__ = "adt-bundle-linux-x86-20140702.zip"
__FILENAME_64__ = "adt-bundle-linux-x86_64-20140702.zip"
__FILENAME_SDK__ = "android-sdk_r23.0.2-linux.tgz"

__SDK_TOOLS__ = "http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz" #both 32 bit and 64bit packages included in this package


def progress():
    print()#working on this
    
def is_86bit():

    if platform.machine().endswith('86'):
        return True
    else:
        return False
def makeAndroidPath():
    try:
        if  os.path.exists(__INSTALL_PATH__) == True:
            
        else:
            os.mkdir(__INSTALL_PATH__)
    except Exception as e:
        print("Directory Error: ", e)

def isLinux():

    if platform.system().endswith('Linux'):
        return True
    else:
        return False


def handleDownloads(option, systemVersion):
    try:
        if option == 1 and systemVersion == 32:
            urlreq.urlretrieve(__ADT_LINUX_32__, __FILENAME_32__, progress())
        if option == 1 and systemVersion == 64:
            urlreq.urlretrieve( __ADT_LINUX_64__, __FILENAME_64__, progress())
        if option == 2 and systemVersion == 64:
            urlreq.urlretrieve( __ADT_LINUX_64__, __FILENAME_SDK__, progress())
        if option == 2 and systemVersion == 32:
            urlreq.urlretrieve( __ADT_LINUX_64__, __FILENAME_SDK__, progress())
        
    except Exception as e:
        print(e)
        return 


def askTypeOfDownload(systemVersion):
    sysVersion = systemVersion
    option = input("Type 1 for ATD Bundle or 2 for SDK Tools only: ")
    print()
    try:
        makeAndroidPath()
    except Exception as e:
        print("Error :", e)
        return
        
    try:
        option = int(option)
        
        if type(option) == int and sysVersion == 32:
            if option == 1:
                print("Awesome! Downloading the 32 bit ADT Bundle for you, please wait.")
                
                handleDownloads(option, sysVersion)
            else:
                 print("Awesome! Downloading the 32 bit SDK Tools for you, please wait.")
                 handleDownloads(option, sysVersion)
        if type(option) == int and sysVersion == 64:
             if option == 1:
                print("Awesome! Downloading 64 bit ADT Bundle for you, please wait.")
                handleDownloads(option, sysVersion)
             else:
                 print("Awesome! Downloading the 64 bit SDK Tools for you, please wait.")
                 handleDownloads(option, sysVersion)
                
    except Exception as e:
        print("That's not a number, try again.", e)
        askTypeOfDownload(sysVersion)

def main():
    print(__INFO__)
    print(__AUTHOR__)
    print(__VERSION__)
    
    systemVersion = 32

    print("Getting os....")
    if isLinux() == True:
        print("Yep system is Linux.")
        if is_86bit() == True:
            print("OS architecture is 32bit | x86 I am downloading the x86 version of android for you.")
            askTypeOfDownload(systemVersion)
        else:
            systemVersion = 64
            print("OS architecture is 64bit | x64 I am downloading the x64 version of android for you.")
            askTypeOfDownload(systemVersion)
            
    else:
        print("This is not a linux system")
    

if __name__ == '__main__':
    main()
   
    
    
