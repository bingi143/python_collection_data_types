'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program copying list

'''


def copyinng_list(list_):
    '''
          Description: 
                this function copying the elements in one list to another
          Parameters:
              list1: list - The list of numbers
          Return :
              it returns the after copying elements

    '''
    return list_.copy()


def main():
    list=[2,4,5,65,4,657,98,"hello","chelo"]
    copy_list=copyinng_list(list)
    print(copy_list)


if __name__=="__main__":
    main()