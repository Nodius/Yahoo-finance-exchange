from cx_Freeze import setup, Executable

setup(
    name = "Exchange",
    version = "0.2",
    description = "Yahoo Finance",
    executables = [Executable("Exchange.py")]
)
