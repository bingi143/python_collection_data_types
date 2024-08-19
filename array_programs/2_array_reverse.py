'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is displaying array items in reverse

'''


import array

def reverse_Array(array_):
    '''
          Description: 
                this function is reversing an array
          Parameters: 
                array: array of items
          Return : 
                this function is reveres array is returned
        '''
    array_.reverse()
    print(array_)
    return array_


def main():
    array_=[2,3,4,5,6]
    reverse_Array(array_)


if __name__=="__main__":
    main()