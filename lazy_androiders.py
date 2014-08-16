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
__ADT_LINUX_32__ = "http://dl.google.com/android/adt/adt-bundle-linux-x86-20140702.zip"
__ADT_LINUX_64__ = "http://dl.google.com/android/adt/adt-bundle-linux-x86_64-20140702.zip"
__INSTALL_PATH__ = "lazy_androiders/"
__FILENAME_32__ = "adt-bundle-linux-x86-20140702.zip"
__FILENAME_64__ = "adt-bundle-linux-x86_64-20140702.zip"
__FILENAME_SDK__ = "android-sdk_r23.0.2-linux.tgz"
__JVM_PATH__ = "/usr/lib/jvm/"
#both 32 bit and 64bit packages are included in this package
__SDK_TOOLS__ = "http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz"


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


def checkjvm():
    print("Checking if JVM is installed....")
    if os.path.exists(__JVM_PATH__):
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


def islinux():
    if platform.system().endswith('Linux'):
        print("Alrighty, seems to me you have a Linux baby! Nice! :) ")
        return True

    else:
        return False


def handledownloads(option, systemversion):
    try:
        if option == 1 and systemversion == 32:
            future_path = __INSTALL_PATH__+__FILENAME_32__
            urlreq.urlretrieve(__ADT_LINUX_32__, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)
        if option == 1 and systemversion == 64:
            future_path = __INSTALL_PATH__+__FILENAME_64__
            urlreq.urlretrieve(__ADT_LINUX_64__, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)
        if option == 2 and systemversion == 64:
            future_path = __INSTALL_PATH__+ __FILENAME_SDK__
            urlreq.urlretrieve(__ADT_LINUX_64__, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)
        if option == 2 and systemversion == 32:
            future_path = __INSTALL_PATH__+__FILENAME_SDK__
            urlreq.urlretrieve(__ADT_LINUX_64__, future_path, progress(0, 100000*100000, -1))
            extractfile(future_path)

    except OSError as e:
        print(e)
        return


def asktypeOfdownload(systemversion):
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

        if type(option) == int and sysversion == 32:
            if option == 1:
                print("Awesome! Downloading the 32 bit ADT Bundle for you, please wait.")
                handledownloads(option, sysversion)

            if option == 2:
                print("Awesome! Downloading the 32 bit SDK Tools for you, please wait.")
                handledownloads(option, sysversion)

        if type(option) == int and sysversion == 64:

            if option == 1:
                print("Awesome! Downloading 64 bit ADT Bundle for you, please wait.")
                handledownloads(option, sysversion)

            if option == 2:
                print("Awesome! Downloading the 64 bit SDK Tools for you, please wait.")
                handledownloads(option, sysversion)

    except Exception as e:
        print("That's not a number, try again.", e)
        asktypeOfdownload(sysversion)

def main():
    print("#########################################################")
    print(__INFO__)
    print(__AUTHOR__)
    print(__VERSION__)
    print("#########################################################")
    systemVersion = 32

    try:
        print("I am trying to figure out what OS you are running on...")
        if islinux():
            if checkjvm():
                if is_86bit():
                    print("OS architecture is 32bit | x86 I am downloading the x86 version of android for you.")
                    asktypeOfdownload(systemVersion)
                else:
                    systemVersion = 64
                    print("OS architecture is 64bit | x64 I am downloading the x64 version of android for you.")
                    asktypeOfdownload(systemVersion)
            else:
                installeclipse()

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
