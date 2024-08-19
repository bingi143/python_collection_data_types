'''

@Author: Venkatesh
@Date: 2024-08-17 18:00:30
@Last Modified by: Venkatesh
@Last Modified time: 2024-08-17 18:00:30
@Title : Python Program append of two lists

'''


def append_two_lists(list_1,list_2):
    '''
          Description: 
                this function we will get two list to be combined
          Parameters:
              list_1: list - The list of combination elements
              list_2: list -the list of combination elements
          Return :
              after addinng two lists returned
    '''
    list_result=list_1+list_2
    return list_result


def main():
    list_1=[3,5,6,"hi","venky",43]
    list_2=["chelo",3,5,90]
    print(f"After appending two lists{append_two_lists(list_1,list_2)}")


if __name__=="__main__":
    main()