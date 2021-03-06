#!/usr/bin/env python

"""
Lazy Androiders is a simple tool that downloads and sets ups the android tools and dependencies for you.
Now it's easy Peezy! No more hassles!
"""

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
import subprocess as sb
import sys

if sys.hexversion < 0x3040000:
    print("Please install python3.4 and up to use Lazy Androiders.")
    sys.exit(1)


__VERSION__ = "Version 1.0"
__AUTHOR__ = "Alexandre Juca <corextechnologies@gmail.com>"
__INFO__ = "Lazy Android - The lazy Android Developers mate."
#########################################################################################
__ADT_LINUX_32__ = "https://dl.google.com/android/adt/adt-bundle-linux-x86-20140702.zip"
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
__WIN_JDK_32__ = "http://download.oracle.com/otn-pub/java/jdk/8u11-b12/jdk-8u11-windows-i586.exe"
__WIN_JDK_64__ = "http://download.oracle.com/otn-pub/java/jdk/8u11-b12/jdk-8u11-windows-x64.exe"

future_path = ""
__jvm_download_path__ = "jdk_install/"


def execjdk(path):
    if os.path.isfile(path) and path.endswith('.exe'):
        sb.call(['start', path])
    else:
        print("Seems like the downloaded jdk file is not in "+path)


def downloadjvm():
    if is_86bit():
        jpath = __jvm_download_path__+"jdk-8u11-windows-i586.exe"
        urlreq.urlretrieve(__WIN_JDK_32__, jpath,
                           progress(0, 100000*100000, -1))
        execjdk(jpath)
    if is_86bit() is False:
        jpath = __jvm_download_path__+"jdk-8u11-windows-x64.exe"
        urlreq.urlretrieve(__WIN_JDK_64__, jpath,
                           progress(0, 100000*100000, -1))
        execjdk(jpath)


def installeclipse():
    print("Installing eclipse....")
    sb.call(['apt-get', 'install', 'eclipse'])
    print("eclipse has been installed on your system.")
    main()


def extractfile(output_path):
    if output_path.endswith('.zip'):
        print("Unzipping to : "+output_path+" patience will be needed.")
        try:
            sb.call(["unzip", "-d android-dev/", output_path])
            print("Extracted contents to : android-dev/")
            sys.exit(0)
        except Exception as e:
            print("Failed in extraction phase: %s", e)
            sys.exit(1)

    if output_path.endswith('.tgz'):
        print("Extracting file to : "+output_path+" patience will be needed.")
        try:
            sb.call(["unzip", "-d android-dev/", output_path])
            print("Extracted contents to : android-dev/")
        except Exception as e:
            print("Failed in extraction phase: %s", e)
            sys.exit(1)

    else:
        print("Format seems wrong....")
        sys.exit(1)

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
        print("I'm downloading the dependencies for your system, have a cup of coffee while I work.... "+str(chunk)) #We need to find a way to display progress during the download process


def is_86bit():
    """Check if the machine is 32 bit or not

    """
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
            extract_path = __INSTALL_PATH__+__FILENAME_32__
            urlreq.urlretrieve(__ADT_LINUX_32__, extract_path, progress(0, 100000*100000, 0))
            extractfile(extract_path)
        if option == 1 and systemversion == 64:
            extract_path = __INSTALL_PATH__+__FILENAME_64__
            urlreq.urlretrieve(__ADT_LINUX_64__, extract_path, progress(0, 100000*100000, 0))
            extractfile(extract_path)
        if option == 2 and systemversion == 64:
            extract_path = __INSTALL_PATH__+ __FILENAME_SDK__
            urlreq.urlretrieve(__SDK_TOOLS__, extract_path, progress(0, 100000*100000, 0))
            extractfile(extract_path)
        if option == 2 and systemversion == 32:
            extract_path = __INSTALL_PATH__+__FILENAME_SDK__
            urlreq.urlretrieve(__SDK_TOOLS__, extract_path, progress(0, 100000*100000, 0))
            extractfile(extract_path)

    except OSError as e:
        print(e)
        return


def asktypeofdownload(op_system, systemversion):
    sysversion = systemversion
    option = input("Type 1 for ATD Bundle or 2 for SDK Tools only: ")
    print()
    try:
        makeandroidpath()
    except Exception as e:
        print("Error creating path :", e)
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
                        handle_win_downloads(option, sysversion)

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
        print("That's not a valid option, try again.", e)
        asktypeofdownload(sysversion)

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
                    asktypeofdownload(op_system, systemarchversion)
                else:
                    systemarchversion = 64
                    print("OS architecture is 64bit | x64 I am downloading the x64 version of android for you.")
                    asktypeofdownload(op_system, systemarchversion)
            else:
                installeclipse()
        if iswindows():
            op_system = "Windows"
            if checkjvm(op_system):
                if is_86bit():
                    print("OS architecture is 32bit | x86 I am downloading the x86 version of android for you.")
                    asktypeofdownload(op_system, systemarchversion)
                else:
                    systemarchversion = 64
                    print("OS architecture is 64bit | x64 I am downloading the x64 version of android for you.")
                    asktypeofdownload(op_system, systemarchversion)
            else:
                    downloadjvm()

        else:
            print("I currently don't support systems like your using just yet but "
                  "you can talk to my author about it. He made me.")
            sys.exit(1)

    except KeyboardInterrupt:

        if os.path.exists(__INSTALL_PATH__):
            shutil.rmtree(__INSTALL_PATH__)
            print("Cleaning up temp files.....")
        else:
            print("")
        print("Okay done cleaning up! Adeus.")

if __name__ == '__main__':
    main()
