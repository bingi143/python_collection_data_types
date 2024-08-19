'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program common items in lists

'''


def common_items_in_lists(list_1,list_2):
    '''
          Description: 
                this function we will get common elements in two lists
          Parameters:
              list_1: list - The list of combination elements
              list_2: list -the list of combination elements
          Return :
              it returns the common elements in two lists
    '''
    list_1=set(list_1)
    list_2=set(list_2)
    result=list_1.intersection(list_2)
    return list(result)


def main():
    list_1=[1,2,3,4,434,656]
    list_2=[3,4,1,2,40,43]
    print(f"Common elements are{common_items_in_lists(list_1,list_2)}")

    
if __name__=="__main__":
    main()