import requests
from config import DOWNLOAD_URL, VM_FILENAME

def download_vm():
    print(f"Downloading Luau VM from {DOWNLOAD_URL}...")
    response = requests.get(DOWNLOAD_URL)
    with open(VM_FILENAME, "wb") as f:
        f.write(response.content)
    print("Downloaded Luau VM.")
