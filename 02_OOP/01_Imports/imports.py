import time

time.sleep(5)

from time import sleep

sleep(5)

from random import randint

print(randint(55, 100))

import random

print(random.randint(55, 100))

# Import a file from the project :

from myFile import my_function

my_function()

from sub_directory.otherFile import test, test2

test()

# Something that is important when importing files from a project is that the root directory is linked to the file currently being executed.

# subdirectory/
#       |-> myfile.py
#       |-> otherFile.py
# file.py
# main.py

# If I execte main.py, all the import path will be from the directory where main.py is located
# So I would have :
# from subdirectory.myFile import content
# If I execute otherFile.py
# THen the root directory would be subdirectory so I would import myFile as :
# from myFile import content