'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is calling external commands

'''


import subprocess

def run_command(command):
    '''
          Description: 
                this function is calling external commands
          Parameters: 
                 commands: commands
          Return : 
                this function not returning any thing
        '''
    try:
        
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        
        print("Output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with return code {e.returncode}")
        print("Error output:\n", e.stderr)


def main():
    command = "echo Hello, World!"
    run_command(command)


if __name__=="__main__":
    main()

