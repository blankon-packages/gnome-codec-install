#!/usr/bin/env python

from setuptools import setup
import os.path
import re

if __name__ == "__main__":

    # look/set what version we have
    changelog = "debian/changelog"
    if os.path.exists(changelog):
        head=open(changelog).readline()
        match = re.compile(".*\((.*)\).*").match(head)
        if match:
            version = match.group(1)

    GETTEXT_NAME="gnome-app-install"

    setup(name='gnome-app-install',
          version=version,
          packages=['GnomeCodecInstall'],
          scripts=['gnome-codec-install'],
	  data_files=[]
          )
