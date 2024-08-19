'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is list all files in folder

'''


import os

def list_file(directory):
    '''
          Description: 
                this function is list all files
          Parameters: 
                 dictionary: folder
          Return : 
                this function returning count
        '''
    print(os.listdir(directory))


def main():
    directory='camera'
    list_file(directory)


if __name__=="__main__":
    main()