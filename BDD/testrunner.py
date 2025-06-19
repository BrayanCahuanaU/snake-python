import os
from behave import __main__ as behave_main

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    behave_main.main("features/")  # Especifica la ruta relativa