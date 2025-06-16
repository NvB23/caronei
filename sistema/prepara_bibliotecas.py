import importlib.util
import os
import subprocess
import sys

def instalaBibliotecas(nomeDasBibliotecas):
    for biblioteca in nomeDasBibliotecas:
        if(importlib.util.find_spec(biblioteca) is None):
            subprocess.check_call([sys.executable, "-m", "pip", "install", biblioteca])
            os.system("cls" if os.name == "nt" else "clear")

def preparaBibliotecas():
    instalaBibliotecas(["pwinput", "deep_translator", "qrcode", "pillow", "pybrcode", "ast"])