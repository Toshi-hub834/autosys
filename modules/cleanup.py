import subprocess

def clean_temp_files():
    print("Cleaning temporary files...")
    subprocess.call("find /tmp -type f -delete 2>/dev/null", shell=True)
    print("Temporary files cleaned.")
