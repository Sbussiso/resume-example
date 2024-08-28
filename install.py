import platform
import subprocess
import os

def install():
    system_platform = platform.system()
    script_dir = os.path.dirname(os.path.abspath(__file__))

    if system_platform == "Windows":
        script_path = os.path.join(script_dir, 'script.ps1')
        command = f'powershell.exe -Command "Start-Process powershell.exe -ArgumentList \'-ExecutionPolicy Bypass -File {script_path}\' -Verb RunAs"'
    else:
        script_path = os.path.join(script_dir, 'script.sh')
        command = f'sudo bash {script_path}'

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed the install script for {system_platform}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute the install script: {e}")

if __name__ == "__main__":
    install()
