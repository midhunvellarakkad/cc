


import ctypes, sys
import win32evtlog
import xml.etree.ElementTree as ET
import ctypes
import sys
import subprocess, sys
p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "C:\\cevent\\4624.ps1"', stdout=sys.stdout)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
      p.communicate()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
