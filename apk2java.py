#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys, os, string
import urllib.request
import zipfile
import subprocess
from optparse import OptionParser

class APK2Java:
    external = "https://github.com/TheZ3ro/apk2java-linux/releases/download/tool2/tool.zip"

    def __init__(self):
        self.home = ''
        self.tool = ''
        self.outdir = ''
        self.apk_file = ''
        self.project_name = ''
        self.smali = False
        self.nosc = False

    def _call(self, cmd, **kwargs):
        print('Running: {0}'.format(' '.join(cmd)))
        return subprocess.call(cmd, **kwargs)

    def _report(self, blocknr, blocksize, size):
        current = blocknr * blocksize
        sys.stdout.write("\rProgress: {0:.2f}%".format(100.0 * current / size) + " - {0:.1f} MB".format(
            current / 1024 / 1024) + "/{0:.1f} MB".format(size / 1024 / 1024))

    def _check_home(self, path):
        return os.path.isdir(path + "/tool")

    def _getunzipped(self, theurl, thedir, report):
        if not os.path.exists(thedir):
            os.mkdir(thedir)
        print("Downloading external tool... -> " + thedir + "/tool/")
        name = os.path.join(thedir, 'temp.zip')
        try:
            name, hdrs = urllib.request.urlretrieve(theurl, name, report)
        except IOError as e:
            print("Can't retrieve %r to %r: %s" % (theurl, thedir, e))
            return
        try:
            z = zipfile.ZipFile(name)
        except zipfile.error as e:
            print("Bad zipfile (from %r): %s" % (theurl, e))
            return
        for n in z.namelist():
            (dirname, filename) = os.path.split(n)
            perm = ((z.getinfo(n).external_attr >> 16) & 0x0777)
            if filename == '':
                # directory
                newdir = thedir + '/' + dirname
                if not os.path.exists(newdir):
                    os.mkdir(newdir)
            else:
                # file
                fd = os.open(thedir + "/" + n, os.O_CREAT | os.O_WRONLY, perm)
                os.write(fd, z.read(n))
                os.close(fd)
        z.close()
        os.unlink(name)
        print("")

    def check_tools(self, home):
        if self._check_home(home) == False:
            self._getunzipped(APK2Java.external, home, self._report)
        self.home = home
        self.tool = os.path.join(self.home, 'tool/')

    def _print_header(self, text):
        block = "*********************************************"
        print(block)
        print('**' + text.center(len(block) - 4) + '**')
        print(block)


    def _apktool(self):
        self._print_header('Extract, fix resource files')
        if self.apk_file != '':
            cmd = ['java', '-jar', os.path.join(self.tool, 'apktool_2.3.0.jar'), 'd', self.apk_file, '-o', self.out, '-f']

            if not self.smali:
                cmd[-1] = '-sf'

            self._call(cmd)

            if not self.smali:
               self._call(['mv', os.path.join(self.out, 'classes.dex'), os.path.join(self.out, 'original/')])
        print('Done')


    def _dex2jar(self):
        self._print_header("Convert 'apk' to 'jar'")
        if self.apk_file != '':
            self._call([os.path.join(self.tool, 'dex2jar-2.0/d2j-dex2jar.sh'), '-f', '-o', self.out + '.jar', self.apk_file])
            print('Done')


    def _cfr(self):
        self._print_header('Decompiling class files')
        if self.apk_file != '':
            self._call(['java', '-jar', os.path.join(self.tool, 'cfr_0_123.jar'), self.out + '.jar',
                  '--outputdir', os.path.join(self.out, 'src/')])
            print('Done')


    def decompile(self, file):
        if os.path.isfile(file) and os.path.splitext(file)[-1].lower() == '.apk':
            self.apk_file = file
            self.project_name = os.path.splitext(os.path.basename(file))[0].lower()
            self.out = os.path.join(self.outdir, self.project_name)
            
            if not os.path.exists(self.outdir):
                os.makedirs(self.outdir)

            self._call(["cp", self.apk_file, os.path.join(self.outdir, self.project_name + "-new.apk")])

            self._apktool()
            if self.smali == False and self.nosc == False:
                self._dex2jar()
                self._cfr()

            print("Output source is at {}".format(self.out))
        else:
            raise Exception("You must select a valid APK file!")


def main():
    # current working directory
    cwd = os.getcwd()
    # apk2java installation path
    home = os.path.dirname(os.path.realpath(sys.argv[0]))

    usage = "usage: %prog file [options]"
    parser = OptionParser(usage=usage)
    parser.add_option("--java", action="store_true", dest="java", default=True,
                      help="select java source format [DEFAULT]")
    parser.add_option("--smali", action="store_true", dest="smali", default=False, help="select smali source format")
    parser.add_option("--no-source", action="store_true", dest="nosc", default=False, help="no source code generation")
    parser.add_option("-o", dest="outdir", default=cwd, help="specify the output directory "
                                                                   + "(if not specified the decomipled version will be store in a folder in the script directory)")
    (options, args) = parser.parse_args()

    app = APK2Java()
    # check if tools are instaled in the script dir
    app.check_tools(home)

    # by default is cwd
    app.outdir = options.outdir

    if (options.smali + options.nosc) > 1:
        parser.error("You can only select 1 source format --[smali/java/no-source]")
        exit(1)

    app.smali = options.smali
    app.nosc = options.nosc

    if len(args) == 1:
        app.decompile(args[0])
    else:
        parser.print_help()


# Script start Here
if __name__ == "__main__":
    main()
