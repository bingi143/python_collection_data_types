'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is environment variable

'''


import os

def method(variable_value,variable_name):
    '''
          Description: 
                this function geting enviroment variable
          Parameters: 
                variable_value: value
                variable_name: name of variable
          Return : 
                this function returning count
        '''
    if variable_value:
        print(f"The value of {variable_name} is: {variable_value}")
    else:
        print(f"{variable_name} is not set in the environment.")


    print("\nAll environment variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")


def main():
    variable_name = 'ENV_VARIABLE_NAME'
    variable_value = os.getenv(variable_name)
    method(variable_value,variable_name)


if __name__=="__main__":
    main()
