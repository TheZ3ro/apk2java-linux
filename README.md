apk2java-linux
==============

This project is a porting for Linux/*nix of https://github.com/rajivvishwa/apk2java that works only on Windows


Introduction
--------------------
This script decompiles an apk to its corresponding java sources. Security code review can be done on theses generated applicaion source files so as to identify any potential vulnerabilities present. 
This is not made to encourage piracy/plagiarism. 

 *** This script just automates the sequence in which various tools are initiated and does not handle any error events. You will have to go through the cmd verbose to figure out the problem.  ***

Usage
--------------------
```
Usage: apk2java.py action file [options]

Options:
  -h, --help   show this help message and exit
  --java       select java source format [DEFAULT]
  --smali      select smali source format
  --jasmin     select jasmin source format
  --no-source  no source code generation
```

Requirements
--------------------
JRE 1.7 (Java Runtime Environment)
Python 3


Tools used
--------------------
Dex2jar : http://code.google.com/p/dex2jar/

Procyon : https://bitbucket.org/mstrobel/procyon/wiki/Java%20Decompiler

apk-tool : http://code.google.com/p/android-apktool/

baksmali : http://code.google.com/p/smali/

