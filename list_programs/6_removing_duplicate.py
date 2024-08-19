'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program removing duplicate values

'''


def remove_duplicate_items_list(list_):
    '''
          Description: 
                this function remove the duplicate elements in list
          Parameters:
              list1: list - The list of numbers
          Return :
              it returns the after removing of duplicate values in list

    '''
    return list(set(list_))


def main():
    list=[2,34,56,7,65,2,56,78,7]
    print("After removing duplicates:",remove_duplicate_items_list(list))


if __name__=="__main__":
    main()