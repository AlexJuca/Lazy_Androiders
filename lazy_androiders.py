#!/usr/bin/env python

"""Lazy Androiders is a tool that downloads and sets ups the android tools for you. Easy Peezy! No more hassles!"""

__author__ = "Alexandre Juca"
__email__ = "corextechnologies@gmail.com"
__license__ = """
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


import os
import platform
import urllib.request as urlreq
import shutil
import tarfile as tarfile
import zipfile
import subprocess as sb


__VERSION__ = "Version 1.0"
__AUTHOR__ = "Alexandre Juca <corextechnologies@gmail.com>"
__INFO__ = "Lazy Android - The lazy Android Developers mate."
#########################################################################################
__ADT_LINUX_32__ = "http://dl.google.com/android/adt/adt-bundle-linux-x86-20140702.zip"
__ADT_LINUX_64__ = "http://dl.google.com/android/adt/adt-bundle-linux-x86_64-20140702.zip"
#########################################################################################
__ADT_WIN_32__ = "http://dl.google.com/android/adt/adt-bundle-windows-x86-20140702.zip"
__ADT_WIN_64__ = "http://dl.google.com/android/adt/adt-bundle-windows-x86_64-20140702.zip"
#########################################################################################
__INSTALL_PATH__ = "lazy_androiders/"
__FILENAME_32__ = "adt-bundle-linux-x86-20140702.zip"
__FILENAME_64__ = "adt-bundle-linux-x86_64-20140702.zip"
__FILENAME_SDK__ = "android-sdk_r23.0.2-linux.tgz"
#########################################################################################
__JVM_PATH__ = "/usr/lib/jvm/"
__WIN_JVM_PATH__ = "C:/Program Files/Java/"
#########################################################################################
#both 32 bit and 64bit packages are included in this package
__SDK_TOOLS__ = "http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz"
#Downloading the executable which is the recommened way to install the sdk tools for windows
__WIN_SDK_TOOLS = "http://dl.google.com/android/installer_r23.0.2-windows.exe"


future_path = ""


def installeclipse():
    sb.call(['apt-get', 'install', 'eclipse'])
    print("installed eclipse")
    main()


def extractfile(future_path):
    if future_path.endswith('.zip'):
        print("Unzipping to : "+future_path+" patience will be needed.")
        zipfile.extractall(future_path, None, None)
    if future_path.endswith('.tgz'):
        print("Extracting file to : "+future_path+" patience will be needed.")
        tarfile.extractall(future_path, None)
    else:
        print("Format seems wrong....")
        return


def checkjvm(op_system):
    print("Checking if JVM is installed....")
    #XXX: I could rather check the windows registry for the JDK installation
    #This might give an error on 64 bit machines with a 32 bit jdk if that's even possisble
    if os.path.exists(__JVM_PATH__) or os.path.exists(__WIN_JVM_PATH__):
            print("Super! JVM seems to be here..Next step please!")
            return True
    else:
            print("Bummer! JVM is not installed but I'll download that right away for ye!")
            print("#########################################################")
            return False


def progress(chunk, max_size, total_size):
        print("working... "+str(chunk))#working on this


def is_86bit():
    if platform.machine().endswith('86'):
        return True
    else:
        return False


def makeandroidpath():
    try:
        if os.path.exists(__INSTALL_PATH__):
            print("directory exists....")
        else:
            os.mkdir(__INSTALL_PATH__)
    except Exception as e:
        print("Directory Error: ", e)


def iswindows():
    if platform.system().endswith('Windows'):
        print("You're a Bill Gates fanatic..Got Windows for sure! :)")
        return True
    else:
        return False


def islinux():
    if platform.system().endswith('Linux'):
        print("Alrighty, seems to me you have a Linux baby! Nice! :) ")
        return True

    else:
        return False


def handle_win_downloads(option, systemversion):
    try:
        if option == 1 and systemversion == 32:
            future_path = __INSTALL_PATH__+__FILENAME_32__
            urlreq.urlretrieve(__ADT_WIN_32__, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)
        if option == 1 and systemversion == 64:
            future_path = __INSTALL_PATH__+__FILENAME_64__
            urlreq.urlretrieve(__ADT_WIN_64__, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)
        if option == 2 and systemversion == 64:
            future_path = __INSTALL_PATH__ + __FILENAME_SDK__
            urlreq.urlretrieve(__WIN_SDK_TOOLS, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)
        if option == 2 and systemversion == 32:
            future_path = __INSTALL_PATH__+__FILENAME_SDK__
            urlreq.urlretrieve(__WIN_SDK_TOOLS, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)

    except OSError as e:
        print(e)
        return

def handledownloads(option, systemversion):
    try:
        if option == 1 and systemversion == 32:
            future_path = __INSTALL_PATH__+__FILENAME_32__
            urlreq.urlretrieve(__ADT_LINUX_32__, future_path, progress(0, 100000*100000, 0))
            extractfile(future_path)
        if option == 1 and systemversion == 64:
            future_path = __INSTALL_PATH__+__FILENAME_64__
            urlreq.urlretrieve(__ADT_LINUX_64__, future_path, progress(0, 100000*100000, 0))
            extractfile(future_path)
        if option == 2 and systemversion == 64:
            future_path = __INSTALL_PATH__+ __FILENAME_SDK__
            urlreq.urlretrieve(__SDK_TOOLS__, future_path, progress(0, 100000*100000, 0))
            extractfile(future_path)
        if option == 2 and systemversion == 32:
            future_path = __INSTALL_PATH__+__FILENAME_SDK__
            urlreq.urlretrieve(__SDK_TOOLS__, future_path, progress(0, 100000*100000, 0))
            extractfile(future_path)

    except OSError as e:
        print(e)
        return


def asktypeOfdownload(op_system, systemversion):
    sysversion = systemversion
    option = input("Type 1 for ATD Bundle or 2 for SDK Tools only: ")
    print()
    try:
        makeandroidpath()
    except Exception as e:
        print("Error :", e)
        return

    try:
        option = int(option)

        if op_system == "Linux":
                if type(option) == int and sysversion == 32:
                    if option == 1:
                        print("Awesome! Downloading the "+op_system+" 32 bit ADT Bundle for you, please wait.")
                        handledownloads(option, sysversion)

                    if option == 2:
                        print("Awesome! Downloading the "+op_system+" 32 bit SDK Tools for you, please wait.")
                        handledownloads(option, sysversion)

                if type(option) == int and sysversion == 64:

                    if option == 1:
                        print("Awesome! Downloading "+op_system+" 64 bit ADT Bundle for you, please wait.")
                        handledownloads(option, sysversion)

                    if option == 2:
                        print("Awesome! Downloading the "+op_system+" 64 bit SDK Tools for you, please wait.")
                        handledownloads(option, sysversion)

        if op_system == "Windows":
            if type(option) == int and sysversion == 32:
                    if option == 1:
                        print("Awesome! Downloading the "+op_system+" 32 bit ADT Bundle for you, please wait.")
                        handle_win_ownloads(option, sysversion)

                    if option == 2:
                        print("Awesome! Downloading the "+op_system+" 32 bit SDK Tools for you, please wait.")
                        handle_win_downloads(option, sysversion)

            if type(option) == int and sysversion == 64:

                    if option == 1:
                        print("Awesome! Downloading the "+op_system+" 64 bit ADT Bundle for you, please wait.")
                        handle_win_downloads(option, sysversion)

                    if option == 2:
                        print("Awesome! Downloading the "+op_system+" 64 bit SDK Tools for you, please wait.")
                        handle_win_downloads(option, sysversion)


    except Exception as e:
        print("That's not a number, try again.", e)
        asktypeOfdownload(sysversion)

def main():
    print("#########################################################")
    print(__INFO__)
    print(__AUTHOR__)
    print(__VERSION__)
    print("#########################################################")
    systemarchversion = 32
    op_system = ""
    try:
        print("I am trying to figure out what OS you are running on...")
        if islinux():
            op_system = "Linux"
            if checkjvm(op_system):
                if is_86bit():
                    print("OS architecture is 32bit | x86 I am downloading the x86 version of android for you.")
                    asktypeOfdownload(op_system, systemarchversion)
                else:
                    systemarchversion = 64
                    print("OS architecture is 64bit | x64 I am downloading the x64 version of android for you.")
                    asktypeOfdownload(op_system, systemarchversion)
            else:
                installeclipse()
        if iswindows():
            op_system = "Windows"
            if checkjvm(op_system):
                if is_86bit():
                    print("OS architecture is 32bit | x86 I am downloading the x86 version of android for you.")
                    asktypeOfdownload(op_system, systemarchversion)
                else:
                    systemarchversion = 64
                    print("OS architecture is 64bit | x64 I am downloading the x64 version of android for you.")
                    asktypeOfdownload(op_system, systemarchversion)


        else:
            print("I currently don't support systems like your using just yet but "
                  "you can talk to my author about it. He made me.")
    except KeyboardInterrupt:

        if os.path.exists(__INSTALL_PATH__):
            shutil.rmtree(__INSTALL_PATH__)
            print("Cleaning up temp files.....")
        else:
            print("")
        print("Okay done cleaning up! Adeus.")

if __name__ == '__main__':
    main()
