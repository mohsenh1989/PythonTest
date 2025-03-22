import os
from openpyxl import load_workbook

class Color :
    Red = '\033[91m'
    Cyan = '\033[96m'
    Blue = '\033[94m'
    Yellow = '\033[93m'
    Bold = '\033[1m'
    Under = '\033[4m'
    Green = '\033[92m'
    End = '\033[0m'



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
       print(Color.Red+ 'hi' + Color.End)
       print(Color.Cyan + "======================================" + Color.End)

