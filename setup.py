import sys
from cx_Freeze import setup, Executable

target = Executable(script="Main_Program_Design.py",
                    base = "Win32GUI",
                    icon="Meat_Icon.ico")

setup(name="Meat Shop Management System",
      version = "1.0",
      description="A simple program that helps the owner compute the order of the clients.",
      executables = [target])
