# Will only execute if I execute this file directly via the command line :
# python3 main_example.py
if __name__ == '__main__':
    print("Hello World")

# Because this line is not inside the __name__ == 'main' this line will also be executed
# when importing the file, so doing
# import main_example
# or
# from main_example import *
# will execute this line.
print("Hello not from main")