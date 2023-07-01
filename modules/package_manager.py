import os

def update_packages():
    print("Updating packages...")
    os.system("sudo apt update && sudo apt upgrade -y")
    print("Packages updated.")
