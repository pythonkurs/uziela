#!/usr/bin/env python

# Written by Karolis Uziela in 2013

from uziela.session3 import CourseRepo,repo_dir
import sys
import os

def test1():
    repo = CourseRepo("a")
    print(repo.required[-1])

    repo.surname = "b"
    print(repo.required[-1])

def test2():
    repo = CourseRepo("uziela")
    print(repo.check())

try:
    target_dir = os.path.abspath(sys.argv[1])
except OSError:
    sys.exit("Entered directory does not exist. Usage: check_repo.py <dir_name>")

lastname = os.path.basename(target_dir)

with repo_dir(target_dir):
    repo = CourseRepo(lastname)
    if repo.check():
        print "PASS"
    else:
        print "FAIL"
