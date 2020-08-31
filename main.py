# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import Set


def filternames():
    # Use a breakpoint in the code line below to debug your script.
    dudes = {"lee", "rich", "todd", "john", "peter"}
    for dude in dudes:
        if "o" in dude:
            print(dude)
            
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filternames()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
