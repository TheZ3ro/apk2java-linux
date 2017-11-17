apk2java-linux
==============

This project is a porting for Linux/*nix of https://github.com/rajivvishwa/apk2java that works only on Windows


Introduction
--------------------
This script decompiles an apk to its corresponding java sources. Security code review can be done on theses generated application source files so as to identify any potential vulnerabilities present.
This is not made to encourage piracy/plagiarism.

 ***This script just automates the sequence in which various tools are initiated and does not handle any error events. You will have to go through the cmd verbose to figure out the problem.***

Usage
--------------------
```
Usage: apk2java.py <ApkFileName> [options]

Options:
  -h, --help   show this help message and exit
  --java       select java source format [DEFAULT]
  --smali      select smali source format
  --no-source  no source code generation
```

Requirements
--------------------
JRE >1.7 (Java Runtime Environment)  
Python >3


Tools used
--------------------
Dex2jar : http://code.google.com/p/dex2jar/  
cfr : http://www.benf.org/other/cfr/  
apk-tool : http://code.google.com/p/android-apktool/  
baksmali : http://code.google.com/p/smali/

Note: These tools and a sample apk are downloaded by the script. There is not need to download them manually
