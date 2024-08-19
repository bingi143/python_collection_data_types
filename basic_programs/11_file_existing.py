'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is file exist or not checking

'''


import os

def check_file(file):
     '''
          Description: 
                this function is check file exist por not
          Parameters: 
                 file: file 
          Return : 
                this function not returning any thing
        '''

     if os.path.isfile(file):
         print("file is exist")
     else:
         print("file not exist")


def main():
    file="D:\sv\WhatsApp_files\9pVubVHS-08.js.download"
    check_file(file)


if __name__=="__main__":
    main()