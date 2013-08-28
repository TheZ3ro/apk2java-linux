apk2java-linux
==============

This project is a porting for Linux/*nix of https://github.com/rajivvishwa/apk2java that works only on Windows


Introduction
--------------------
This batch file decompiles an apk to its corresponding java sources. Security code review can be done on theses generated applicaion source files so as to identify any potential vulnerabilities present. 
This is not made to encourage piracy/plagiarism. 

 *** This script just automates the sequence in which various tools are initiated and does not handle any error events. You will have to go through the cmd verbose to figure out the problem.  ***

Install
--------------------
Just execute the install.sh file from a ROOT terminal

    # ./install.sh

For uninstall the script type in a ROOT terminal:

    # ./uninstall.sh
    
or

    # /opt/apk2java/uninstall.sh

Usage
--------------------
	$ apk2java [smali] <file>.apk

Note: The smali option is optional

Requirements
--------------------
JRE 1.6 (Java Runtime Environment)

Tools used
--------------------
Dex2jar : http://code.google.com/p/dex2jar/

JAD : http://www.varaneckas.com/jad

apk-tool : http://code.google.com/p/android-apktool/

baksmali : http://code.google.com/p/smali/

