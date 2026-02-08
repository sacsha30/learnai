import os
from os import removedirs

path = os.getcwd()
print(path)

path = os.chdir("/Users/sunny/PycharmProjects/learnai/pythonfundamentals/")
print(path)

os.makedirs("testdir")
print(path)

path = removedirs("testdir")
print(path)

#
from pathlib import Path

my_path = Path.home()
my_path = Path(my_path, "Total Python","Day 6","path_practice.py")

