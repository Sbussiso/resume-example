import shutil
import os

def zip_install_folder():
    shutil.make_archive('scripts/install', 'zip', 'scripts/install')

if __name__ == "__main__":
    zip_install_folder()
