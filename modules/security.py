import os

def check_open_ports():
    print("Checking open ports...")
    os.system("ss -tuln")
