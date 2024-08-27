import os
import sys
import subprocess
import platform

def activate_virtualenv():
    """
    Determine the correct path to the virtual environment activation script
    based on the operating system and the provided virtual environment structure.
    """
    if platform.system() == 'Windows':
        # For Windows: Assume a PowerShell script to activate in 'bin'
        activate_script = os.path.join('virtual_env', 'bin', 'Activate.ps1')
    else:
        # For Linux/Unix: Use the standard 'bin/activate' script
        activate_script = os.path.join('virtual_env', 'bin', 'activate')
    
    # if not os.path.exists(activate_script):
    #     raise RuntimeError(f"Could not find the virtual environment activation script at {activate_script}. Please ensure the virtual environment is set up properly.")

    return activate_script

def run_django_server():
    """
    Run the Django development server in a subprocess with the virtual environment activated.
    """
    try:
        # Ensure manage.py exists in the 'paszmix' directory
        # manage_py_path = os.path.join('paszmix', 'manage.py')
        # if not os.path.exists(manage_py_path):
        #     raise RuntimeError(f"{manage_py_path} not found. Ensure you're in the correct directory and the 'paszmix' folder exists.")

        # Get the path to the activation script
        activate_script = activate_virtualenv()

        # Construct the command to activate the virtual environment and run the server
        if platform.system() == 'Windows':
            # Windows: Use PowerShell to activate the environment and then change directory and run the Django server
            command = f'powershell.exe -ExecutionPolicy Bypass -File "{activate_script}"; cd paszmix; python manage.py runserver'
        else:
            # Linux/Unix: Use bash to source the activation script and then change directory and run the Django server
            command = f"source {activate_script} && cd paszmix && exec python manage.py runserver"

        # Execute the command in the appropriate shell
        subprocess.run(command, shell=True, executable='/bin/bash' if platform.system() != 'Windows' else None, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error while running the server: {e}")
        sys.exit(1)
    except RuntimeError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    run_django_server()
