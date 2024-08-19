'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is occurrence of items

'''


def remove_first_occurance(array):
     '''
          Description: 
                this function is removing first item
          Parameters: 
                array: array of item
          Return : 
                not returnig any thing
        '''
     print(array[1:])


def main():
    array=[1,7,3,5,6]
    remove_first_occurance(array)


if __name__=="__main__":
     main()