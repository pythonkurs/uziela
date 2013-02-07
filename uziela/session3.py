#!/usr/bin/env python

# Written by Karolis Uziela in 2013

import os

class CourseRepo(object):
    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self, surname):
        self._surname = surname
        self.required=[".git", "setup.py", "README.md", "scripts/getting_data.py", "scripts/check_repo.py", self._surname + "/__init__.py", self._surname + "/session3.py"]
    def __init__(self, surname):
        self.surname = surname
    def check(self):
        answer = True
        for elem in self.required:
            if not os.path.exists(elem):
                answer = False
        return answer

class repo_dir(object):
    def __init__(self, new_dir):
        self.new_dir = new_dir
        self.old_dir = None

    def __enter__(self):
        self.old_dir = os.getcwd()
        os.chdir(self.new_dir)

    def __exit__(self, *_):
        os.chdir(self.old_dir)

