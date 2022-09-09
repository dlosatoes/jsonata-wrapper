#!/usr/bin/python3
# This script updates jsonata-es5.min.js to the latest version built from the jsonata repo.
from os import chdir
from os import path, remove
import sys
import requests
from shutil import rmtree, copy
import tarfile
from git import Repo
from git.exc import GitCommandError
from pynpm import NPMPackage
clonedir = "jsonata_clone"
cloneurl = "https://github.com/jsonata-js/jsonata.git"
targetfile = "jsonata-es5.min.js"
duktapehost = "https://duktape.org/"
duktapetar = "duktape-2.7.0.tar.xz"
duktapedir = "duktape-2.7.0"
duktapeurl = duktapehost + duktapetar
clonedir2 = "pybind11"
cloneurl2 = "https://github.com/pybind/pybind11.git"
try:
    rep = Repo.clone_from(cloneurl, clonedir)
except GitCommandError as exp:
    print("Problem cloning jsonata:")
    print(exp)
    sys.exit(1)
if path.exists(clonedir2):
    rmtree(clonedir2)
try:
    rep = Repo.clone_from(cloneurl2, clonedir2)
    rmtree(path.join(clonedir2,".git"))
except GitCommandError as exp:
    print("Problem cloning pybind11:")
    print(exp)
    sys.exit(1)
chdir(clonedir)
try:
    pkg = NPMPackage('./package.json')
    pkg.install()
    pkg.run_script('build-es5')
    oldfile = path.join("..","targetfile")
    if path.exists(oldfile) and path.exists(targetfile):
        remove(oldfile)
    copy(targetfile, "..")
except Exception as exp:
    print("Problem building minimized jsonata javascript file:")
    print(exp)
chdir("..")
rmtree(clonedir)
print("Fetching:", duktapeurl)
r = requests.get(duktapeurl, allow_redirects=True)
open(duktapetar, 'wb').write(r.content)
if path.exists(duktapedir):
    rmtree(duktapedir)
tar = tarfile.open(duktapetar)
tar.extractall()
tar.close()
remove(duktapetar)
