'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program is displaying array items

'''


def display_array(array):
    '''
          Description: 
                this function displaying array items
          Parameters: 
                array: array of items
          Return : 
                this function not returning  any thing
        '''
    for i in range(0,len(array)):
        print(array[i])


def main():
    array=[1,3,5,6,8]
    display_array(array)


if __name__=="__main__":
    main()