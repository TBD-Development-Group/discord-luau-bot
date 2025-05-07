import requests
import zipfile
import os
from config import DOWNLOAD_URL, ZIP_FILENAME, VM_FILENAME

def download_vm():
    if os.path.exists(VM_FILENAME):
        print(f"[VM] {VM_FILENAME} already exists.")
        return

    print("[VM] Downloading Luau VM for Windows...")
    response = requests.get(DOWNLOAD_URL)
    if response.status_code == 200:
        with open(ZIP_FILENAME, "wb") as f:
            f.write(response.content)
        print(f"[VM] Downloaded {ZIP_FILENAME}")

        # Extract luau.exe from the ZIP
        with zipfile.ZipFile(ZIP_FILENAME, 'r') as zip_ref:
            zip_ref.extract(VM_FILENAME)
        print(f"[VM] Extracted {VM_FILENAME}")

        # Clean up the ZIP file
        os.remove(ZIP_FILENAME)
        print(f"[VM] Removed {ZIP_FILENAME}")
    else:
        print(f"[ERROR] Failed to download VM. Status code: {response.status_code}")
