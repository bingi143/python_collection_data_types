'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program smallest element inlist

'''


def smallest_item_list(list_):
    '''
          Description: 
              The function is smallest items in the list   
          Parameters:
              list1: list - The list of numbers
          Return :
              smallest element in list

    '''
    small=min(list_)
    return small


def main():
    list_=[2,4,5,6,7,10]
    print("Smallest element in list is",smallest_item_list(list_))


if __name__=="__main__":
    main()